from urllib.request import urlopen
import pandas as pd

df = pd.read_excel('JOOR to NuORDER Sample Data and Field Descriptions Revised.xlsx', index_col=0)  
raw_df=df.iloc[[0]]
print(raw_df)

df2 = pd.read_excel('joor_linesheets (1).xlsx', index_col=0)  


frames=[df,df2]
df3= pd.concat(frames)

print(df3.columns)

# Find the columns where each value is null
empty_cols = [col for col in df3.columns if df3.iloc[[0]][col].isnull().any()]
# Drop these columns from the dataframe
df3.drop(empty_cols,
        axis=1,
        inplace=True)
print(df3["Sizes"])

for i in range(len(df3)) : 
    parsed_sizes = df3.iloc[i]["Sizes"].split(',')
    for size in parsed_sizes: 
        size_column = 'Size ' + str(parsed_sizes.index(size)+1) 
        if size_column not in df3:
            df3[size_column] = size



df3.to_csv('out.csv',index=False)
df3.to_excel("output.xlsx")
#https://realpython.com/python-web-scraping-practical-introduction/
#https://support.zendesk.com/hc/en-us/community/posts/360029389614-Extracting-chats-details-with-API-measuring-C-sat-request-rate
