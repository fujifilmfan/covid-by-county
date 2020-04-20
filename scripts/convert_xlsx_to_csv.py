#!/usr/bin/env python

import pandas as pd

data_xls = pd.read_excel('../reference_files/all-geocodes-v2018.xlsx')
data_xls.to_csv('../reference_files/all-geocodes-v2018.csv',
                index=False,
                encoding='utf-8')
