import hashlib
import hmac
import binascii
from hashlib import pbkdf2_hmac

def generate_pbkdf2_hash(email: str, iterations: int = 10) -> str:
    # Convert the email to lowercase
    email_lower = email.lower()

    # Calculate the salt by taking the SHA-256 of the lowercase email
    salt = hashlib.sha256(email_lower.encode('utf-8')).digest()

    # Use the lowercase email as the password
    password = email_lower.encode('utf-8')

    # Generate the PBKDF2 hash
    hash_value = pbkdf2_hmac('sha256', password, salt, iterations)

    # Convert the hash to a hexadecimal string
    hash_hex = binascii.hexlify(hash_value).decode('utf-8').upper()

    return hash_hex

# Example usage
email = "Example@Email.com"
hash_output = generate_pbkdf2_hash(email)
print(f"PBKDF2 Hash: {hash_output}")
