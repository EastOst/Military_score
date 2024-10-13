import pandas as pd
import re

def load_scores():
    JAN_2024 = pd.read_excel('2024JAN.xlsx')
    FEB_2024 = pd.read_excel('2024FEB.xlsx',skiprows=1)
    MAR_2024 = pd.read_excel('2024MAR.xlsx',skiprows=1)
    APR_2024 = pd.read_excel('2024APR.xlsx',skiprows=1)
    MAY_2024 = pd.read_excel('2024MAY.xlsx',skiprows=1)
    JUN_2024 = pd.read_excel('2024JUN.xlsx',skiprows=1)
    JUL_2024 = pd.read_excel('2024JUL.xlsx',skiprows=1)
    AUG_2024 = pd.read_excel('2024AUG.xlsx',skiprows=1)
    SEP_2024 = pd.read_excel('2024SEP.xlsx',skiprows=1)
    OCT_2024 = pd.read_excel('2024OCT.xlsx',skiprows=1)
    NOV_2024 = pd.read_excel('2024NOV.xlsx',skiprows=1)
    DEC_2024 = pd.read_excel('2024DEC.xlsx',skiprows=1)

    MonthScore = [JAN_2024, FEB_2024, MAR_2024, APR_2024, MAY_2024, JUN_2024, JUL_2024, AUG_2024, SEP_2024, OCT_2024, NOV_2024, DEC_2024]
    return MonthScore
def load_rates():
    JAN_2024_Rate = pd.read_excel('2024JAN_Rate.xlsx')
    FEB_2024_Rate = pd.read_excel('2024FEB_Rate.xlsx')
    MAR_2024_Rate = pd.read_excel('2024MAR_Rate.xlsx')
    APR_2024_Rate = pd.read_excel('2024APR_Rate.xlsx')
    MAY_2024_Rate = pd.read_excel('2024MAY_Rate.xlsx')
    JUN_2024_Rate = pd.read_excel('2024JUN_Rate.xlsx')
    JUL_2024_Rate = pd.read_excel('2024JUL_Rate.xlsx')
    AUG_2024_Rate = pd.read_excel('2024AUG_Rate.xlsx')
    SEP_2024_Rate = pd.read_excel('2024SEP_Rate.xlsx')
    OCT_2024_Rate = pd.read_excel('2024OCT_Rate.xlsx')
    NOV_2024_Rate = pd.read_excel('2024NOV_Rate.xlsx')
    DEC_2024_Rate = pd.read_excel('2024DEC_Rate.xlsx')


    MonthRate = [JAN_2024_Rate, FEB_2024_Rate, MAR_2024_Rate, APR_2024_Rate, MAY_2024_Rate, JUN_2024_Rate, JUL_2024_Rate, AUG_2024_Rate, SEP_2024_Rate,
    OCT_2024_Rate, NOV_2024_Rate, DEC_2024_Rate]
    for idx in range(len(MonthRate)):
        MonthRate[idx].columns = MonthRate[idx].columns.str.replace('모집계열', '통합 군사특기')


    return MonthRate

