package main

// 	W,O,B,Y,G,R = "white","orange","blue","yellow","green","red"
// colors = [W,O,B,Y,G,R]
// W,O,B,Y,G,R = [i[0].upper() for i in colors]

import (
	"fmt"
	"time"
)

// import "math/rand"

func rotate(inM [8][3]int, axis string, dir int) [8][3]int {
	// axis_dict = {"x":{"axes":["zy","yz","xx"],"cubes" : [2,3,7,6]},"y":{"cubes" : [4,8,7,3], "axes" : ["zx","xz","yy"]},"z":{"cubes" :[1,2,3,4],"axes" :["xy","yx","zz"]}}
	// axis_dict = {"x":{"axes":[(2,1),(1,2),(0,0)],"cubes" : [1,2,6,5]},"y":{"cubes" : [3,7,6,2], "axes" : [(2,0),(0,2),(1,1)]},"z":{"cubes" :[0,1,2,3],"axes" :[(0,1),(1,0),(2,2)]}}
	outM := [8][3]int{{0, 0, 0}, {0, 0, 0}, {0, 0, 0}, {0, 0, 0}, {0, 0, 0}, {0, 0, 0}, {0, 0, 0}, {0, 0, 0}}
	if axis == "x" {
		cubes := []int{1, 2, 6, 5}
		for j := 0; j < 4; j++ {
			var first_cube = cubes[j]
			var second_cube = cubes[(j+dir+4)%4]
			outM[first_cube][2] = inM[second_cube][1]
			outM[first_cube][1] = inM[second_cube][2]
			outM[first_cube][0] = inM[second_cube][0]
		}
		//copy the rest
		cubes = []int{0, 3, 4, 7}
		for j := 0; j < 4; j++ {
			for k := 0; k < 3; k++ {
				outM[cubes[j]][k] = inM[cubes[j]][k]
			}
		}

	}

	if axis == "y" {
		outM = inM
		cubes := []int{3, 7, 6, 2}
		for j := 0; j < 4; j++ {
			var first_cube = cubes[j]
			var second_cube = cubes[(j+dir+4)%4]
			outM[first_cube][2] = inM[second_cube][0]
			outM[first_cube][0] = inM[second_cube][2]
			outM[first_cube][1] = inM[second_cube][1]
		}
		//copy the rest
		cubes = []int{0, 1, 4, 5}
		for j := 0; j < 4; j++ {
			for k := 0; k < 3; k++ {
				outM[cubes[j]][k] = inM[cubes[j]][k]
			}
		}

	}

	if axis == "z" {
		outM = inM
		cubes := []int{0, 1, 2, 3}
		for j := 0; j < 4; j++ {
			var first_cube = cubes[j]
			var second_cube = cubes[(j+dir+4)%4]
			outM[first_cube][1] = inM[second_cube][0]
			outM[first_cube][0] = inM[second_cube][1]
			outM[first_cube][2] = inM[second_cube][2]
		}
		cubes = []int{4, 5, 6, 7}
		for j := 0; j < 4; j++ {
			for k := 0; k < 3; k++ {
				outM[cubes[j]][k] = inM[cubes[j]][k]
			}
		}

	}
	return outM

}

func genHash(arr [8][3]int) string {
	outString := ""
	for i := 0; i < 8; i++ {
		for j := 0; j < 3; j++ {
			outString += fmt.Sprint(arr[i][j])
		}
	}
	return outString
}

func changeconfigurations(x [50000][8][3]int) {
	for i := 0; i < 50000; i++ {
		for j := 0; j < 6; j++ {
			for k := 0; k < 6; k++ {
				x[i][j][k] = 1 // i+j+k //rand.Intn(10)
			}
		}
	}
}

func main() {
	start := time.Now()
	var configurations = new([4000000][8][3]int)
	var hashArray = new([4000000]string)
	var initial_config = [8][3]int{{0, 1, 2}, {3, 1, 2}, {3, 5, 2}, {0, 5, 2}, {0, 1, 4}, {3, 1, 4}, {3, 5, 4}, {0, 5, 4}}
	var mapOfExistingConfigurations = make(map[string]string)
	var duplicateRotations = make(map[string][]string)
	mapOfExistingConfigurations[genHash(initial_config)] = "0"
	var lo = 0
	var hi = 1
	var numrotations = 1
	configurations[0] = initial_config
	hashArray[0] = genHash(initial_config)
	var newIndex = hi
	var newConfigsProduced = true
	for newConfigsProduced {
		newConfigsProduced = false

		for lo != hi {
			existingHash := hashArray[lo]
			for _, axis := range []string{"x", "y", "z"} {
				for _, direction := range []int{-1, 1} {
					newConfig := rotate(configurations[lo], axis, direction)
					newHash := genHash((newConfig))
					_, exist := mapOfExistingConfigurations[newHash]
					if !exist {
						newConfigsProduced = true
						mapOfExistingConfigurations[newHash] = existingHash + axis + fmt.Sprint(direction)
						hashArray[newIndex] = newHash
						configurations[newIndex] = newConfig
						newIndex += 1

					} else {
						mapOfExistingConfigurations[newHash] = existingHash + axis + fmt.Sprint(direction)
						_, existingRotation := duplicateRotations[axis]
						if existingRotation {
							duplicateRotations[axis] = append(duplicateRotations[axis], existingHash)

						} else {

							duplicateRotations[axis] = []string{existingHash}
							fmt.Println(axis, duplicateRotations[axis])
						}
					}
				}

			}
			lo = lo + 1
		}
		fmt.Println(fmt.Sprint(numrotations), "rotations yields", fmt.Sprint(newIndex-hi), "new configurations computed in", time.Since(start))
		lo = hi
		hi = newIndex
		numrotations += 1
	}

	fmt.Println("time passed: ", time.Since(start))

}
