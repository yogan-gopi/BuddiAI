#9_clique.py 

import numpy as np

MAX = 100

store = [0]* MAX

graph = np.zeros((MAX, MAX))

d = [0] * MAX

def is_clique(b) :
	for i in range(1, b) :
		for j in range(i + 1, b) :
			if (graph[store[i]][store[j]] == 0) :
				return False;
	return True;

def print_cli(n) :

	for i in range(1, n) :
		print(store[i], end = " ");
	print(",", end=" ");

def findCliques(i, l, s) :

	for j in range( i + 1, n -(s - l) + 1) :

		if (d[j] >= s - 1) :

			store[l] = j;

			if (is_clique(l + 1)) :

				if (l < s) :
					findCliques(j, l + 1, s);

				else :
					print_cli(l + 1);

if __name__ == "__main__" :

	edges = [ [ 1, 2 ],
			[ 2, 3 ],
			[ 3, 1 ],
			[ 4, 3 ],
			[ 4, 5 ],
			[ 5, 3 ] ];
	k = 3;
	size = len(edges);
	n = 5;

	for i in range(size) :
		graph[edges[i][0]][edges[i][1]] = 1;
		graph[edges[i][1]][edges[i][0]] = 1;
		d[edges[i][0]] += 1;
		d[edges[i][1]] += 1;
	

	findCliques(0, 1, k);

