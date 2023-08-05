from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd


def compression_time_anova(data):
    x1 = data.loc[(data['compression_type'] == 'zlib'), 'compression_time']
    x2 = data.loc[(data['compression_type'] == 'gzip'), 'compression_time']
    x3 = data.loc[(data['compression_type'] == 'bz2'), 'compression_time']
    x4 = data.loc[(data['compression_type'] == 'lzma'), 'compression_time']
    x5 = data.loc[(data['compression_type'] == 'zipfile'), 'compression_time']
    x6 = data.loc[(data['compression_type'] == 'tarfile'), 'compression_time']

    anova = stats.f_oneway(x1, x2, x3, x4, x5, x6)
    return anova.pvalue


def compression_time_posthoc(data):
    x1 = data.loc[(data['compression_type'] == 'zlib'),
                  'compression_time'].reset_index(drop=True)
    x2 = data.loc[(data['compression_type'] == 'gzip'),
                  'compression_time'].reset_index(drop=True)
    x3 = data.loc[(data['compression_type'] == 'bz2'),
                  'compression_time'].reset_index(drop=True)
    x4 = data.loc[(data['compression_type'] == 'lzma'),
                  'compression_time'].reset_index(drop=True)
    x5 = data.loc[(data['compression_type'] == 'zipfile'),
                  'compression_time'].reset_index(drop=True)
    x6 = data.loc[(data['compression_type'] == 'tarfile'),
                  'compression_time'].reset_index(drop=True)
    df = pd.DataFrame({'zlib': x1, 'gzip': x2, 'bz2': x3,
                      'lzma': x4, 'zipfile': x5, 'tarfile': x6})
    x_melt = pd.melt(df)
    posthoc = pairwise_tukeyhsd(
        x_melt['value'], x_melt['variable'], alpha=(0.05)/3)
    print(posthoc)


def compression_ratio_posthoc(data):
    x1 = data.loc[(data['compression_type'] == 'zlib'),
                  'compression_ratio'].reset_index(drop=True)
    x2 = data.loc[(data['compression_type'] == 'gzip'),
                  'compression_ratio'].reset_index(drop=True)
    x3 = data.loc[(data['compression_type'] == 'bz2'),
                  'compression_ratio'].reset_index(drop=True)
    x4 = data.loc[(data['compression_type'] == 'lzma'),
                  'compression_ratio'].reset_index(drop=True)
    x5 = data.loc[(data['compression_type'] == 'zipfile'),
                  'compression_ratio'].reset_index(drop=True)
    x6 = data.loc[(data['compression_type'] == 'tarfile'),
                  'compression_ratio'].reset_index(drop=True)
    df = pd.DataFrame({'zlib': x1, 'gzip': x2, 'bz2': x3,
                      'lzma': x4, 'zipfile': x5, 'tarfile': x6})
    x_melt = pd.melt(df)
    posthoc = pairwise_tukeyhsd(
        x_melt['value'], x_melt['variable'], alpha=(0.05)/3)
    fig = posthoc.plot_simultaneous()
    fig.show()
    fig.savefig('compression_ratio_posthoc.png')
    print(posthoc)


def compression_ratio_anova(data):
    x1 = data.loc[(data['compression_type'] == 'zlib'), 'compression_ratio']
    x2 = data.loc[(data['compression_type'] == 'gzip'), 'compression_ratio']
    x3 = data.loc[(data['compression_type'] == 'bz2'), 'compression_ratio']
    x4 = data.loc[(data['compression_type'] == 'lzma'), 'compression_ratio']
    x5 = data.loc[(data['compression_type'] == 'zipfile'), 'compression_ratio']
    x6 = data.loc[(data['compression_type'] == 'tarfile'), 'compression_ratio']

    anova = stats.f_oneway(x1, x2, x3, x4, x5, x6)
    return anova.pvalue


def anova_analyis():
    data = pd.read_csv('compression_times.csv')
    compression_time_pvalue = compression_time_anova(data)
    print('compression_time_pvalue: ', compression_time_pvalue)
    compression_ratio_pvalue = compression_ratio_anova(data)
    print('compression_ratio_pvalue: ', compression_ratio_pvalue)

    if compression_time_pvalue < (0.05)/3:
        print('compression_time_posthoc')
        compression_time_posthoc(data)

    if compression_ratio_pvalue < (0.05)/3:
        print('compression_ratio_posthoc')
        compression_ratio_posthoc(data)


def main():
    anova_analyis()


if __name__ == "__main__":
    main()
