def read_file(file_name):
    """Reads a file and returns its content

    :param file_name: Name of the file to be opened
    :return: Bytearray of file content
    """
    with open(file_name, 'rb') as f:    # open the file in read/binary mode
        data = f.read()                 # read content
    f.close()                           # close file
    return data                         # return content

def write_file(file_name, content):
    """Writes a bytearray into a file

    :param file_name: Name of the file to be written
    :param content: Content to be written to file
    """
    with open(file_name, 'wb') as f:    # open the file in write/binary mode
        f.write(content)                # write content
    f.close()                           # close file
    return

def encrypt(content, key):
    """Encryptes a bytearray with a given key using permutation scheme

    :param content: Bytearray to be encrypted
    :param key: Bytearray of permutation key
    :return: Encrypted bytearray
    """
    result = bytearray(b'')             # create an empty bytearray
    for byte in content:                # iterate through content bytes
        result.append(key[byte])        # add the encrypted byte to the result
    return result                       # return encrypted result

def decrypt(content, key):
    """Decrypts a bytearray with a given key using permutation scheme

    :param content: Encrypted bytearray to be decrypted
    :param key: Bytearray of permutation key
    :return: Decrypted bytearray
    """
    result = bytearray(b'')             # create an empty bytearray
    for byte in content:                # iterate through encrypted bytes 
        pos = key.find(byte)            # fine the position of byte in key
        result.append(pos)              # append using the position as value byte
    return result                       # return decrypted result

key = read_file('key')                  # read key from file 'key'
plaintext = read_file('plain_text')     # read plaintext content from file 'plain_text'
ciphertext = encrypt(plaintext, key)    # encrypt plaintext
write_file('cipher_text', ciphertext)   # write encrypted content to file 'cipher_text'
ciphertext = read_file('cipher_text')   # read encrypted content from file 'cipher_text'
plaintext = decrypt(ciphertext, key)    # decrypt the encrypted content
write_file('plain_text1', plaintext)    # write plaintext to file 'plain_text1'
