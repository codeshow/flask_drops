from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    """<regex("reg_expression_here"):name>
    Matches URL for exact reg expression"""
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


class ListConverter(BaseConverter):
    """<list:names>
    converts /nome+nome2+nome3/ to ['nome', 'nome2', 'nome3']"""

    def to_python(self, value):
        return value.split('+')

    def to_url(self, values):
        return '+'.join(
            BaseConverter.to_url(self, item)
            for item in values
        )
