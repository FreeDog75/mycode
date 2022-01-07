#!/usr/bin/env python3
"""Author: James Freeman, Description: Converts no header comic book listing to a readable format"""

#importing pandas mondule
import pandas as pd

#Establishing new fieldnames for file
header_list= ["Issue", "Number", "Arc", "Distributor", str("ID"), "Contributor"]

#importing file as Pandas dataframe and identifying semicolon seperator
df = pd.read_csv('brett_comics.txt', sep=';', names=header_list)

#get input for search
search = input("Enter the name of contributor to search for (Suggest just the last name): ")

#Search "Contributor" column for input string and ideentify if it exists in an additional index
df["Indexes"]= df["Contributor"].str.contains(search.capitalize())

#Attempted to filter csv but only outputs index numbers where true exists.
#df=df.filter(like="True")

print(df)
