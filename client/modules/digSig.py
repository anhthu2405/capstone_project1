import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def generate_key_pair():
    # Generate a new RSA key pair
    key = RSA.generate(2048)

    # Export the private key
    private_key = key.export_key()
    with open('private_key.pem', 'wb') as f:
        f.write(private_key)

    # Export the public key
    public_key = key.publickey().export_key()
    with open('public_key.pem', 'wb') as f:
        f.write(public_key)

    print('Key pair generated successfully.')

def create_signature(file_path, private_key_path):
    # Read the file contents
    with open(file_path, 'rb') as file:
        data = file.read()

    # Read the private key
    with open(private_key_path, 'rb') as key_file:
        private_key = RSA.import_key(key_file.read())

    # Compute the SHA-256 hash of the file data
    hash_obj = SHA256.new(data)

    # Create a signature object using the private key and the hash
    signer = pkcs1_15.new(private_key)
    signature = signer.sign(hash_obj)

    # Write the signature to a file
    signature_file_path = file_path + '.sig'
    with open(signature_file_path, 'wb') as signature_file:
        signature_file.write(signature)

    return signature

def verify_signature(file_path, signature_path, public_key_path):
    # Read the file contents
    with open(file_path, 'rb') as file:
        data = file.read()

    # Read the signature
    with open(signature_path, 'rb') as signature_file:
        signature = signature_file.read()

    # Read the public key
    with open(public_key_path, 'rb') as key_file:
        public_key = RSA.import_key(key_file.read())

    # Compute the SHA-256 hash of the file data
    hash_obj = SHA256.new(data)

    # Create a verifier object using the public key and the hash
    verifier = pkcs1_15.new(public_key)

    # Verify the signature
    try:
        verifier.verify(hash_obj, signature)
        return True
    except (ValueError, TypeError):
        return False


# Usage example:
# generate_key_pair()

# print(create_signature('C:\\Users\\Quang Thinh\\Downloads\\1.txt', 'private_key.pem'))

# verify_signature('path/to/your/file.txt', 'path/to/your/file.txt.sig', 'public_key.pem')