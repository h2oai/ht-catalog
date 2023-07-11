"""
Utility script to generate readme and index.html
"""

import os 
import pandas as pd 

def rename_usecases():
	for f in os.listdir("use-cases/"):
		n = f.lower().replace("-" ,"_").replace(" ", "_").strip()
		n = "_".join(n.split("_")[1:])
		os.rename("use-cases/" + f, "use-cases/" + n)

def update_master_readme():
	df = pd.read_csv("use_cases.csv", encoding= 'unicode_escape')

	html = """
| # | Use-Case       | Industry | Prediction Target | Problem Type | Data Type |
|---| -------------- | ------- | ----------------- | ----- | ----- |\n"""

	for i, r in df.iterrows():
		r = dict(r) 
		url = "https://github.com/h2oai/ht-catalog/tree/main/Assets/use-cases/"
		html += f"| {int(r['id'])}. | [{r['use-case']}]({url + r['github_url'].strip()})| {r['industry']} | {r['prediction-target']} | {r['problem-type']} | {r['data-type']} |"
		html += "\n"
	return html

def update_all_usecases_readme():
	df = pd.read_csv("use_cases.csv", encoding= 'unicode_escape').fillna("NA")
	
	for i, r in df.iterrows():
		idd = "646864e3c695f7c721514159bd6c59520dab7438"
		
		## custom fix for pest_classification 
		if r['github_url'] == 'pest_classification':
			idd = "73e76f4b255b46596224efa4da3aedc9320ce970"
		## custom fix for deforestation_segmentation
		elif r['github_url'] == 'deforestation_segmentation':
			idd = "78d74498d8534193d3208f31a38cc0aa936d3f86"

		## url for github
		base = f"https://github.com/h2oai/ht-catalog/blob/{idd}/Assets/use-cases/"
		base_l = "../use-cases/"

		r = dict(r)
		url = base + r['github_url'] + "/"
		url_l = base_l + r['github_url'] + "/"

		## create YAML string
		yaml_string = ""
		try:
			for _ in os.listdir(url_l):
				if _.startswith("log"):
					yaml_file = [a for a in os.listdir(url_l+ _) if a.endswith(".yaml")][0]
					yaml_string = open(url_l +_+"/"+ yaml_file).read()
		except Exception as E:
			pass

		## create individual readme

		if r["original-source"] == 'NA':
			r["original-source"] = "Unknown"

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

{r["dataset-description"]} 

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

### Acknowledgements

Original dataset source is {r["original-source"]}
"""

		## add this to each use-case
		open(url_l + "readme.md", "w").write(readme)

def update_webpage_html():
	visited = []
	url = "https://github.com/h2oai/ht-catalog/tree/main/Assets/use-cases/"
	html = ""
	df = pd.read_csv("use_cases.csv", encoding= 'unicode_escape').fillna("NA")
	for i, r in df.iterrows():
		r = dict(r)

		## Uncomment to create new options in dropdown in HTML
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
	return html

if __name__ == '__main__':
	## paste the readme_table in README.md
	# readme_table = update_master_readme()
	# print (readme_table)
	
	## replace the webpage_cards html in index.html between <! Add Here> and <! End Here>
	# webpage_cards = update_webpage_html()
	# print (webpage_cards)

	## update readme of all usecases
	update_all_usecases_readme()
	


