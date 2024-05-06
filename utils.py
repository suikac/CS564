from stegano import lsb

def stegano_encrypt(datatoencrypt, png):
      # Embed the data 'datatoencrypt' into the image specified by 'png' using LSB steganography
    secret = lsb.hide(png, datatoencrypt)
    # Save the new image with the embedded data to a temporary file
    secret.save("/tmp/secret.png")
    # Open the newly created image file in binary read mode
    with open('/tmp/secret.png', 'rb') as f:
        # Read the contents of the file into 'data'
        data = f.read()
         # Return the binary data of the image
    return data

def stegano_decrypt(secretFilePath):
     # Extract the hidden data from the image file specified by 'secretFilePath' using LSB steganography
    data = lsb.reveal(secretFilePath)
    # Check if the extracted data is of bytes type
    if isinstance(data, bytes):
        # Decode the bytes to a string assuming UTF-8 encoding or default string encoding
        data = data.decode()
         # Return the decoded string or the original data if it wasn't bytes
    return data
