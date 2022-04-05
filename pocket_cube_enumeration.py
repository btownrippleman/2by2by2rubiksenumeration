import json,copy
import numpy as np
from numpy.lib.function_base import append
import pandas as pd
#ok, so the point of this code is to enumerate all the 3^7 * 8!/ 24, i.e. 3674160 different combinations of a pocket
# cube

# first step:
# visualize the cube 

#each corner will have a number starting with the top back left cube being 1, going clockwise on the top layer
# around to the top front left cube being four and then starting with the bottom back left cube at 
# 5, going around clockwise on the bottom layer to the front bottom left corner at 8
# each corner will then having a color for each cordinate wherein the current orientation gives 
# the top:blue, right:yellow, front:red, back:orange, left:white, bottom: green
# TOP_BACK_LEFT = 1
# TOP_BACK_RIGHT = 2
# TOP_RIGHT_LEFT = 
#color domains
W = "white"
O = "orange"
B = "blue"
Y = "yellow"
G = "green"
R = "red"
W,O,B,Y,G,R = "white","orange","blue","yellow","green","red"
colors = [W,O,B,Y,G,R]
W,O,B,Y,G,R = [i[0].upper() for i in colors]
# TOP CUBES
# 1 -> 2
#      |
#      V
# 4 <- 3
#
# BOTTOM CUBES
# 5 -> 6
#      |
#      V
# 8 <- 7
import copy
initial_config = {1:{"x":W,"y":O,"z":B}, 2:{"x":Y,"y":O,"z":B},
						3:{"x":Y,"y":R,"z":B}, 4:{"x":W,"y":R,"z":B},
						5:{"x":W,"y":O,"z":G}, 6:{"x":Y,"y":O,"z":G},
						7:{"x":Y,"y":R,"z":G}, 8:{"x":W,"y":R,"z":G},
}

initial_color_domains = {"top":B, "right":Y, "front":R, "back":O, "left":W, "bottom":G}


# new_config = {B: ]["top_back_left","top_back_right","top_front_left","top_front_right"],
# 				  R:]["front_top_left","front_top_right","front_bottom_left","front_bottom_right"],
# 				  Y:""}

# new_config = {'blue': ['top_front_left', 'top_front_right', 'top_back_left', 'top_back_right'], 'yellow': ['right_front_top', 'right_front_bottom', 'right_back_top', 'right_back_bottom', 'right_top_front', 'right_top_back', 'right_bottom_front', 'right_bottom_back'], 'red': ['front_top_left', 'front_top_right', 'front_bottom_left', 'front_bottom_right', 'front_left_top', 'front_left_bottom', 'front_right_top', 'front_right_bottom'], 'orange': ['back_top_left', 'back_top_right', 'back_bottom_left', 'back_bottom_right', 'back_left_top', 'back_left_bottom', 'back_right_top', 'back_right_bottom'], 'white': ['left_front_top', 'left_front_bottom', 'left_back_top', 'left_back_bottom', 'left_top_front', 'left_top_back', 'left_bottom_front', 'left_bottom_back'], 'green': ['bottom_front_left', 'bottom_front_right', 'bottom_back_left', 'bottom_back_right']}


initial_string = "lWWWWtBBBBfRRRRrYYYYuGGGGbOOOO"
sidenames = "ltfrub"
l,t,f,r,u,b = [initial_string.find(i) for i in sidenames]
#{0: 'l', 1: 'W', 2: 'W', 3: 'W', 4: 'W', 5: 't', 6: 'B', 7: 'B', 8: 'B', 9: 'B', 10: 'f', 11: 'R', 12: 'R', 13: 'R', 14: 'R', 15: 'r', 16: 'Y', 17: 'Y', 18: 'Y', 19: 'Y', 20: 'u', 21: 'G', 22: 'G', 23: 'G', 24: 'G', 25: 'b', 26: 'O', 27: 'O', 28: 'O', 29: 'O'}

# l - 1,4,8,5 r-2,3,7,6
def rotate_string(config,direction,axis):
	prev = config #copy.deepcopy(config)
	if direction == 1:
		if axis == "x":
			config = config[:t+2] + prev[f+2:f+4]+ config[t+4:]
			config = config[:f+2] + prev[u+2:u+4]+ config[f+4:]
			config = config[:u+2] + prev[b+2:b+4]+ config[u+4:]
			config = config[:b+2] + prev[t+2:t+4]+ config[b+4:]

			# config = config.replace(prev[f+1:f+3],prev[u+1:u+3])
			# config = config.replace(prev[u+1:u+3],prev[b+1:b+3])
			# config = config.replace(prev[b+1:b+3],prev[t+1:t+3])
			# config = config.replace(prev[l+1],prev[l+4])
			# config = config.replace(prev[l+2],prev[l+1])
			# config = config.replace(prev[l+3],prev[l+2])
			# config = config.replace(prev[l+4],prev[l+3])
	return config

# print(rotate_string(initial_string,1,"x"))


def rotate(previous_config, direction, axis):
	new_config = {k:{l:u for l,u in v.items()} for k,v in previous_config.items()}

	if axis == "x": #2,3,7,6
		axes = ["zy","yz","xx"]
		cubes = [2,3,7,6]

	elif axis == "y": #4,8,7,3
		cubes = [4,8,7,3]
		axes = ["zx","xz","yy"]

	elif axis == "z":
		cubes = [1,2,3,4]
		axes = ["xy","yx","zz"]
	for i,v in enumerate( cubes):
		for pair in axes:
			new_config[v][pair[0]] = previous_config[cubes[(i+direction)%4]][pair[1]]
	return new_config

def check_if_all_sides_same_color(config):
	top = config[1]["z"]
	for i in [2,3,4]:
		if config[i]["z"] != top:
			print("top")
			return False
	left = config[1]["x"]
	for i in [4,8,5]:
		if config[i]["x"] != left:
			print("left")
			return False
	back = config[1]["y"]
	for i in [2,6,5]:
		if config[i]["y"] != back:
			print("back")
			return False
	front = config[7]["y"]
	for i in [8,4,3]:
		if config[i]["y"] != front:
			print("front")
			return False
	right = config[7]["x"]
	for i in [6,2,3]:
		if config[i]["x"] != right:
			print("right")
			return False	
	bottom = config[7]["z"]
	for i in [5,6,8]:
		if config[i]["z"] != bottom:
			print("bottom")
			return False
	return True

def rotate_whole_cube_positive_x_axis(config):
	new_config = {k:v for k,v in config.items()}
	for cube_combo in [(1,4),(2,3),(3,7),(4,8),(8,5),(7,6),(5,1),(6,2)]:
		for side_combo in ["yz","zy","xx"]:
			new_config[cube_combo[0]][side_combo[0]]=config[cube_combo[1]][side_combo[1]]
	return new_config

def rotate_whole_cube_positive_y_axis(config):
	new_config = {k:v for k,v in config.items()}
	for cube_combo in [(1,5),(4,8),(2,1),(3,4),(6,2),(7,3),(5,6),(8,7)]:
		for side_combo in ["xz","zx","yy"]:
			new_config[cube_combo[0]][side_combo[0]]=config[cube_combo[1]][side_combo[1]]
	return new_config

def rotate_whole_cube_positive_z_axis(config):
	new_config = {k:v for k,v in config.items()}
	for cube_combo in [(2,1),(3,2),(4,3),(1,4),(6,5),(7,6),(8,7),(5,8)]:
		for side_combo in ["xy","yx","zz"]:
			new_config[cube_combo[0]][side_combo[0]]=config[cube_combo[1]][side_combo[1]]
	return new_config

def rotate_whole_cube_negative_x_axis(config):
	new_config = copy.deepcopy(config)
	for cube_combo in [(4,1),(3,2),(7,3),(8,4),(5,8),(6,7),(1,5),(2,6)]:
		for side_combo in ["yz","zy","xx"]:
			new_config[cube_combo[0]][side_combo[0]]=config[cube_combo[1]][side_combo[1]]
	return new_config

def rotate_whole_cube_negative_y_axis(config):
	new_config = copy.deepcopy(config)
	for cube_combo in [(5,1),(8,4),(1,2),(4,3),(2,6),(3,7),(6,5),(7,8)]:
		for side_combo in ["xz","zx","yy"]:
			new_config[cube_combo[0]][side_combo[0]]=config[cube_combo[1]][side_combo[1]]
	return new_config

def rotate_whole_cube_negative_z_axis(config):
	new_config = copy.deepcopy(config)
	for cube_combo in [(1,2),(2,3),(3,4),(4,1),(5,6),(6,7),(7,8),(8,5)]:
		for side_combo in ["xy","yx","zz"]:
			new_config[cube_combo[0]][side_combo[0]]=config[cube_combo[1]][side_combo[1]]
	return new_config




def get_all_rotations(config):
	configs = []
	configs.append(config)
	configs.append(rotate_whole_cube_negative_z_axis(configs[-1]))
	configs.append(rotate_whole_cube_negative_z_axis(configs[-1]))
	configs.append(rotate_whole_cube_negative_z_axis(configs[-1]))
	configs.append(rotate_whole_cube_negative_x_axis(configs[0]))	
	configs.append(rotate_whole_cube_negative_y_axis(configs[-1]))
	configs.append(rotate_whole_cube_negative_y_axis(configs[-1]))
	configs.append(rotate_whole_cube_negative_y_axis(configs[-1]))
	configs.append(rotate_whole_cube_negative_x_axis(rotate_whole_cube_negative_x_axis(configs[0])))
	configs.append(rotate_whole_cube_negative_z_axis(configs[-1]))
	configs.append(rotate_whole_cube_negative_z_axis(configs[-1]))
	configs.append(rotate_whole_cube_negative_z_axis(configs[-1]))
	configs.append(rotate_whole_cube_positive_x_axis(configs[0]))	
	configs.append(rotate_whole_cube_negative_y_axis(configs[-1]))
	configs.append(rotate_whole_cube_negative_y_axis(configs[-1]))
	configs.append(rotate_whole_cube_negative_y_axis(configs[-1]))
	configs.append(rotate_whole_cube_positive_y_axis(configs[0]))	
	configs.append(rotate_whole_cube_positive_x_axis(configs[-1]))
	configs.append(rotate_whole_cube_positive_x_axis(configs[-1]))
	configs.append(rotate_whole_cube_positive_x_axis(configs[-1]))
	configs.append(rotate_whole_cube_negative_y_axis(configs[0]))	
	configs.append(rotate_whole_cube_positive_x_axis(configs[-1]))
	configs.append(rotate_whole_cube_positive_x_axis(configs[-1]))
	configs.append(rotate_whole_cube_positive_x_axis(configs[-1]))
	return configs


def convert_config_to_string(config):

	s = ""
	for i in range(1,9):
		for axis in "xyz":
			s = s+str(i)+axis.upper()+config[i][axis][0].upper()
	return s
	# l for left, t for top, f for front, r for right, b for back, u for underneath or bottom
	# using lowercase as to not confuse with the uppercase colors 
	#using this shortened version as a shorter, less memory consuming key for a dictionary
	# wherein the keys are the configurations and the values are moves to get such configurations
def convert_config_to_shortened_string(config):
	s = "l"
	for i in [1,4,8,5]:
		s = s+config[i]["x"][0].upper()
	s = s+"t"
	for i in [1,2,3,4]:
		s = s+config[i]["z"][0].upper()
	s = s+"f"
	for i in [4,3,7,8]:
		s = s+config[i]["y"][0].upper()
	s= s+"r"
	for i in [3,2,6,7]:
		s = s+config[i]["x"][0].upper()
	s= s+"b"
	for i in [2,1,5,6]:
		s = s+config[i]["y"][0].upper()
	s= s+"u"
	for i in [5,6,7,8]:
		s = s+config[i]["z"][0].upper()
	return s



def generate_for_one_set_of_configs(configs):
	new_configs = np.ndarray([0]*2000000)
	it = 0
	for config in configs["latest_configs"]:
		for direction in [-1,1]:
			for axis in "xyz":
				c = rotate(config,direction,axis)
				c_hash = "".join([str(i)+"".join([v for k,v in c[i].items()]) for i in c])
				if c_hash not in configs["hashes"]:
					configs["hashes"].add(c_hash)
					new_configs[it] = c
					it+=1

	configs["latest_configs"] = new_configs[:it]

def generate_all_configs(initial_config):
	import time
	last_key = 0
	new_configs = [initial_config]
	initial_hash = "".join([str(i)+"".join([v for k,v in initial_config[i].items()]) for i in initial_config])
	configs = { "latest_configs":[initial_config], "hashes": set(initial_hash) }
	init = time.time()
	while configs["latest_configs"] != []:
		generate_for_one_set_of_configs(configs)
		last_key = last_key +1
		print(last_key,len(configs["latest_configs"]),str(time.time()-init)+ " seconds")
		

	return configs

def generate_for_one_set_of_configs(configs):
	# new_configs = np.array([[[0]*3]*8]*400000,dtype = np.byte)
	# new_configs = []#
	new_configs = configs["zeroes"].copy()
	it = 0
	for config in configs["latest_configs"]:
		for direction in [-1,1]:
			for axis in "xyz":
				c = rotate(config,direction,axis)
				c_hash =   "".join(["".join([str(k) for k in i]) for i in c])
				if c_hash not in configs["hashes"] and len(c_hash) == 24:
					configs["hashes"].add(c_hash)
					new_configs[it] = c
					it+=1
	# configs["latest_configs"]= np.array(new_configs,dtype=np.byte)#[:it]
	configs["latest_configs"]= np.array(new_configs[:it],dtype=np.byte)

# def generate_all_configs(initial_config,rotationLimit):

# 	import time
# 	init = time.time()
# 	last_key = 0
# 	initial_hash = "".join(["".join([str(k) for k in i]) for i in initial_config])
# 	print(initial_hash)
# 	configs = { "latest_configs":[initial_config], "hashes": set(initial_hash) }
# 	# configs["zeroes"] = np.array([[[0]*3]*8]*1400000,dtype = np.byte)
# 	configs["zeroes"] = np.array([np.zeros((8,3),np.byte) for i in range(int(1.4*10**6))],np.byte)
# 	# configs["zeroes"].flags.writeable = False

# 	while configs["latest_configs"] != []:
# 		generate_for_one_set_of_configs(configs)
# 		last_key = last_key +1
# 		print(last_key,len(configs["hashes"], len(configs["latest_configs"]),str(time.time()-init)+ " seconds")
# 		# if last_key == rotationLimit:
# 		# 	return configs

# 	return configs

def generate_configs_recursive(initial_config):
	import time
	hashes = set("".join(["".join([str(k) for k in i]) for i in initial_config]))

	def getNextConfigs(configs,rotations = 0, t = time.time()):
		
		if configs != []:
			new_configs = []
			for config in configs:
				for rotation in [(1, 'x'), (1, 'y'), (1, 'z'), (-1, 'x'), (-1, 'y'), (-1, 'z')]:
					new_config = rotate(config,*rotation)
					hash_ = "".join(["".join([str(k) for k in i]) for i in new_config])
					# if hash_ not in hashes:
					# print(new_config*(hash_ not in hashes))
					newarr = new_config*(hash_ not in hashes)
					if hash_ in hashes:
						print("True")
						print(newarr)

					new_configs.append(newarr)
					hashes.add(hash_)

			print(len(new_configs)," configurations from ", rotations + 1, " rotations calculated in", time.time()-t, " seconds ")
			getNextConfigs(new_configs,rotations + 1)
	getNextConfigs([initial_config])
						


# previous config in this case is a numpy matrix
def rotate(previous_config,direction,axis):
	new_config = previous_config.copy() #
	# new_config = [[k for k in i ] for i in previous_config]
	axis_dict = {"x":{"axes":["zy","yz","xx"],"cubes" : [2,3,7,6]},"y":{"cubes" : [4,8,7,3], "axes" : ["zx","xz","yy"]},"z":{"cubes" :[1,2,3,4],"axes" :["xy","yx","zz"]}}
	axis_dict = {"x":{"axes":[(2,1),(1,2),(0,0)],"cubes" : [1,2,6,5]},"y":{"cubes" : [3,7,6,2], "axes" : [(2,0),(0,2),(1,1)]},"z":{"cubes" :[0,1,2,3],"axes" :[(0,1),(1,0),(2,2)]}}
	cubes = axis_dict[axis]["cubes"]
	axes = axis_dict[axis]["axes"]
	for index,col in enumerate(cubes):
		for axis_ in axes:
			col1 = col
			col2 = cubes[(index+direction)%4]
			new_config[col1][axis_[0]] = previous_config[col2][axis_[1]]
	return new_config

W,O,B,Y,G,R = [i for i in range(6)]

initial_config = {1:{"x":W,"y":O,"z":B}, 2:{"x":Y,"y":O,"z":B},
						3:{"x":Y,"y":R,"z":B}, 4:{"x":W,"y":R,"z":B},
						5:{"x":W,"y":O,"z":G}, 6:{"x":Y,"y":O,"z":G},
						7:{"x":Y,"y":R,"z":G}, 8:{"x":W,"y":R,"z":G},
}

# import numpy as np
initial_config = [[i for i in k.values()] for k in initial_config.values()]
initial_config =np.array(initial_config,dtype=np.byte)
print(rotate(initial_config,*(1,"x")))


generate_configs_recursive(initial_config)
# import pandas as pd
# initial_config = np.array(initial_config)
# initial_config = pd.DataFrame(initial_config)
# # initial_config = np.asarray(initial_config)


# print(initial_config)
# print(rotate(initial_config,1,"x"))


# x = generate_all_configs(initial_config,3)
# print(x["hashes"])
# for i in range(6):
# 	x["hashes"].remove(str(i))
# print(x["hashes"])
# test code 


# rotations = get_all_rotations(initial_config)
# for i in rotations:
# 	print(rotations.count(i),check_if_all_sides_same_color(i))


# print((convert_config_to_string(initial_config)))
# print((convert_config_to_shortened_string(initial_config)))


# for n in range(50):
# 	config = initial_config
# 	for i in [(1,"x"),(1,"y"),(-1,"x"),(-1,"y")]*n:
# 		config = rotate(config,i[0],i[1])
# 	if (config == initial_config):
# 		print(n, True)

# for key in initial_config.keys():
# 	print(key,initial_config[key])

# config = (initial_config)
# config = rotate_whole_cube_negative_x_axis(config)
# config = rotate_whole_cube_positive_z_axis(config)
# config = rotate_whole_cube_positive_y_axis(config)
# config = rotate_whole_cube_negative_z_axis(config)

# config = rotate_whole_cube_negative_z_axis(config)
# config = rotate_whole_cube_positive_y_axis(config)
# config = rotate_whole_cube_positive_z_axis(config)
# config = rotate_whole_cube_positive_x_axis(config)

# config = rotate_whole_cube_negative_x_axis(config)
# config = rotate_whole_cube_negative_x_axis(config)
# config = rotate_whole_cube_negative_y_axis(config)
# config = rotate_whole_cube_negative_y_axis(config)
# config = rotate_whole_cube_negative_z_axis(config)
# config = rotate_whole_cube_negative_z_axis(config)

# config = rotate_whole_cube_negative_x_axis(config)
# config = rotate_whole_cube_negative_x_axis(config)