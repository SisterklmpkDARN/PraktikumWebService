from suds.client import Client

client = Client('http://localhost:8080/Hashing/soap/description')
plaintext = str(raw_input('Masukkan plaintext: '))
print 'Metode hash yang dapat digunakan'
print '1. md5'
print '2. sha1'
print '3. sha224'

sel = int(raw_input('Masukkan pilihan: '))
if sel == 1:
	result = client.service.hashthis('md5',plaintext)
elif sel == 2:
	result = client.service.hashthis('sha1',plaintext)
elif sel == 3:
	result = client.service.hashthis('sha224',plaintext)
else:
	print 'Input tidak valid'

print 'Hash:', result