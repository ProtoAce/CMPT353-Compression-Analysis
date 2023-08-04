import pandas as pd

compression_data_NVMe = pd.read_csv(
    'compression_times/compression_times_GCheng_NVMe.csv')
compression_data_HDD = pd.read_csv(
    'compression_times/compression_times_HDD.csv')
compression_data_SSD = pd.read_csv(
    'compression_times/compression_times_GCheng_SSD.csv')

joined_data = pd.concat(
    [compression_data_NVMe, compression_data_HDD, compression_data_SSD])
joined_data.loc[(joined_data['file_type'] != 'json') & (
    joined_data['file_type'] != 'txt') & (joined_data['file_type'] != 'csv'), 'file_type'] = 'file'
joined_data.to_csv('compression_times/compression_times.csv', index=False)
