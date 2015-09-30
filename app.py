from flask import Flask
from flask.ext.assets import Environment, Bundle
from hamlish_jinja import HamlishExtension


app = Flask(__name__)
app.jinja_env.add_extension(HamlishExtension)


# compile assets
assets = Environment(app)
assets.url = app.static_url_path

css_bundle = Bundle('css/base.scss', filters='scss', output='all.css')
assets.register('css_all', css_bundle)

import views
