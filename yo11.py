import hashlib
import binascii
import base64

# Constants
ITERATION_CNT = 10
MAX_LENGTH = 256
MAX_HASH_CNT = 1000
HASH_CAPACITY = 2
PBKDF2_ALG = 'pbkdf2_hmac_sha256'

def hash_email(email):
    """
    Hash the email using SHA-256 with multiple iterations.
    Combines SHA-256 hashing, Base64 encoding, and hexadecimal encoding in one function.
    """
    try:
        # Step 1: Initial SHA-256 hashing of the email (lowercased)
        email_lower = email.lower().encode('utf-8')
        message_digest = hashlib.sha256(email_lower).digest()

        # Step 2: Perform additional SHA-256 hash iterations
        current_hash = email_lower
        for _ in range(MAX_HASH_CNT):
            current_hash = hashlib.sha256(current_hash).digest()

        # Step 3: Final combination and hashing
        sha256_email_bytes = hashlib.sha256(email_lower).digest()
        combined_hash = sha256_email_bytes + current_hash
        final_hash_result = hashlib.sha256(combined_hash).digest()

        # Step 4: Return final hash as hexadecimal string
        return binascii.hexlify(final_hash_result).decode('utf-8')

    except Exception as e:
        raise e

# Example usage
email = "example@example.com"
hashed_email = hash_email(email)
print("Hashed email:", hashed_email)
