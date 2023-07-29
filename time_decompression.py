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

data_directories = ['compressed_data/' + directory for directory in os.listdir('data') if directory != 'zip']
data_subdirectories = [directory + '/' + subdirectory for directory in data_directories for subdirectory in os.listdir(directory)]
print(len(data_subdirectories))

def time_decompression(file, initial_size, de_compression_function):
    start_time = time.time()
    compressed_data = de_compression_function(file)
    end_time = time.time()
    total_time = end_time - start_time
    # final_size = len(compressed_data)
    # compression_ratio = initial_size / final_size
    return total_time #, compression_ratio

compression_functions = {'gzip': cf.gzip_decompress, 'zlib': cf.zlib_decompress, 'bz2': cf.bz2_decompress, 'lzma': cf.lzma_decompress, 'zipfile': cf.zip_decompress, 'tarfile': cf.tar_decompress}


def get_decompression_times():
    decompression_data = []
    start = time.time()
    for directory in data_subdirectories:
        start_dir = time.time()
        decompression_func = None
        if("zlib" in directory):
            decompression_func = cf.zlib_decompress
        elif("gzip" in directory):
            decompression_func = cf.gzip_decompress
        elif("bz2" in directory):
            decompression_func = cf.bz2_decompress
        elif("lzma" in directory):
            decompression_func = cf.lzma_decompress
        elif("zipfile" in directory):
            decompression_func = cf.zip_decompress
        elif("tarfile" in directory):
            decompression_func = cf.tar_decompress
        for file in  os.listdir(directory):
            file_path = directory + "/"+ file
            with open(file_path, 'rb') as f:
                file = f.read()
            if decompression_func == cf.zip_decompress or decompression_func == cf.tar_decompress:
                file = file_path
            total_time= time_decompression(file, decompression_func)
            compression_data.append({'decompression_time': total_time, 'decompression_type': key, 'single_file': True})
        end = time.time()
        print("current directory: ", directory, "time:", end - start_dir, "total time:", end - start)

    compression_data = pd.DataFrame(compression_data)
    compression_data.to_csv('data/compression_times.csv', index=False)


get_decompression_times()