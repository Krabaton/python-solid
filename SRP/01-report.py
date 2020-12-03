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


'''
Принцип единой ответственности подсказывает, что выбор формата не входит ни в задачу форматирования данных, 
ни в задачу их подготовки. Поэтому существующие классы нам не подойдут.
Создадим новый класс FormatSelector, который будет выбирать тип форматирования, в зависимости от настроек.
'''


class FormatSelector:
    @staticmethod
    def selector_for(type_format):
        type_dict = {
            ReportType.HTML: HtmlFormatter,
            ReportType.TEXT: TextFormatter
        }
        return type_dict.get(type_format, Formatter)()


class ReportExport:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def export(self, report_type):
        formatter = FormatSelector.selector_for(report_type)
        return formatter.format(self.data)

# dinamyc_formatter = FormatSelector.selector_for(ReportType.HTML)
# print(dinamyc_formatter.format('test'))


report = ReportExport('Log: ', 'Test data')
# result = report.export(ReportType.HTML)
result = report.export('Test')
print(result)
