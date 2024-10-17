import os
import base64
from cryptography.fernet import Fernet

# Load the encryption key
with open('o.txt', 'r') as key_file:
    b64key = key_file.read()
key = base64.b64decode(key)

cipher_suite = Fernet(key)
chunk_dir = 'chunks/'
output_gz_file = 'reconstructed_file.gz'

def decrypt_and_combine_files(chunk_dir, output_gz_file):
    part_files = sorted([f for f in os.listdir(chunk_dir) if f.find('ope_') == 0])

    with open(output_gz_file, 'wb') as output_f:
        for part_file in part_files:
            part_path = os.path.join(chunk_dir, part_file)
            print(f"Processing {part_path}")
            with open(part_path, 'rb') as f:
                encrypted_chunk = f.read()

                # Decrypt the chunk
                decrypted_chunk = cipher_suite.decrypt(encrypted_chunk)

                # Write the decrypted data to the output file
                output_f.write(decrypted_chunk)

            print(f"Part {part_file} decrypted and written to output.")

decrypt_and_combine_files(chunk_dir, output_gz_file)

print(f"Decrypted and reassembled file saved as {output_gz_file}.")
