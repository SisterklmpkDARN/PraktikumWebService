import xml.etree.ElementTree as ET
from suds.client import Client

url = 'http://www.webservicex.net/stockquote.asmx?WSDL'
client = Client(url)
result = client.service.GetQuote('TLK')
tree = ET.ElementTree(ET.fromstring(result))
data = tree.getroot().find('Stock')
print data.find('Name').text, data.find('Date').text, '-', data.find('Time').text
print data.find('Last').text, data.find('Change').text, '(', data.find('PercentageChange').text, ')'
print '\nPrevious Close: ', data.find('PreviousClose').text, '\nOpen: ', data.find('Open').text, '\nHigh: ', data.find('High').text, '\nLow: ', data.find('Low').text
print 'Volume: ', data.find('Volume').text, '\nMkt Cap: ', data.find('MktCap').text
