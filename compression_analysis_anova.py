from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd


def compression_time_anova(data):
    x1 = data[data['compression_type'] == 'zlib']['compression_time']
    x2 = data[data['compression_type'] == 'gzip']['compression_time']
    x3 = data[data['compression_type'] == 'bz2']['compression_time']
    x4 = data[data['compression_type'] == 'lzma']['compression_time']
    x5 = data[data['compression_type'] == 'zipfile']['compression_time']
    x6 = data[data['compression_type'] == 'tarfile']['compression_time']

    anova = stats.f_oneway(x1, x2, x3, x4, x5, x6)
    print(anova)
    print(anova.pvalue)
    return anova.pvalue


def compression_time_posthoc(data):
    x1 = data[data['compression_type'] == 'zlib']['compression_time']
    x2 = data[data['compression_type'] == 'gzip']['compression_time']
    x3 = data[data['compression_type'] == 'bz2']['compression_time']
    x4 = data[data['compression_type'] == 'lzma']['compression_time']
    x5 = data[data['compression_type'] == 'zipfile']['compression_time']
    x6 = data[data['compression_type'] == 'tarfile']['compression_time']
    df = pd.DataFrame({'zlib': x1, 'gzip': x2, 'bz2': x3, 'lzma': x4, 'zipfile': x5, 'tarfile': x6})
    x_melt = pd.melt(df)
    posthoc = pairwise_tukeyhsd(x_melt['value'], x_melt['variable'],alpha=0.05)
    print(posthoc)

def compression_ratio_posthoc(data):
    x1 = data[data['compression_type'] == 'zlib']['compression_ratio']
    x2 = data[data['compression_type'] == 'gzip']['compression_ratio']
    x3 = data[data['compression_type'] == 'bz2']['compression_ratio']
    x4 = data[data['compression_type'] == 'lzma']['compression_ratio']
    x5 = data[data['compression_type'] == 'zipfile']['compression_ratio']
    x6 = data[data['compression_type'] == 'tarfile']['compression_ratio']
    df = pd.DataFrame({'zlib': x1, 'gzip': x2, 'bz2': x3, 'lzma': x4, 'zipfile': x5, 'tarfile': x6})
    x_melt = pd.melt(df)
    posthoc = pairwise_tukeyhsd(x_melt['value'], x_melt['variable'],alpha=0.05)
    print(posthoc)


def compression_ratio_anova(data):
    x1 = data[data['compression_type'] == 'zlib']['compression_time']
    x2 = data[data['compression_type'] == 'gzip']['compression_time']
    x3 = data[data['compression_type'] == 'bz2']['compression_time']
    x4 = data[data['compression_type'] == 'lzma']['compression_time']
    x5 = data[data['compression_type'] == 'zipfile']['compression_time']
    x6 = data[data['compression_type'] == 'tarfile']['compression_time']

    anova = stats.f_oneway(x1, x2, x3, x4, x5, x6)
    print(anova)
    print(anova.pvalue)
    return anova.pvalue


def anova_analyis():
    data = pd.read_csv('compression_times.csv')
    compression_time_pvalue = compression_time_anova(data)
    compression_ratio_pvalue = compression_ratio_anova(data)

    if compression_time_pvalue < 0.05:
        compression_time_posthoc(data)

    if compression_ratio_pvalue < 0.05:
        compression_ratio_posthoc(data)


