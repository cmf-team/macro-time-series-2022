from statsmodels.tsa.stattools import adfuller
import statsmodels.api as sm

import pandas as pd

def dickey_fuller_test(series: pd.Series) -> None:
    test = adfuller(series.dropna())
    print(f"Dickey-Fuller test for {series.name}")
    print("------------------------------")
    print('adf:', round(test[0], 3))
    print('p-value:', round(test[1], 3))
    for percent in test[4]:
        print(f"{percent}: {round(test[4][percent], 3)}")
    if test[0] > test[4]['5%']:
        print('Есть единичные корни, ряд не стационарен')
    else:
        print('Единичных корней нет, ряд стационарен')
    print("\n")

def bkxg_filter(series: pd.DataFrame, params: tuple) -> pd.DataFrame:
    return sm.tsa.filters.bkfilter(series, params[0], params[1], params[2])

def hodrick_prescott_filter(series: pd.DataFrame) -> pd.DataFrame:
    cycle, trend = sm.tsa.filters.hpfilter(series)
    return cycle, trend

def crosscorr(datax: pd.DataFrame, datay: pd.DataFrame, lag: int = 0)->float:
    """ Lag-N cross correlation. 
    Parameters
    ----------
    lag : int, default 0
    datax, datay : pandas.Series objects of equal length

    Returns
    ----------
    crosscorr : float
    """
    return datax.corr(datay.shift(lag))