import xml.etree.ElementTree as ET
from suds.client import Client

def getStockQuote():
    url = 'http://www.webservicex.net/stockquote.asmx?WSDL'
    client = Client(url)
    result = client.service.GetQuote('TLK')
    tree = ET.ElementTree(ET.fromstring(result))
    data = tree.getroot().find('Stock')
    print '\n--------------------------------------------------------------------'
    print data.find('Name').text, data.find('Date').text, '-', data.find('Time').text
    print data.find('Last').text, data.find('Change').text, '(', data.find('PercentageChange').text, ')'
    print '\nPrevious Close  : ', data.find('PreviousClose').text, '\nOpen            : ', data.find('Open').text, '\nHigh            : ', data.find('High').text, '\nLow             : ', data.find('Low').text
    print 'Volume          : ', data.find('Volume').text, '\nMkt Cap         : ', data.find('MktCap').text
    print '===================================================================\n'

def getConversionRate():
    url = 'http://www.webservicex.net/CurrencyConvertor.asmx?WSDL'
    client = Client(url)
    result = client.service.ConversionRate('USD','IDR')
    print '\n--------------------------------------------------------------------'
    print '1$ USD = Rp', result
    print '===================================================================\n'


def getCurrentWeather():
    url = 'http://www.webservicex.net/globalweather.asmx?WSDL'
    client = Client(url)
    result = client.service.GetWeather('Jakarta','Indonesia')
    weather = result.encode('utf16')
    parseWeather = ET.fromstring(weather)
    tree = ET.ElementTree(parseWeather)
    data = tree.getroot()
    print '\n--------------------------------------------------------------------'
    print 'Location          : ', data.find('Location').text
    print 'Time              : ', data.find('Time').text
    print 'Wind              : ', data.find('Wind').text
    print 'Visibility        : ', data.find('Visibility').text
    print 'Sky Condition     : ', data.find('SkyConditions').text
    print 'Temperature       : ', data.find('Temperature').text
    print 'Dew point         : ', data.find('DewPoint').text
    print 'Relative Humidity : ', data.find('RelativeHumidity').text
    print 'Pressure          : ', data.find('Pressure').text
    print '===================================================================\n'

print '1. Mendapatkan harga saham PT. Telkom Indonesia di NYSE'
print '2. Mendapatkan informasi harga konversi USD ke IDR'
print '3. Mendapatkan informasi cuaca kota Jakarta, Indonesia'
print '4. Mengakhiri program'

opt = int(raw_input('Masukkan pilihan: '))
while opt != 4:
    if opt == 1:
        getStockQuote()
    elif opt == 2:
        getConversionRate()
    elif opt == 3:
        getCurrentWeather()
    opt = int(raw_input('Masukkan pilihan: '))
