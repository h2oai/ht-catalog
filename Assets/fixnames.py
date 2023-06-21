import os 

for f in os.listdir("use-cases/"):
	n = f.lower().replace("-" ,"_").replace(" ", "_").strip()
	n = "_".join(n.split("_")[1:])

	# printf)
	os.rename("use-cases/" + f, "use-cases/" + n)
