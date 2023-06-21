import os 
import pandas as pd 

def rename_usecases():
	for f in os.listdir("use-cases/"):
		n = f.lower().replace("-" ,"_").replace(" ", "_").strip()
		n = "_".join(n.split("_")[1:])
		os.rename("use-cases/" + f, "use-cases/" + n)

df = pd.read_csv("use_cases.csv")

for i, r in df.head(100).iterrows():
	r = dict(r)

	print (f"| {int(r['id'])}. | [{r['use-case']}](#)| {r['industry']} | {r['prediction-target']} | {r['problem-type']} | {r['data-type']} |")

