axes1 = ["zy","yz","xx"]


axes2 = ["zx","xz","yy"]


axes3 = ["xy","yx","zz"]

for axes in [axes1,axes2,axes3]:
	print([[f"{k}"for k in i] for i in axes])