from fastapi import FastAPI
import Core.Security.Encode.Base64Encode
import Core.Security.Decode.Base64Decode

app: FastAPI= FastAPI(title='SOAP python Security', description='USBSI 2023')

app.get("/base64encode")
async def base64_encode(plainText: str | None= None):
    base64_encode = base64_encode()
    return base64_encode.encode(plainText)

app.post("/base64Decode")
async def base64_Decode(plainText: str | None= None):
    base64_Decode = base64_Decode()
    return base64_Decode.decode(plainText)
