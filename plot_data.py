import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def plot_compression_times():
    data = pd.read_csv('compression_times.csv')
    x1 = data.loc[(data['compression_type'] == 'zlib'), 'compression_time']
    x1_sqrt = np.sqrt(x1)
    x2 = data.loc[(data['compression_type'] == 'gzip'), 'compression_time']
    x2_sqrt = np.sqrt(x2)
    x3 = data.loc[(data['compression_type'] == 'bz2'), 'compression_time']
    x3_sqrt = np.sqrt(x3)
    x4 = data.loc[(data['compression_type'] == 'lzma'), 'compression_time']
    x4_sqrt = np.sqrt(x4)
    x5 = data.loc[(data['compression_type'] == 'zipfile'), 'compression_time']
    x5_sqrt = np.sqrt(x5)
    x6 = data.loc[(data['compression_type'] == 'tarfile'), 'compression_time']
    x6_sqrt = np.sqrt(x6)
    plt.hist([x1_sqrt, x2_sqrt, x3_sqrt, x4_sqrt, x5_sqrt, x6_sqrt], bins=10)
    plt.hist([x1_sqrt, x2, x3, x4, x5, x6], bins=8)
    plt.show()


def plot_compression_ratio():
    data = pd.read_csv('compression_times.csv')
    x1 = data.loc[(data['compression_type'] == 'zlib'), 'compression_ratio']
    x1_sqrt = np.sqrt(x1)
    x2 = data.loc[(data['compression_type'] == 'gzip'), 'compression_ratio']
    x2_sqrt = np.sqrt(x2)
    x3 = data.loc[(data['compression_type'] == 'bz2'), 'compression_ratio']
    x3_sqrt = np.sqrt(x3)
    x4 = data.loc[(data['compression_type'] == 'lzma'), 'compression_ratio']
    x4_sqrt = np.sqrt(x4)
    x5 = data.loc[(data['compression_type'] == 'zipfile'), 'compression_ratio']
    x5_sqrt = np.sqrt(x5)
    x6 = data.loc[(data['compression_type'] == 'tarfile'), 'compression_ratio']
    x6_sqrt = np.sqrt(x6)
    # plt.hist([x1_sqrt, x2_sqrt, x3_sqrt, x4_sqrt, x5_sqrt, x6_sqrt], bins=20)
    plt.hist([x1, x2, x3, x4, x5, x6], bins=7, label=[
             'zlib', 'gzip', 'bz2', 'lzma', 'zipfile', 'tarfile'])
    plt.legend(loc='upper right')
    plt.xlabel('Compression Ratio')
    plt.ylabel('Frequency')
    plt.title('Compression Ratio of Different Compression Methods')
    plt.savefig('compression_ratio.png')
    plt.show()


def plot_decompression_times():
    data = pd.read_csv('compression_times.csv')
    x1 = data.loc[(data['compression_type'] == 'zlib'), 'decompression_time']
    x1_sqrt = np.sqrt(x1)
    x2 = data.loc[(data['compression_type'] == 'gzip'), 'decompression_time']
    x2_sqrt = np.sqrt(x2)
    x3 = data.loc[(data['compression_type'] == 'bz2'), 'decompression_time']
    x3_sqrt = np.sqrt(x3)
    x4 = data.loc[(data['compression_type'] == 'lzma'), 'decompression_time']
    x4_sqrt = np.sqrt(x4)
    x5 = data.loc[(data['compression_type'] == 'zipfile'),
                  'decompression_time']
    x5_sqrt = np.sqrt(x5)
    x6 = data.loc[(data['compression_type'] == 'tarfile'),
                  'decompression_time']
    x6_sqrt = np.sqrt(x6)
    # plt.hist([x1_sqrt, x2_sqrt, x3_sqrt, x4_sqrt, x5_sqrt, x6_sqrt], bins=20)
    plt.hist([x1, x2, x3, x4, x5, x6], bins=50, label=[
        'zlib', 'gzip', 'bz2', 'lzma', 'zipfile', 'tarfile'])
    plt.legend(loc='upper right')
    plt.xlabel('Decompression Time')
    plt.ylabel('Frequency')
    plt.title('Decompression Time of Different Compression Methods')
    plt.savefig('compression_ratio.png')
    plt.show()


def plot_storage_type():
    data = pd.read_csv('compression_times.csv')
    x1 = data.loc[(data['storage_type'] == 'HDD'),
                  'compression_time'].reset_index(drop=True)
    x2 = data.loc[(data['storage_type'] == 'SSD'),
                  'compression_time'].reset_index(drop=True)
    x3 = data.loc[(data['storage_type'] == 'NVMe'),
                  'compression_time'].reset_index(drop=True)
    # plt.hist([x1_sqrt, x2_sqrt, x3_sqrt, x4_sqrt, x5_sqrt, x6_sqrt], bins=20)
    plt.hist([x1, x2, x3], bins=50, label=['HDD', 'SSD', 'NVMe'])
    plt.legend(loc='upper right')
    plt.xlabel('Compression Time')
    plt.ylabel('Frequency')
    plt.title('Decompression Time of Different Compression Methods')
    plt.savefig('compression_ratio.png')
    plt.show()


# plot_compression_times()
# plot_compression_ratio()
# plot_decompression_times()
plot_storage_type()
