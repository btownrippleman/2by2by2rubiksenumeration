// ok, so in this version of the same code, perhaps i should try to do it in c vs c++, i don't think it matters 
// but the idea is to create a 3d array, essentially an array of matrices that will store all the configurations of the
// pocket cube and the job of the code is keep track of the lo and hi values, i.e. the range of values, the window of values
// that are being drawn from to create new ones and then where to store the new matrices, i.e. just above the lo and hi.
// Then there will be a hashmap that stores the strings that are associated with each matrix and the number 

// C++ Program to print the elements of a
// Two-Dimensional array
#include<iostream>
#include<math.h>
using namespace std;

int main()
{

    double (*sample) [200000];
s = malloc(sizeof(*sample) * 2); 
sample[0][0] = 0.0;
sample[1][199999] = 9.9;
    // int xdim=3,ydim=4,zdim = 5;

	// int ***a3d = (int ***)malloc(xdim * sizeof(int **));
	// for(int i = 0; i < xdim; i++) {
	// 	a3d[i] = (int **)malloc(ydim * sizeof(int *));
	// 	// for(int j = 0; j < ydim; j++)
	// 	// 	a3d[i][j] = (int *)malloc(zdim * sizeof(int));
	// }
	// an array with 3 rows and 2 columns.
	// int x[malloc(400000)][3][8];

	// output each array element's value
	// for (int i = 0; i < 3; i++)
	// {
	// 	for (int j = 0; j < 2; j++)
	// 	{
    //         a3d[i][j] = rand() %10;
	// 		cout << "Element at x[" << i
	// 			<< "][" << j << "]: ";
	// 		cout << a3d[i][j]<<endl;
	// 	}
	// }

	return 0;
}
