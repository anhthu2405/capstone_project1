import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Generate a random 256-bit key
def generate_key_AES():
    return os.urandom(32)

def encrypt_file(file_path, key):
    # Read the file contents
    with open(file_path, 'rb') as file:
        data = file.read()

    # Generate a random 128-bit IV (Initialization Vector)
    iv = os.urandom(16)

    # Create an AES cipher object with CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Apply encryption to the data
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))

    # Write the encrypted data and IV to the output file
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(iv)
        encrypted_file.write(encrypted_data)

    return encrypted_file_path

def decrypt_file(file_path, key):
    # Read the encrypted file contents
    with open(file_path, 'rb') as encrypted_file:
        iv = encrypted_file.read(16)
        encrypted_data = encrypted_file.read()

    # Create an AES cipher object with CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Apply decryption to the encrypted data
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    # Write the decrypted data to the output file
    decrypted_file_path = file_path[:-4]  # Remove the '.enc' extension
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    return decrypted_file_path

key = generate_key_AES()
encrypted_file_path = encrypt_file('C:\\Users\\Quang Thinh\\Downloads\\1.txt', key)
decrypt_file(encrypted_file_path, key)