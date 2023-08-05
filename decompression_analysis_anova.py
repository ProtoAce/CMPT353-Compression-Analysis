from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd


def decompression_time_anova(data):
    x1 = data.loc[(data['compression_type'] == 'zlib'), 'decompression_time']
    x2 = data.loc[(data['compression_type'] == 'gzip'), 'decompression_time']
    x3 = data.loc[(data['compression_type'] == 'bz2'), 'decompression_time']
    x4 = data.loc[(data['compression_type'] == 'lzma'), 'decompression_time']
    x5 = data.loc[(data['compression_type'] == 'zipfile'),
                  'decompression_time']
    x6 = data.loc[(data['compression_type'] == 'tarfile'),
                  'decompression_time']

    anova = stats.f_oneway(x1, x2, x3, x4, x5, x6)
    return anova.pvalue


def decompression_time_posthoc(data):
    x1 = data.loc[(data['compression_type'] == 'zlib'),
                  'decompression_time'].reset_index(drop=True)
    x2 = data.loc[(data['compression_type'] == 'gzip'),
                  'decompression_time'].reset_index(drop=True)
    x3 = data.loc[(data['compression_type'] == 'bz2'),
                  'decompression_time'].reset_index(drop=True)
    x4 = data.loc[(data['compression_type'] == 'lzma'),
                  'decompression_time'].reset_index(drop=True)
    x5 = data.loc[(data['compression_type'] == 'zipfile'),
                  'decompression_time'].reset_index(drop=True)
    x6 = data.loc[(data['compression_type'] == 'tarfile'),
                  'decompression_time'].reset_index(drop=True)
    df = pd.DataFrame({'zlib': x1, 'gzip': x2, 'bz2': x3,
                      'lzma': x4, 'zipfile': x5, 'tarfile': x6})
    x_melt = pd.melt(df)
    posthoc = pairwise_tukeyhsd(
        x_melt['value'], x_melt['variable'], alpha=(0.05)/3)
    print(posthoc)
    fig = posthoc.plot_simultaneous()
    fig.show()
    fig.savefig('decompression_speed.png')


def anova_analyis():
    data = pd.read_csv('compression_times.csv')
    decompression_time_pvalue = decompression_time_anova(
        data)
    print('decompression_time_pvalue: ', decompression_time_pvalue)

    if decompression_time_pvalue < (0.05)/3:
        print('decompression_time_posthoc')
        decompression_time_posthoc(data)


def main():
    anova_analyis()


if __name__ == "__main__":
    main()
