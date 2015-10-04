from fabric.api import run, env, local, cd, hosts, put
from fabric.colors import green, cyan, red, yellow

# Some assumptions:
#
# * /opt/apps/johndietrick.com exists on the remote machine, is writable
#   by the (SSH) user of this script, and is where the webserver (uWSGI)
#   is serving from
#
# * /git/johndietrick.com.git is a bare git repo on the remote end
#   (initialized empty with`git init --bare /git/johndietrick.com.git`).
#   This repo *could* also act as your `origin`, but I'd really not
#   recommend it. It only exists so we can push diffs rather than the whole
#   codebase on each deploy.
#
# * uWSGI is your server of choice and it runs based on a configuration
#   file uwsgi.ini, which if touched will cause the server to gracefully
#   pick up changes.
#
# * The "let's locally compile assets and then put() them up" solution is
#   a hack because I couldn't get libsass (the C++ lib) to compile on my
#   VPS server -- not enough RAM. If you have a server with more than 64kB
#   of RAM, that should be enough for anyone... so you may not need those
#   parts.

APPS_BASE_DIR = '/opt/apps/'
APP_NAME      = 'johndietrick.com'
APP_PATH      = '%s%s' % (APPS_BASE_DIR, APP_NAME)
GIT_PATH      = '/git/johndietrick.com.git'
GIT_BRANCH    = 'master'


def _git_push(bare_repo_path, branch_to_push):
    print cyan('Syncing code...', bold=True)
    if env.user:
        git_login = '%s@%s' % (env.user, env.host)
    else:
        git_login = env.host
    local('git push -vf ssh://%s%s %s:%s' % (git_login, bare_repo_path, branch_to_push, branch_to_push))


@hosts(['johndietrick.com'])
def git_push(branch=None):
    branch_to_push = GIT_BRANCH if branch == None else branch
    _git_push(GIT_PATH, branch_to_push)


def _git_checkout_to_dir(bare_repo_path, checkout_to, branch):
    with cd(bare_repo_path):
        print yellow('Checking out branch "%s" from %s into %s...' % (branch, bare_repo_path, checkout_to), bold=True)
        run('mkdir -p %s' % checkout_to)
        run('GIT_WORK_TREE=%s git checkout -f %s' % (checkout_to, branch))


@hosts(['johndietrick.com'])
def git_checkout(branch=None):
    branch_to_checkout = GIT_BRANCH if branch == None else branch
    _git_checkout_to_dir(GIT_PATH, APP_PATH, branch_to_checkout)


def _restart_uwsgi():
    with cd(APP_PATH):
        print cyan('Restarting uWSGI...', bold=True)
        run('touch uwsgi.ini')


@hosts(['johndietrick.com'])
def touch():
    _restart_uwsgi()


@hosts(['johndietrick.com'])
def deploy(branch=None):
    branch_to_push = GIT_BRANCH if branch == None else branch

    if not _scary_confirm('You\'re pushing to the production server. Set condition one throughout the ship!'):
        return
    print ''

    # Compile assets locally
    print cyan('Compiling assets...', bold=True)
    local('rm -rf static/.webassets-cache')
    local('rm -rf static/.generated')
    local('. venv/bin/activate && python build_assets.py')
    print ''

    # Push the latest code up
    _git_push(GIT_PATH, branch_to_push)
    print ''

    # Check out the latest code
    _git_checkout_to_dir(GIT_PATH, APP_PATH, branch_to_push)

    with cd(APP_PATH):
        print yellow('Installing requirements...', bold=True)
        run('source venv/bin/activate && pip install -r requirements.txt')

    print cyan('Uploading assets...', bold=True)
    put('static/.webassets-cache/', APP_PATH + '/static/')
    put('static/.generated/', APP_PATH + '/static/')
    print ''

    _restart_uwsgi()
    print ''

    print green('Deploy to %s OK.' % env.host, bold=True)


def _scary_confirm(message):
    print yellow('*' * 80)
    print yellow(message, bold=True)
    print yellow('*' * 80)
    confirm = raw_input(red('...are you sure? [y/N] ', bold=True))
    return confirm.lower() == 'y'
