import pandas as pd
from datetime import *
import random
df=pd.read_csv('patient_history.csv')

heads=list(df.columns)
tid=heads.index('disease_detected_date')+1
d={}
for key in heads:
	d[key]=[]
d['treatment_end_date']=[]

for post in df.itertuples():
	for i in range(len(heads)):
		d[heads[i]].append(post[i+1])
	tdate=datetime.strptime(post[tid],"%d-%m-%Y").date()
	delta=timedelta(days=random.randint(10,100))
	d['treatment_end_date'].append((tdate+delta).strftime("%Y-%m-%d"))

dfnew=pd.DataFrame(d)
dfnew.to_csv('patient_history1.csv')