# coding: utf-8
from urllib.request import urlopen
from xml.etree import ElementTree
 
 
class Budget(object):
 
    def __init__(self, data_url):
        with urlopen(data_url) as response:
            self.tree = ElementTree.parse(response)
 
    def __iter__(self):
        return (Spending(element) for element in self.tree.iterfind(
            './/copa:empreendimento',
            namespaces={'copa': 'http://www.portaltransparencia.gov.br/copa2014'}))
 
 
class Spending(object):
    '''2014 World Cup spending line.'''
 
    def __init__(self, element):
        self.element = element
 
    @property
    def value(self):
        value = self.element.find('./valorTotalPrevisto')
        return 0 if value is None else float(value.text)
 
    @property
    def started(self):
        return self.element.find('./andamento/id').text != '1'
 
 
if __name__ == '__main__':
    import locale
 
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
 
    budget = Budget('http://www.portaltransparencia.gov.br/copa2014/api/rest/empreendimento')
    total_spending = sum(spending.value for spending in budget if spending.started)
 
    print(locale.currency(total_spending, grouping=True))
