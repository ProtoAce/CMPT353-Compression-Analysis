import time
import os
import zlib
import gzip
import bz2
import lzma
import zipfile
import tarfile
import pandas as pd
import numpy as np
import compression_functions as cf
import time_decompression as td

data_directories = ['data/' + directory for directory in os.listdir('data') if directory != 'zip']
data_subdirectories = [directory + '/' + subdirectory for directory in data_directories for subdirectory in os.listdir(directory)]
print(len(data_subdirectories))

def time_compression(file, initial_size, compression_function):
    start_time = time.time()
    compressed_data = compression_function(file)
    end_time = time.time()
    total_time = end_time - start_time
    final_size = len(compressed_data)
    compression_ratio = initial_size / final_size
    return total_time, compression_ratio, compressed_data

compression_functions = {'gzip': cf.gzip_compress, 'zlib': cf.zlib_compress, 'bz2': cf.bz2_compress, 'lzma': cf.lzma_compress, 'zipfile': cf.zip_compress, 'tarfile': cf.tar_compress}
decompression_functions = {'gzip': cf.gzip_decompress, 'zlib': cf.zlib_decompress, 'bz2': cf.bz2_decompress, 'lzma': cf.lzma_decompress, 'zipfile': cf.zip_decompress, 'tarfile': cf.tar_decompress}

def get_compression_times():
    compression_data = []
    start = time.time()
    for directory in data_subdirectories:
        start_dir = time.time()
        for file in  os.listdir(directory):
            file_path = directory + "/"+ file
            initial_size = os.path.getsize(file_path)
            with open(file_path, 'rb') as f:
                file = f.read()
            
            for key, fn in compression_functions.items():
                if key == 'zipfile' or key == 'tarfile':
                    file = file_path
                total_time, compression_ratio, compressed_data = time_compression(file, initial_size, fn)
                total_time_decomp, final_size_decomp = td.time_decompression(compressed_data, decompression_functions[key])
                compression_data.append({'file_size': initial_size, 'compression_ratio': compression_ratio,
                                                    'compression_time': total_time, 'compression_type': key, 
                                                    'decompression_time': total_time_decomp, 
                                                    'decompression_size': final_size_decomp})
                
        end = time.time()
        print("current directory: ", directory, "time:", end - start_dir, "total time:", end - start)

    compression_data = pd.DataFrame(compression_data)
    compression_data.to_csv('data/compression_times.csv', index=False)


get_compression_times()