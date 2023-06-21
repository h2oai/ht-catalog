import os 
import pandas as pd 

def rename_usecases():
	for f in os.listdir("use-cases/"):
		n = f.lower().replace("-" ,"_").replace(" ", "_").strip()
		n = "_".join(n.split("_")[1:])
		os.rename("use-cases/" + f, "use-cases/" + n)

def master_readme():
	df = pd.read_csv("use_cases.csv")

	htm = """
| # | Use-Case       | Industry | Prediction Target | Problem Type | Data Type |
|---| -------------- | ------- | ----------------- | ----- | ----- |\n"""

	for i, r in df.head(100).iterrows():
		r = dict(r)
		url = "https://github.com/h2oai/ht-catalog/tree/main/Assets/use-cases/"
		htm += f"| {int(r['id'])}. | [{r['use-case']}]({url + r['github_url'].strip()})| {r['industry']} | {r['prediction-target']} | {r['problem-type']} | {r['data-type']} |"
		htm += "\n"
	print (htm)

master_readme()