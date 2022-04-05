import java.util.*;

public class PocketCubeEnumeration{
	HashMap<String, Object> configs;
	public PocketCubeEnumeration(){
		Cube c = new Cube();
		Cube n = c.rotate("x",1);
		configs = new HashMap<String, Object>();
		HashMap<String, Cube> latest_configs = new HashMap<String, Cube>();
		latest_configs.put(c.generateHash(), new Cube());
		latest_configs.put(n.generateHash(),n);
		HashSet<String> existingHashes = new HashSet<String>();
		existingHashes.add(c.generateHash());

		configs.put("existingHashes", existingHashes);
		configs.put("latestConfigs",latest_configs);
		System.out.println((HashMap<String, Cube>)configs.get("latestConfigs"));//.get(c.generateHash()));

	}

	// public void enumerateAllconfigs(int rotationLimit){


	// 	ArrayList<Cube> newConfigs = new ArrayList<Cube>();
	// 	newConfigs.add(new Cube());		


	// 	int rotations = 0;
	// 	while(newConfigs.size()!=0 && rotations < rotationLimit){
	// 		System.out.println("rotations :"+rotations+" configurations: "+newConfigs.size()+" hashes: "+this.existingHashes.size());
	// 		newConfigs = generateNewConfigs(newConfigs);
	// 	    rotations = rotations +1;
	// 	}
	// }

	
	public static void main(String[] args){
		PocketCubeEnumeration p = new PocketCubeEnumeration();

		// ArrayList<Cube> initialList = new ArrayList<Cube>();
		// initialList.add(new Cube());
		// HashSet<String> initialHashes = new HashSet<String>();
		// initialHashes.add(new Cube().generateHash());
		// p.generateNewConfigs(initialList,0 );
		// String printOut = "";
		// for (String h: p.existingHashes){
		// 	printOut = printOut +"\', \'"+(h);
		// }
		// System.out.println(printOut);

	}


	public void enumerateAllconfigs(){
		int last_key = 0;
		Cube c = new Cube();
		String initialHash = c.generateHash();
		ArrayList<Cube> new_configs = new ArrayList<Cube>();
		new_configs.add(c);
		HashMap<String, Object> configs = new HashMap<String, Object>();
		HashMap<String, Cube> latest_configs = new HashMap<String, Cube>();
		latest_configs.put(initialHash,c);
		HashSet<String> hashes = new HashSet<String>();
		HashSet<String> latestHashes = new HashSet<String>();

		existingHashes.add(initialHash);
		configs.put("hashes",latestHashes);configs.put("latest_configs",new_configs);
	// 	while (configs.get("latest_configs").size()!=0){
	// 		generateNewConfigs(configs);
	// 		last_key = last_key+1;
	// 		System.out.println(last_key+", "+configs.get("latest_configs").size()+", time yet to be placed");

	// 	}
	// }
	}

	public void generate_for_one_set_of_configs(HashMap<String,Object> configs){
			// Getting a Set of Key-value pairs
			// Set entrySet = configs["latest_configs"].entrySet();
		
			// // Obtaining an iterator for the entry set
			// Iterator it = entrySet.iterator();

			System.out.println(configs["latest_configs"].get(new Cube().generateHash()));

			// for (Map.Entry<String, Cube> entry : configs["latest_configs"].entrySet()) {
			// 	System.out.println(entry.getKey() + "/" + entry.getValue());
			// }


			
			//     // Iterate through HashMap entries(Key-Value pairs)
			//     System.out.println("HashMap Key-Value Pairs : ");
			//     while(it.hasNext()){
			//        Map.Entry me = (Map.Entry)it.next();
			//        System.out.println("Key is: "+me.getKey() + 
			//        " & " + 
			//        " value is: "+me.getValue());
			//    }






			// 		for (String hash: configs["latest_configs"].keySet()){





			// 			for (int direction: new int[]{-1,1}){
			// 				for (String axis:new String[] {"x","y","z"}){
			// 					Cube candidate = configs["latest_configs"].get(hash).rotate(axis,direction);
								




			// 				}
			// 			}
			// 		}
	}


// def generate_for_one_set_of_configs(configs):
// 	# new_configs = np.array([[[0]*3]*8]*400000,dtype = np.byte)
// 	# new_configs = []#
// 	new_configs = configs["zeroes"].copy()
// 	it = 0
// 	for config in configs["latest_configs"]:
// 		for direction in [-1,1]:
// 			for axis in "xyz":
// 				c = rotate(config,direction,axis)
// 				c_hash =   "".join(["".join([str(k) for k in i]) for i in c])
// 				if c_hash not in configs["hashes"] and len(c_hash) == 24:
// 					configs["hashes"].add(c_hash)
// 					new_configs[it] = c
// 					it+=1
// 	# configs["latest_configs"]= np.array(new_configs,dtype=np.byte)#[:it]
// 	configs["latest_configs"]= np.array(new_configs[:it],dtype=np.byte)


// 	// import time
// 	// last_key = 0
// 	// new_configs = [initial_config]
// 	// initial_hash = "".join([str(i)+"".join([v for k,v in initial_config[i].items()]) for i in initial_config])
// 	// configs = { "latest_configs":[initial_config], "hashes": set(initial_hash) }
// 	// init = time.time()
// 	// while configs["latest_configs"] != []:
// 	// 	generate_for_one_set_of_configs(configs)
// 	// 	last_key = last_key +1
// 	// 	print(last_key,len(configs["latest_configs"]),str(time.time()-init)+ " seconds")








	// public void generateNewConfigs(ArrayList<Cube> configs,int iterations){
	// 	System.out.println(configs.size());
	// 	ArrayList<Cube> newConfigs = new ArrayList<Cube>();
	// 	HashMap<String, Cube> cubeMap = generateFromCube(configs);
	// 	for (String hash: cubeMap.keySet()){
	// 			if (!this.existingHashes.contains(hash)){
	// 				newConfigs.add(cubeMap.get(hash));
	// 				this.existingHashes.add(hash);
	// 			}
			

	// 	}
	// 	if (iterations == 2){
	// 		StringJoiner sj = new StringJoiner("\',\'");
	// 		for (String s: this.existingHashes){
	// 			sj.add(s);
	// 		}

	// 		System.out.println(sj.toString());
	// 	}
	// 	if (newConfigs.size() > 0) {generateNewConfigs(newConfigs,iterations +1);}
	// }

	// public HashMap<String, Cube> generateFromCube(ArrayList<Cube> cb){
	
	// 	HashMap<String, Cube> newConfigs = new HashMap<String,Cube>();
	// 	for (Cube c: cb){
	// 			for (String axis: new String[]{"x","y","z"}){
	// 				for (int dir: new int[]{-1,1}){
	// 					Cube n = c.rotate(axis,dir);
	// 					String h = n.generateHash();
	// 							newConfigs.put(h,n);
	// 				}
	// 		}
	// 	}
	// 				return newConfigs;

	// 	}
}