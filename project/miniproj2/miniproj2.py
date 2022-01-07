#!/usr/bin/env python3

import pandas as pd

header_list= ["Issue", "Number", "Arc", "Distributor", str("ID"), "Contributors"]

df = pd.read_csv('brett_comics.txt', sep=';', names=header_list)

print(df)
  
