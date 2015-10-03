from app import app
from bundles import css_bundle, js_bundle
from flask.ext.assets import Environment


if __name__ == '__main__':
    assets = Environment(app)
    css_bundle.build()
    js_bundle.build()
