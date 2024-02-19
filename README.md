# Permutation Encryption Scheme

A basic encryption scheme is implemented using permutation. This scheme involves encrypting and decrypting messages using a shared key.
The key consists of a permutation of byte values (0-255). Let's go through the details and implementation.

## How Permutation Encryption Works

In permutation encryption, messages are encrypted by rearranging the bytes that represent the message according to a predefined permutation key.
For example, if the key is `(251, 24, 31, ..., 186)`, it represents a mapping where each byte value (0-255) is mapped to a new position according to the given permutation.

### Encryption Process
1. Given a plaintext message, each byte is replaced with its corresponding byte in the permutation key.
2. The resulting sequence is the ciphertext.

### Decryption Process
1. To decrypt the ciphertext, the inverse of the permutation mapping is applied.
2. This mapping is easily computed using the same key used for encryption.

## Implementation Details

The Python file `encryption.py` contains the following functions:

- `read_file(file_name)`: Reads a file in binary mode and returns its content as a list of bytes.
- `write_file(file_name, content)`: Writes a bytearray into a file in binary mode.
- `encrypt(plain_text, key)`: Accepts plaintext and a key, returning the encrypted ciphertext.
- `decrypt(cipher_text, key)`: Accepts ciphertext and a key, returning the decrypted plaintext.

## Testing

To test the encryption and decryption functions, run the `test_encryption()` function. This function performs the following steps:

1. Reads the key from a file named "key".
2. Encrypts the content of a file named "plain_text".
3. Writes the ciphertext to a file called "cipher_text".
4. Decrypts the ciphertext from "cipher_text".
5. Writes the decrypted plaintext to a file named "plain_text1".

If the files "plain_text1" and "plain_text" are identical, the encryption and decryption algorithms are working correctly.

## File Structure

- `key`: Contains the permutation key used for encryption and decryption.
- `plain_text`: Contains the plaintext data to be encrypted.
- `cipher_text`: Contains the encrypted data.
- `plain_text1`: Contains the decrypted data.

