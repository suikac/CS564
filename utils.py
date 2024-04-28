from stegano import lsb

def stegano_encrypt(datatoencrypt, png):
    secret = lsb.hide(png, datatoencrypt)
    secret.save("/tmp/secret.png")
    with open('/tmp/secret.png', 'rb') as f:
        data = f.read()
    return data

def stegano_decrypt(secretFilePath):
    data = lsb.reveal(secretFilePath)
    if isinstance(data, bytes):
        data = data.decode()
    return data
