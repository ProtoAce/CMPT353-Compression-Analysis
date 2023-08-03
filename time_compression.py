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

def save_compression(compressed_data, compression_type, out_file):
    if compression_type == 'gzip':
        with open(out_file + ".gz", 'wb') as f_out:
            f_out.write(compressed_data)
        # decompressed_data = gzip.decompress(compressed_data)
        # with open(out_file + ".txt", 'wb') as f_out1:
        #     f_out1.write(decompressed_data)
        
    elif compression_type == 'zlib':
        with open(out_file + ".zlib", 'wb') as f_out:
            f_out.write(compressed_data)

    elif compression_type == 'bz2':
        with open(out_file + ".bz2", 'wb') as f_out:
            f_out.write(compressed_data)
    elif compression_type == 'lzma':
        with open(out_file + ".lzma", 'wb') as f_out:
            f_out.write(compressed_data)
    elif compression_type == 'zipfile':
        with open(out_file + ".zip", 'wb') as f_out:
            f_out.write(compressed_data)
        # with zipfile.ZipFile(out_file + ".zip", 'r') as f:
        #     f.extractall("data/data/compressed_files/")    
    elif compression_type == 'tarfile':
        with open(out_file + ".tar.gz", 'wb') as f_out:
            f_out.write(compressed_data)
        # with tarfile.open(out_file + ".tar.gz", 'r') as f:
        #     f.extractall("data/data/compressed_files/")
    else:
         return   
    return

def get_compression_times():
    
    compression_data = []
    start = time.time()
    for directory in data_directories:
        start_dir = time.time()
        for typer in  os.listdir(directory):
            print("type is: " + typer )
            for folder in os.listdir(directory + "/" + typer):
                for file in os.listdir(directory + "/" + typer + "/" + folder):
                    name = file
                    file_path = directory + "/" + typer + "/" + folder + "/" + file
                    initial_size = os.path.getsize(file_path)
                    print(file_path)
                    with open(file_path, 'rb') as f:
                        file = f.read()
                    
                    for key, fn in compression_functions.items():
                        if key == 'zipfile' or key == 'tarfile':
                            file = file_path
                        total_time, compression_ratio, compressed_data = time_compression(file, initial_size, fn)
                        compression_data.append({'file_size': initial_size, 'compression_ratio': compression_ratio, 'compression_time': total_time, 'compression_type': key, 'single_file': True})
                        out_file = "compressed_files/" + key + "/" + key + '-' + str(name)
                        save_compression(compressed_data,key, out_file)

        end = time.time()
        print("current directory: ", directory, "time:", end - start_dir, "total time:", end - start)

    compression_data = pd.DataFrame(compression_data)
    compression_data.to_csv('compression_times.csv', index=False)


get_compression_times()