from urllib.request import urlopen
import pandas as pd
import os

basepath = 'data/c_ruiz'
final_path = "data/fixed/"
asked_name = '213503'


df = pd.read_excel('data/c_ruiz/Retailer.xlsx', index_col=0)  
#print(df["Style Number"].head)
i=0

for row in df["Style Number"].drop_duplicates():
    asked_name = row
#    print(os.listdir(basepath))
    for root, subdirs, files in os.walk(basepath):
        
     #   print("root",root,"fi",files)
        for file in files:
            i+=1
            if str(asked_name) in root:
                os.rename(os.path.join(root, file), os.path.join(final_path, ''.join([str(row),"_",str(i), '.jpg'])))
