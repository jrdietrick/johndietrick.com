from webassets.filter import Filter


try:
    from sassc import compile as sassc_compile
except ImportError:
    def sassc_compile(*args, **kwargs):
        raise NotImplementedError


class SasscFilter(Filter):
    name = 'sassc'

    def output(self, _in, out, **kwargs):
        out.write(_in.read())

    def input(self, _in, out, **kwargs):
        out.write(sassc_compile(string=_in.read()))
