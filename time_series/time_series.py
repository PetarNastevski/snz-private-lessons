import numpy as np
import scipy.stats as sp


def stats_calculate_all(x, stat_config):
    """Пресметка на статистиките од дадената листа x, врз основа на stat_config
    вредностите.

    :param x: листа на временската серија на податоци
    :type x: list(float)
    :param stat_config: листа со имиња на статистики кои треба да се пресметаат
    :type stat_config: list(str)
    :return: листа со пресметаните статистики според редоследот од stat_config
    :rtype: list
    """
    assert len(set(stat_config).difference(['len', 'min', 'max', 'range', 'mean', 'hmean',
                                            'gmean', 'var', 'std', 'skew', 'kurtosis',
                                            'median', 'mode', 'energy', 'energy_sample', 'snr'])) == 0

    x_array = np.array(x)
    n = len(x)
    if n == 0:
        values = [0 for i in range(len(stat_config))]
        return values, stat_config

    min_value = np.min(x_array)
    if min_value < 1:
        offset = 1 + np.abs(min_value)
    else:
        offset = 0
    max_value = np.max(x_array)

    values = []
    for stat_name in stat_config:
        if stat_name == 'len':
            values.append(n)
        elif stat_name == 'min':
            values.append(min_value)
        elif stat_name == 'max':
            values.append(max_value)
        elif stat_name == 'range':
            range_value = max_value - min_value
            values.append(range_value)
        elif stat_name == 'mean':
            mean_value = np.mean(x_array)
            values.append(mean_value)
        elif stat_name == 'hmean':
            hmean_value = sp.hmean(x_array + offset)
            values.append(hmean_value)
        elif stat_name == 'gmean':
            gmean_value = sp.gmean(x_array + offset)
            values.append(gmean_value)
        elif stat_name == 'var':
            std_value = np.std(x_array)
            var_value = std_value ** 2
            values.append(var_value)
        elif stat_name == 'std':
            std_value = np.std(x_array)
            values.append(std_value)
        elif stat_name == 'skew':
            skew_value = sp.skew(x_array)
            values.append(skew_value)
        elif stat_name == 'kurtosis':
            kurtosis_value = sp.kurtosis(x_array)
            values.append(kurtosis_value)
        elif stat_name == 'median':
            median_value = np.median(x_array)
            values.append(median_value)
        elif stat_name == 'mode':
            mode_value = sp.mode(x_array)[0][0]
            values.append(mode_value)
        elif stat_name == 'energy':
            energy_value = np.sum(x_array ** 2)
            values.append(energy_value)
        elif stat_name == 'energy_sample':
            energy_sample_value = np.sum(x_array ** 2) / n
            values.append(energy_sample_value)
        elif stat_name == 'snr':
            mean_value = np.mean(x_array)
            std_value = np.std(x_array)
            snr_value = 0.0
            if std_value != 0:
                snr_value = mean_value / std_value
            values.append(snr_value)

    return values


def percentiles_all(x, iqr=True, amplitude=True, percentiles_list=[5, 10, 25, 40, 50, 60, 75, 90, 95]):
    """Пресметка на перцентили за дадените податоци

    :param x: листа на временската серија на податоци
    :type x: list(float)
    :param iqr: дали да се пресмета интерквартален ранг.
           Ако е True, percentiles_list мора да ги содржи вредностите 25 и 75
    :type iqr: bool
    :param amplitude: дали да се пресмета амплитуда.
           Ако е True, percentiles_list мора да ги содржи вредностите 1 и 99
    :type amplitude: bool
    :param percentiles_list: листа на перцентили кои е потребно да се пресметаат.
           Листата мора да има барем еден елемент и вредностите да бидат поголеми од
           0 и помали од 100.
    :type percentiles_list: list(int)
    :return: листа со вредности за перцентилите според редоследот од параметарот
             percentiles_list, каде што доколку се бараат iqr и amplitude, тие се
             додаваат на крајот на резултантната листа.
    :rtype: list(float)
    """
    assert len(percentiles_list) > 0 and all([0 < q < 100 for q in percentiles_list])

    if len(x) == 0:
        values = [0 for i in range(len(percentiles_list))]
        return values

    values = list(np.percentile(x, percentiles_list))

    if iqr and 25 in percentiles_list and 75 in percentiles_list:
        q1 = percentiles_list.index(25)
        q3 = percentiles_list.index(75)
        values.append(values[q3] - values[q1])
    if amplitude and 1 in percentiles_list and 99 in percentiles_list:
        q1 = percentiles_list.index(1)
        q3 = percentiles_list.index(99)
        values.append(values[q3] - values[q1])
    return values


def is_valid_example(i, window_size, y):
    """Проверка дали податоците се валидни, односно дали сите
    вредности во движечкиот прозорец имаат иста класа

    :param i: моментален индекс од податочното множество
    :type i: int
    :param window_size: големина на движечкиот прозорец
    :type window_size: int
    :param y: листа со лабели (класи)
    :type y: list
    :return: True или False
    :rtype: bool
    """
    y_val = y[i - window_size]
    for j in range(i - window_size + 1, i):
        if y[j] != y_val:
            return False
    return True


def generate_dataset(x, y, stat_config, w_long=0, w_short=0, shift=5):
    """Генерирање на податочното множество за тренирање со дрво на одлука

    :param x: податоци од временската серија
    :type x: np.array
    :param y: податоци за лабелите (класите)
    :type y: list
    :param stat_config: листа со имиња на статистики кои треба да се пресметаат
    :type stat_config: list(str)
    :param w_long: големина на големиот движечки прозорец
    :type w_long: int
    :param w_short: големина на малиот движечки прозорец
    :type w_short: int
    :param shift: поместување при движењето на лизгачките прозорци
    :type shift: int
    :return: податочно множество, индекси од временската серија кои се влезени во податочното множество
    :rtype: list(list), list(int)
    """
    rows = []
    indices = []
    for i in range(max(w_short, w_long), len(x), shift):
        row = []
        if is_valid_example(i, max(w_short, w_long), y):
            for j in range(x.shape[1]):
                if w_long != 0:
                    x_window_long = x[i - w_long:i, j]
                    all_long = stats_calculate_all(x_window_long, stat_config)
                    row.extend(all_long)
                if w_short != 0:
                    x_window_short = x[i - w_short:i, j]
                    all_short = stats_calculate_all(x_window_short, stat_config)
                    row.extend(all_short)
            indices.append(i - 1)
            row.append(y[i])
            rows.append(row)
        else:
            print('nevaliden podatok')
    return rows, indices