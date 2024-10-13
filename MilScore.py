import pandas as pd
import datas
import string_equivalent
import re

Month_Scores = datas.load_scores()
Month_Rates = datas.load_rates()
Month_Scores_re = []
Month_Rates_re = []

#커트라인 데이터의 군사특기 통합
for i in range(len(Month_Scores)):
    Month_Scores[i]['통합 군사특기'] = Month_Scores[i].apply(lambda row: f"{row['군사특기']} {row['군사특기명']} {row['입영부대']}", axis=1)


for Month_score in Month_Scores:
    Month_Scores_re.append(Month_score.loc[:,['통합 군사특기', '총점']])



for Month_Rate in Month_Rates:
    Month_Rates_re.append(Month_Rate.loc[:,['통합 군사특기', '모집(선발)계획인원', '접수인원(1지망)','지원율']])

def Only_Score(job):
    for idx, month in enumerate(Month_Scores_re, start=1):  # idx로 월을 추적
        for a, b in month.iterrows():
            if job in str(b['통합 군사특기']).strip():  # '통합 군사특기'에서 job을 찾음
                print(f'{idx}월: {b}')  # idx는 월, b는 해당 데이터
    return

def Only_Rate(job):
    for idx, month in enumerate(Month_Rates_re, start=1):  # idx로 월을 추적
        for a, b in month.iterrows():
            if job in str(b['통합 군사특기']).strip():  # '통합 군사특기'에서 job을 찾음
                print(f'{idx}월: {b}')  # idx는 월, b는 해당 데이터

merged_data_df = []


    #merged_data_month = pd.concat[Month_score, Month_rate]
    #print(merged_data_month)


# 경쟁률과 커트라인 통합하기
merged_data_df = [] #통합한 프레임들 넣어두는 곳. 월별로.
# 1월달 커트라인을 기준으로 통합 그러면 미달인 곳은 자동으로 제외
month = 0
for Month_score, Month_Rate in zip(Month_Scores_re, Month_Rates_re):
    month = []
    for _, score_job in Month_score.iterrows():
        for _, rate_job in Month_Rate.iterrows():
            if string_equivalent.are_strings_equivalent(score_job['통합 군사특기'], rate_job['통합 군사특기']):
                new_row = {
                    '통합 군사특기': score_job['통합 군사특기'],
                    '커트라인 점수': score_job['총점'],
                    '모집인원': rate_job['모집(선발)계획인원'],
                    '접수인원(1지망)': rate_job['접수인원(1지망)'],
                    '지원율': rate_job['지원율']
                }
                month.append(new_row)
                break
    month_df = pd.DataFrame(month)
merged_data_df.append(month_df)

merged_data_df[0].to_excel('시험용.xlsx')

print(merged_data_df[0])

def job_merge(job):
    merge = []
    for month in merged_data_df:
        for _, i in month.iterrows():
            if job in i['통합 군사특기']:
                print(i)
                break
    return



        
        

