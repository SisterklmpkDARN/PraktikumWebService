import hashlib
from ladon.ladonizer import ladonize

class Hashing(object):
    @ladonize(str,str,rtype=str)
    def hashthis(self,method,plaintext):
        if method == 'md5':
            m = hashlib.md5()
        elif method == 'sha1':
            m = hashlib.sha1()
        elif method == 'sha224':
            m = hashlib.sha224()
        else:
            return 'unknown hash type'
        m.update(plaintext)
        return m.hexdigest()
