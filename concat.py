import glob
import pandas as pd
path =r'C:/Users/tiany/Documents/GitHub/csv' # use your path
allFiles = glob.glob(path + "/*.csv")
print(allFiles)
frame = pd.DataFrame()
dflist = []
for filename in allFiles:
    df = pd.read_csv(filename, encoding='latin-1', dtype='unicode',low_memory=False)
    dflist.append(df)
frame = pd.concat(dflist)

frame.to_csv('C:/Users/tiany/Documents/GitHub/conca.csv')
