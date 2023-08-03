import zlib
import gzip
import bz2
import lzma
import zipfile
import tarfile


# Compress data using zlib
def zlib_compress(data):
    compressed_data = zlib.compress(data)
    return compressed_data

# Decompress data using zlib
def zlib_decompress(data): 
    decompressed_data = zlib.decompress(data)
    return decompressed_data

# Compress data using gzip
def gzip_compress(data):
    compressed_data = gzip.compress(data)
    return compressed_data

# Decompress data using gzip
def gzip_decompress(data):
    decompressed_data = gzip.decompress(data)
    return decompressed_data

# Compress data using bz2
def bz2_compress(data):
    compressed_data = bz2.compress(data)
    return compressed_data

# Decompress data using bz2
def bz2_decompress(data):
    decompressed_data = bz2.decompress(data)
    return decompressed_data

# Compress data using lzma
def lzma_compress(data):
    compressed_data = lzma.compress(data)
    return compressed_data

# Decompress data using lzma
def lzma_decompress(data):
    decompressed_data = lzma.decompress(data)
    return decompressed_data

# Compress data using zipfile
def zip_compress(data_path):
    with zipfile.ZipFile('data.zip', 'w', zipfile.ZIP_DEFLATED) as compressed_data:
        compressed_data.write(data_path)
    with zipfile.ZipFile('compressed.zip', 'a', zipfile.ZIP_DEFLATED) as compressed_data:
        compressed_data.write(data_path)
    with open('data.zip', 'rb') as compressed_data:
        compressed_data = compressed_data.read()
    return compressed_data
# Decompress data using zipfile
def zip_decompress(data):
    decompressed_data = zipfile.decompress(data)
    return decompressed_data

# Compress data using tarfile
def tar_compress(data_path):
    with tarfile.open('data.tar.gz', 'w:gz') as compressed_data:
        compressed_data.add(data_path)
    with open('data.tar.gz', 'rb') as compressed_data:
        compressed_data = compressed_data.read()
    return compressed_data

# Decompress data using tarfile
def tar_decompress(data):
    decompressed_data = tarfile.decompress(data)
    return decompressed_data



