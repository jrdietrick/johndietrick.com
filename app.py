from bundles import css_bundle, js_bundle
from flask import Flask
from flask.ext.assets import Environment
from hamlish_jinja import HamlishExtension


app = Flask(__name__)

template_env = app.jinja_env
template_env.add_extension(HamlishExtension)
template_env.hamlish_mode = 'indented'
template_env.hamlish_enable_div_shortcut = True

assets = Environment(app)
assets.url = app.static_url_path
assets.register('css_all', css_bundle)
assets.register('js_all', js_bundle)

import views
