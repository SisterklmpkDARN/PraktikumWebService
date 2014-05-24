import xml.etree.ElementTree as ET
from suds.client import Client

url = 'http://www.webservicex.net/CurrencyConvertor.asmx?WSDL'
client = Client(url)
result = client.service.ConversionRate('USD','IDR')
print '1$ USD = Rp.',result
