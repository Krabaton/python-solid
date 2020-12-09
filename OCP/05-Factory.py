from enum import Enum


class ReportType(Enum):
    HTML = 'Html'
    TEXT = 'Text'


class Formatter:
    def format(self, data):
        pass


class HtmlFormatter(Formatter):
    def format(self, data):
        return f'<div>{data}</div>'


class TextFormatter(Formatter):
    def format(self, data):
        return str(data)


class FormatterFactory:
    @staticmethod
    def create_formatter(type_format):
        return formatter_strategy(type_format)


def formatter_strategy(type_format):
    type_dict = {
        ReportType.HTML: HtmlFormatter(),
        ReportType.TEXT: TextFormatter()
    }
    return type_dict.get(type_format, TextFormatter())


class ReportExport:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def export(self, report_type):
        formatter = FormatterFactory.create_formatter(report_type)
        return formatter.format(self.data)


report = ReportExport('Log: ', 'Test data')
result = report.export(ReportType.HTML)
print(result)
