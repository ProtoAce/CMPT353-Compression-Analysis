from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd


def storage_type_anova(data):
    x1 = data.loc[(data['storage_type'] == 'HDD'), 'compression_time']
    x2 = data.loc[(data['storage_type'] == 'SSD'), 'compression_time']
    x3 = data.loc[(data['storage_type'] == 'NVMe'), 'compression_time']

    anova = stats.f_oneway(x1, x2, x3)
    return anova.pvalue


def storage_type_posthoc(data):
    x1 = data.loc[(data['storage_type'] == 'HDD'),
                  'compression_time'].reset_index(drop=True)
    x2 = data.loc[(data['storage_type'] == 'SSD'),
                  'compression_time'].reset_index(drop=True)
    x3 = data.loc[(data['storage_type'] == 'NVMe'),
                  'compression_time'].reset_index(drop=True)
    df = pd.DataFrame({'HDD': x1, 'SSD': x2, 'NVMe': x3})
    x_melt = pd.melt(df)
    posthoc = pairwise_tukeyhsd(
        x_melt['value'], x_melt['variable'], alpha=(0.05)/3)
    print(posthoc)
    fig = posthoc.plot_simultaneous()
    fig.show()
    fig.savefig('storage_type_compression_time.png')


def anova_analyis():
    data = pd.read_csv('compression_times.csv')
    compression_time_p_value = storage_type_anova(
        data)
    print('decompression_time_pvalue: ', compression_time_p_value)

    if compression_time_p_value < (0.05)/3:
        print('decompression_time_posthoc')
        storage_type_posthoc(data)


def main():
    anova_analyis()


if __name__ == "__main__":
    main()
