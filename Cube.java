import java.lang.Integer;
import java.util.*;

public class Cube{
		// Map map = new HashMap<Integer, HashMap<String,Integer>>();
		// // W,O,B,Y,G,R 
		public final int WHITE = 0;
		public final int ORANGE = 1;
		public final int BLUE = 2;
		public final int YELLOW = 3;
		public final int GREEN = 4;
		public final int RED = 5;
		public int[][] configuration;

// initial_config = {1:{"x":W,"y":O,"z":B}, 2:{"x":Y,"y":O,"z":B},
// 						3:{"x":Y,"y":R,"z":B}, 4:{"x":W,"y":R,"z":B},
// 						5:{"x":W,"y":O,"z":G}, 6:{"x":Y,"y":O,"z":G},
// 						7:{"x":Y,"y":R,"z":G}, 8:{"x":W,"y":R,"z":G},
// }

	public Cube(){
		// Map m1 = new HashMap<String,Integer>();	m1.put("x",WHITE);m1.put("y",ORANGE);m1.put("z",BLUE);map.put(1,m1);
		// m1 = new HashMap<String,Integer>();	m1.put("x",YELLOW);m1.put("y",ORANGE);m1.put("z",BLUE);map.put(2,m1);	
		// m1 = new HashMap<String,Integer>();	m1.put("x",YELLOW);m1.put("y",RED);m1.put("z",BLUE);map.put(3,m1);
		// m1 = new HashMap<String,Integer>();	m1.put("x",WHITE);m1.put("y",RED);m1.put("z",BLUE);map.put(4,m1);	
		// m1 = new HashMap<String,Integer>();	m1.put("x",WHITE);m1.put("y",ORANGE);m1.put("z",GREEN);map.put(5,m1);
		// m1 = new HashMap<String,Integer>();	m1.put("x",YELLOW);m1.put("y",ORANGE);m1.put("z",GREEN);map.put(6,m1);	
		// m1 = new HashMap<String,Integer>();	m1.put("x",YELLOW);m1.put("y",RED);m1.put("z",GREEN);map.put(7,m1);
		// m1 = new HashMap<String,Integer>();	m1.put("x",WHITE);m1.put("y",RED);m1.put("z",GREEN);map.put(8,m1);
		this.configuration = new int[][] {{WHITE,ORANGE,BLUE},
										   {YELLOW,ORANGE,BLUE},
										   {YELLOW,RED,BLUE},
										   {WHITE,RED,BLUE},
										   {WHITE,ORANGE,GREEN},
										   {YELLOW,ORANGE,GREEN},
										   {YELLOW,RED,GREEN},
										   {WHITE,RED,GREEN}};

		}

	public static void main(String[] args){
		Cube c = new Cube();
		Cube k = c.rotate("x",1);
		System.out.println(c);
		System.out.println(k);
	}
	
	public Cube rotate( String axis, int direction){

		Cube k = new Cube();

		int[][] axes;// ={{"z", "y"}, {"y", "z"}, {"x", "x"}}
		int[] cubes;// = new int[]{2,3,7,6};// = new int[];//= new int[4];
	// 		axis_dict = {"x":{"axes":["zy","yz","xx"],"cubes" : [2,3,7,6]},"y":{"cubes" : [4,8,7,3], "axes" : ["zx","xz","yy"]},"z":{"cubes" :[1,2,3,4],"axes" :["xy","yx","zz"]}}
	// axis_dict = {"x":{"axes":[(2,1),(1,2),(0,0)],"cubes" : [1,2,6,5]},"y":{"cubes" : [3,7,6,2], "axes" : [(2,0),(0,2),(1,1)]},"z":{"cubes" :[0,1,2,3],"axes" :[(0,1),(1,0),(2,2)]}}
	
		if (axis.equals("x"))//  : #2,3,7,6
		{
		 axes = new int[][]{{2, 1}, {1, 2}, {0, 0}};
		 cubes = new int[]{1,2,6,5};
		}

		else if (axis.equals("y")) //: #4,8,7,3
		{
			 cubes = new int[]{3,7,6,2};
			 axes = new int[][]{{2, 0}, {0, 2}, {1, 1}};
		}

		else
			{ cubes = new int[]{0,1,2,3};
			 axes = new int[][]{{0, 1}, {1, 0}, {2, 2}};
			}
		
		for (int i= 0; i<4; i++){
			for (int[] pair: axes){
				int other_cube_number = cubes[(((i+direction)%4)+4)%4];
				int initial_cube_number = cubes[i];

				k.configuration[initial_cube_number][pair[0]] = this.configuration[other_cube_number][pair[1]];
					}
				}

				return k;

	}

	public String generateHash(){
		// String out = "";
		// for (int[] arr:this.configuration){
		
		// 	for (int s: arr){
		// 		out = out + String.valueOf(s);
		// 	}
		// }

		// return out;
		StringJoiner sj = new StringJoiner("");
		for (int[] row : this.configuration) {
			sj.add(Arrays.toString(row));
		}
		String result = sj.toString();
		result = result.replace(" ","").replace("]","").replace("[","").replace(",","");

		return result;
			
		}	

	


	public String toString(){
		String out = "";
		for (int[] arr:configuration){
			out = out +"\n";
			for (int s: arr){
				out = out +" "+ s;
			}
		}

		return out;
		}													
	
}