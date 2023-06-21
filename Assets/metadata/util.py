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


def individual_usecases():
	base = "https://github.com/h2oai/ht-catalog/blob/646864e3c695f7c721514159bd6c59520dab7438/Assets/use-cases/"

	base_l = "../use-cases/"
	

	df = pd.read_csv("use_cases.csv").fillna("NA")
	for i, r in df.head(100).iterrows():
		r = dict(r)
		url = base + r['github_url'].strip()  + "/"

		url_l = base_l + r['github_url'].strip()  + "/"
		yaml_string = ""

		try:
			for _ in os.listdir(url_l):
				if _.startswith("log"):
					yaml_file = [a for a in os.listdir(url_l+ _) if a.endswith(".yaml")][0]

					yaml_string = open(url_l +_+"/"+ yaml_file).read()
		except Exception as E:
			pass

		readme = f"""## Use Case {int(r['id'])}: {r['use-case']}

{r["prediction-target"]}

- `Industry: {r['industry']}`
- `Problem Type: {r['problem-type']}`
- `Data Type: {r['data-type']}`

![]({url}cover.png)
![]({url}cover.jpg)
![]({url}cover.jpeg)
![]({url}cover.webp)
![]({url}cover)

### Business Problem 

{r["description"]}

### Impact

{r["Business Impact"]}

### Dataset

Dataset path: {r["dataset-link"]}

{r["dataset-description"]} Import this link directly in Hydrogen Torch using Amazon S3 ingestion

![train data]({url}train%20data.png)

### Solution

[H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)

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
		# if 'pest_clas' in url_l:
			# print (url_l)
		# 	continue
		open(url_l + "readme.md", "w").write(readme)




		# break

# individual_usecases()


def html_generator():
	visited = []
	url = "https://github.com/h2oai/ht-catalog/tree/main/Assets/use-cases/"
	html = ""
	df = pd.read_csv("use_cases.csv").fillna("NA")
	for i, r in df.head(100).iterrows():
		r = dict(r)

		## Do not remove
		# if r['industry'].replace(" ", "") not in visited:
		# 	visited.append(r['industry'].replace(" ", ""))
		# 	print (f"""<option value="{r['industry'].replace(" ", "")}">{r['industry']}</option>""")
		
		html += f"""<div class="card mb-4 all {r['problem-type'].replace(" ", "")} {r['data-type']} {r['industry']}">
	<font color='#ffc107'><i class="fa-solid fa-2x fa-fire"></i></font>
	<h3 class="card-title">{r['use-case']}</h3>
	<p>{r['prediction-target']}</p>
	<p><span class="badge1">{r['problem-type']}</span> <span class="badge1">{r['industry']}</span> <span class="badge1">{r['data-type']}</span> </p>
	<p class="card-icon"><a target='_blank' href="{url + r['github_url'].strip()}"><i class="fa-solid fa-arrow-right"></i></a></p>
</div>"""

	print (html)	
		



# html_generator()