from bundles import css_bundle, js_bundle
from flask import Flask
from flask.ext.assets import Environment
from hamlish_jinja import HamlishExtension


app = Flask(__name__)
app.jinja_env.add_extension(HamlishExtension)

assets = Environment(app)
assets.url = app.static_url_path
assets.register('css_all', css_bundle)
assets.register('js_all', js_bundle)

import views
