import pandas as pd
import xlsxwriter
import numpy as np


def reads(r, v):  # v: class, r: ds ten tu file anh
    m = 0
    w = []      # ds sv vang mat
    df = pd.read_csv(v + 'ATTENDENCE.csv')
    k = df['name'].tolist()         # ds full
    print(k, r)
    h = df['attendence'].tolist()
    if k == r:
        for r in k:
            df['attendence'] = "có mặt"
    else:
        i = 0
        for f in k:
            for t in r:
                if f == t:
                    m = m + 1
            if m == 0:
                df.loc[df['name'] == str(f), 'attendence'] = "vắng mặt"
                w.append(f)
            else:
                df.loc[df['name'] == str(f), 'attendence'] = "có mặt"
                m = 0
            i = i + 1
    df.to_csv(v + "ATTENDENCE.csv", index=False)
    return w
