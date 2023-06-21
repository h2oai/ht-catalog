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
		url = "https://github.com/h2oai/ht-catalog/tree/main/assets/use-cases/"
		htm += f"| {int(r['id'])}. | [{r['use-case']}]({url + r['github_url'].strip()})| {r['industry']} | {r['prediction-target']} | {r['problem-type']} | {r['data-type']} |"
		htm += "\n"
	print (htm)

"""
'id', 'use-case', 'industry', 'prediction-target', 'problem-type', 'github_url', 
'data-type', 
'description', 'Business Impact', 
'instance-link', 'dataset', 'dataset-description', 
'source', 'license', 'artifacts-link'
"""

def individual_usecases():
	base = "https://github.com/h2oai/ht-catalog/tree/main/assets/use-cases/"
	base = "../use-cases/"
	

	df = pd.read_csv("use_cases.csv").fillna("NA")
	for i, r in df.head(100).iterrows():
		r = dict(r)
		url = base + r['github_url'].strip()  + "/"

		yaml_string = ""

		try:
			for _ in os.listdir(url):
				if _.startswith("log"):
					yaml_file = [a for a in os.listdir(url+ _) if a.endswith(".yaml")][0]

					yaml_string = open(url +_+"/"+ yaml_file).read()
		except Exception as E:
			print (E)
			pass

		print (yaml_string)
		readme = f"""## Use Case {int(r['id'])}: {r['use-case']}

{r["prediction-target"]}

`Industry: {r['industry']}`
`Industry: {r['problem-type']}`
`Industry: {r['data-type']}`

![]({url}cover.png)
![]({url}cover.jpg)
![]({url}cover.jpeg)
![]({url}cover.webp)
![]({url}cover)

### Business Problem 

{r["description"]}

{r["Business Impact"]}

### Dataset

{r["dataset-description"]}

![train data]({url}train%20data.png)

### Model Training

Objective: {r["prediction-target"]}

Model Configuration (Hydrogen Torch yaml)

```yaml
{yaml_string}
```

![chart]({url}chart.png)


### Prediction

![Predictions]({url}Validation%20Predictions.png)

### License

{r['license']}
"""
		
		print (readme)




		break

individual_usecases()