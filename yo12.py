import os
from cryptography.fernet import Fernet

# Generate or load your encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

input_gz_file = '../560f38ac-b91d-4379-a748-0b048af18652.csv.gz'
chunk_size = 1.3 * (1024 ** 3)  # 1.9 GB in bytes
output_dir = 'output_chunks'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def split_and_encrypt_gz_file(input_gz_file, chunk_size):
    with open(input_gz_file, 'rb') as f:
        part_num = 1
        while True:
            chunk = f.read(int(chunk_size))
            if not chunk:
                break

            # Encrypt the chunk
            encrypted_chunk = cipher_suite.encrypt(chunk)

            # Save the encrypted chunk as a new file
            part_filename = os.path.join(output_dir, f'ope_{part_num}')
            with open(part_filename, 'wb') as part_file:
                part_file.write(encrypted_chunk)

            print(f"Part {part_num} written and encrypted.")
            part_num += 1

# Run the splitting and encryption process
split_and_encrypt_gz_file(input_gz_file, chunk_size)

# Save the encryption key for later decryption
with open('../encryption_key.key', 'wb') as key_file:
    key_file.write(key)

print(f"Encryption key saved to 'encryption_key.key'.")
