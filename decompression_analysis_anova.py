from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd


def decompression_time_anova(data):
    x1 = data[data['decompression_type'] == 'zlib']['decompression_time']
    x2 = data[data['decompression_type'] == 'gzip']['decompression_time']
    x3 = data[data['decompression_type'] == 'bz2']['decompression_time']
    x4 = data[data['decompression_type'] == 'lzma']['decompression_time']
    x5 = data[data['decompression_type'] == 'zipfile']['decompression_time']
    x6 = data[data['decompression_type'] == 'tarfile']['decompression_time']

    anova = stats.f_oneway(x1, x2, x3, x4, x5, x6)
    print(anova)
    print(anova.pvalue)
    return anova.pvalue


def decompression_time_posthoc(data):
    x1 = data[data['decompression_type'] == 'zlib']['decompression_time']
    x2 = data[data['decompression_type'] == 'gzip']['decompression_time']
    x3 = data[data['decompression_type'] == 'bz2']['decompression_time']
    x4 = data[data['decompression_type'] == 'lzma']['decompression_time']
    x5 = data[data['decompression_type'] == 'zipfile']['decompression_time']
    x6 = data[data['decompression_type'] == 'tarfile']['decompression_time']
    df = pd.DataFrame({'zlib': x1, 'gzip': x2, 'bz2': x3, 'lzma': x4, 'zipfile': x5, 'tarfile': x6})
    x_melt = pd.melt(df)
    posthoc = pairwise_tukeyhsd(x_melt['value'], x_melt['variable'],alpha=0.05)
    print(posthoc)


def anova_analyis():
    data = pd.read_csv('decompression_times.csv')
    decompression_time_pvalue = decompression_time_anova(data)

    if decompression_time_pvalue < 0.05:
        decompression_time_posthoc(data)
