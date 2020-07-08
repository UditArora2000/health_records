import pandas as pd
df=pd.read_csv('patient_history.csv')
d={}
heads=list(df.columns)
rid=heads.index('record_ID')+1
pid=heads.index('patient_ID')+1

for post in df.itertuples():
	d[post[rid]]=post[pid]



df=pd.read_csv('medical_test_history.csv')

heads=list(df.columns)
rid=heads.index('record_ID')+1
pid=heads.index('patient_ID')+1
from collections import defaultdict
dic=defaultdict(list)

for post in df.itertuples():
	for i in range(len(heads)):
		dic[heads[i]].append(post[i+1])
	dic['patient_ID'][-1]=d[post[rid]]

dfnew=pd.DataFrame(dic)
dfnew.to_csv('medical_test_history1.csv')