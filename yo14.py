import gzip
import shutil

# Path to your gzip file and the output decompressed file
gzip_file = 'yourfile.gz'
output_file = 'decompressed_file'

# Open the gzip file and decompress it
with gzip.open(gzip_file, 'rb') as f_in:
    with open(output_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
