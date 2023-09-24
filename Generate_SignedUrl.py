import datetime
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from botocore.signers import CloudFrontSigner

def rsa_signer(message):
    # Load your private key from the PEM file
    with open('private_key.pem', 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    # Sign the message using SHA1 and PKCS1v15 padding
    signature = private_key.sign(message, padding.PKCS1v15(), hashes.SHA1())
    return signature

key_id = 'K1LH24W6PYOUAB0X'
url = 'https://d1fwxbaw7sqbnf.cloudfront.net/Samplevideo.mp4'
expire_date = datetime.datetime(2023, 10, 10)

cloudfront_signer = CloudFrontSigner(key_id, rsa_signer)

# Create a signed URL that will be valid until the specific expiry date
# provided using a canned policy.
signed_url = cloudfront_signer.generate_presigned_url(
    url, date_less_than=expire_date)
print(signed_url)
