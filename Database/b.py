import pandas as pd
df=pd.read_csv('medicines_in_pharmacy.csv')

heads=list(df.columns)
mid=heads.index('medicine_name')+1
pid=heads.index('pharmacy_ID')+1

d={}
for key in heads:
	d[key]=[]
 
pair={}

for post in df.itertuples():
	t=(post[mid],post[pid])
	if pair.get(t,-1)==-1:
		pair[t]=1
		for i in range(len(heads)):
			d[heads[i]].append(post[i+1])
	
dfnew=pd.DataFrame(d)
dfnew.to_csv('medicines_in_pharmacy1.csv')