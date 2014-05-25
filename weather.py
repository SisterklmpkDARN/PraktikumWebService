import xml.etree.ElementTree as ET
from suds.client import Client

url = 'http://www.webservicex.net/globalweather.asmx?WSDL'
client = Client(url)
result = client.service.GetWeather('Jakarta','Indonesia')
weather = result.encode('utf16')
parseWeather = ET.fromstring(weather)
tree = ET.ElementTree(parseWeather)
data = tree.getroot()
print '--------------------------------------------------------------------'
print 'Location      : ', data.find('Location').text
print 'Time          : ', data.find('Time').text
print 'Wind          : ', data.find('Wind').text
print 'Visibility    : ', data.find('Visibility').text
print 'Sky Condition : ', data.find('SkyConditions').text
print 'Temperature   : ', data.find('Temperature').text
print 'Dew point     : ', data.find('DewPoint').text
print 'Relative Humidity : ', data.find('RelativeHumidity').text
print 'Pressure      : ', data.find('Pressure').text
print '==================================================================='
