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
import shutil

def time_decompression(file, decompression_function):
    final_size = 0
    start_time = time.time()
    if decompression_function == cf.zip_decompress or decompression_function == cf.tar_decompress:
        decompression_function()
    else:
        decompressed_data = decompression_function(file)
    end_time = time.time()
    
    total_time = end_time - start_time
    if decompression_function == cf.zip_decompress or decompression_function == cf.tar_decompress:
        final_size = cf.get_directory_size('decompressed_ziptar')
        shutil.rmtree('decompressed_ziptar/data')
    else:
        final_size = len(decompressed_data)
    return total_time , final_size

