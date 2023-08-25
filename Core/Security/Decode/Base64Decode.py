import base64

class Base64Encode:
    def encode(self, plaintext):
        encoded_bytes = base64.b64encode(plaintext.encode('utf-8'))
        return encoded_bytes.decode('utf-8')
