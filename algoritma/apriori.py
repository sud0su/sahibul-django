import pandas as pd
import numpy as np
from apyori import apriori


def calculate_apriori(df, support, confidence):

    data=df.drop(['Tanggal','ID Transaksi'],axis=1)

    records = []
    for i in range(data.shape[0]):
        records.append([str(data.values[i,j]).split(',') for j in range(data.shape[1])])

    trx = [[] for trx in range(len(data))]
    for i in range(len(records)):
        for j in records[i][0]:
            trx[i].append(j)


    association_rules = list(apriori(trx, min_support=float(support/100), min_confidence=float(confidence/100), min_lift=1))
    association_results = association_rules

    pd.set_option('max_colwidth', 1000)
    
    Result = pd.DataFrame(columns=['Rule', 'Support', 'Confidence'])
    rows = []

    for item in association_results:
        pair = item[2]
        for i in pair:
            items = str([x for x in i[0]])
            if i[3] != 1:
                row = {
                    'Rule': str([x for x in i[0]]) + " -> " + str([x for x in i[1]]),
                    'Support': str(round(item[1] * 100, 2)) + '%',
                    'Confidence': str(round(i[2] * 100, 2)) + '%'
                }
                rows.append(row)

    Result = pd.concat([Result, pd.DataFrame(rows)], ignore_index=True)

    return Result