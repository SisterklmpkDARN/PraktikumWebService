Environment: Ubuntu

Installation
sudo easy_install ladon
sudo easy_install suds

Testing
Jalanin webservice: ladon-ctl Hashing nama-file.py -p 8080
mengakses webservice pake curl: curl --data "@request.req" http://localhost:8080/Hashing/jsonwsp --header "Content-Type: text/javascript; charset=utf-8"
perintahnya di jalanin dalam kondisi pwd yang isinya request.req
