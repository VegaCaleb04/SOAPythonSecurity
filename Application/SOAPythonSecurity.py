from fastapi import FastAPI
from Core.Security.Encode import Base64Encode
from Core.Security.Decode import Base64Decode

app: FastAPI= FastAPI(title='SOAP python Security', description='USBSI 2023')

app.get("/base64encode")
async def base64_encode(plainText: str | None= None):
    base64_encode = Base64Encode()
    return base64_encode.encode(plainText)

app.post("/base64Decode")
async def base64_Decode(plainText: str | None= None):
    base64_Decode = Base64Decode()
    return base64_Decode.decode(plainText)
