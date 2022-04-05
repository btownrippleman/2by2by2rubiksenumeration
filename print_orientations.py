orientations = []
sides = ["top","bottom","left","right","front","back"]

side_dict = {"top":"blue", "right":"yellow", "front":"red", "back":"orange", "left":"white", "bottom":"green"}

for x in ["left","right"]:
	for y in ["front","back"]:
		for z in ["top","bottom"]:
			orientation = x+"_"+y+"_"+z
			if orientation not in orientations:
				orientations.append(orientation)

for x in ["left","right"]:
	for z in ["top","bottom"]:
		for y in ["front","back"]:

			orientation = x+"_"+z+"_"+y
			if orientation not in orientations:
				orientations.append(orientation)
for z in ["top","bottom"]:
	for x in ["left","right"]:
		for y in ["front","back"]:

			orientation = x+"_"+y+"_"+z
			if orientation not in orientations:
				orientations.append(orientation)

for z in ["top","bottom"]:
	for y in ["front","back"]:
		for x in ["left","right"]:

			orientation = z+"_"+y+"_"+x
			if orientation not in orientations:
				orientations.append(orientation)
				
for y in ["front","back"]:
	for z in ["top","bottom"]:
		for x in ["left","right"]:

			orientation = y+"_"+z+"_"+x
			if orientation not in orientations:
				orientations.append(orientation)

for y in ["front","back"]:
	for x in ["left","right"]:
		for z in ["top","bottom"]:

			orientation = y+"_"+x+"_"+z
			if orientation not in orientations:
				orientations.append(orientation)
orientation_dict = {side:[] for side in side_dict.values()}
for orientation in orientations:
	for side,color in side_dict.items():
		if side in orientation.split("_",1):
			orientation_dict[color].append(orientation)

print(orientation_dict)