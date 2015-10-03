from filters import SasscFilter
from flask.ext.assets import Bundle
from webassets.filter import register_filter


register_filter(SasscFilter)

css_bundle = Bundle('css/base.scss', filters='sassc', output='.generated/all.css')
js_bundle = Bundle('js/base.js', output='.generated/all.js')
