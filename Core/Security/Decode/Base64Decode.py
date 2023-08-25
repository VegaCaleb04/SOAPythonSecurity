import base64

class Base64Decode:
     def decode(self, encoded_text):
            decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
            return decoded_bytes.decode('utf-8')
