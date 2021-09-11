"""
This module is used for choosing the right atom neighboors and then creating a sphere
which will be used for evaluating the distances between each atoms.
 
"""

import numpy as np 
import pandas as pd 
import time
from scipy.spatial import distance_matrix 



# The VDW radius of all the periodic elements.
# We will use those for the dtermination of the distance beteween each atom. 

VDW_RADIUS = {'H': 1.20, 'C': 1.7, 'N': 1.55, 'O': 1.52,'S': 1.80} 

def sphere_coords(nb):
 	"""
 	This fucntion can simulate a sphere contaning nb points 

 	PARAMETERS 
 	----------
 		** nb : int
 			The number of points simulating on the sphere surface.
 	RETURNS
 	-------
 		** sphere_coords : array
 			Array containing the x,y and z coordinates.
 	"""

 	indice = np.arange(0, nb, dtype = float) + 0.5
 	golden_angle = np.pi * (1 + 0.5**0.5)
 	phi = np.arccos(1 - 2*indice/nb)
 	theta = golden_angle * indice

 	sphere_coords = np.zeros((nb, 3))
 	sphere_coords[:, 0] = np.cos(theta) * np.sin(phi)
 	sphere_coords[:, 1] = np.sin(theta) * np.sin(phi)
 	sphere_coords[:, 2] = np.cos(phi)

 	return sphere_coords


def dist_eucl(coord1, coord2):
	"""
	Function that calculate the euclidian distance between 2 points

	PARAMETERS 
	----------
		** coord1, coord2 : flaot
			frist and second point coordinates. 

	RETURN
	------
		** dist : flaot
			The euclidian distance. 
	"""

	squared_dist = np.sum((coord1-coord2)**2, axis = 0)
	dist = np.sqrt(squared_dist)

	return dist 


def dist_matrix(data_coords_atom):
 	"""
 	This function create a matrix distance between all the atoms.

 	PARAMETERS
 	----------
 		** data_coords_atoms : float 
 			Data Frame of the coordiantes atoms.
 	RETURN
 	------
 		** Data Frame of the atoms distances.
 	"""
 	return pd.DataFrame(distance_matrix(data_coords_atom.iloc[:,3:],
 		data_coords_atom.iloc[:,3:]), index = data_coords_atom.iloc[:, 3:].index,
 	columns = data_coords_atom.iloc[:, 3:].index)

 

def neighboors(data_frame_matrix):
 	"""
 	This function is creating a dictionnary from the dataframe 
 	which having as keys the atoms and as values their atom neighboors.

 	PARAMETERS 
 	----------
 		** data_frame_matrix: dataframe.
 	RETURNS
 	-------
 		** atom_neighboors: dict
 			Dictionnary containing all the atoms and their neighboor.
 	"""

 	THRESOLD = 1.4 + VDW_RADIUS['S'] * 2
 	row_matrix =[]
 	i_matrix = []

 	for index, row in data_frame_matrix.iterrows():
 		row_matrix.append(row)
 		i_matrix.append(index)

 	atom_neighboors = {}
 	for i in range(len(i_matrix)):
 		neighboors = []
 		for j in range(len(row_matrix[i]) - 1):
 			if(row_matrix[i][j] < THRESOLD) & (i != j):
 				neighboors.append(j)
 		atom_neighboors[i] = neighboors

 	return atom_neighboors

def contact_atom(data_coords_atom, atom_neighboors, nb):
	"""
	This function creating sphere between close atoms and the calculate 
	the distance between them.

	PARAMETERS
	----------
		** data_coords_atom : float 
 			Data Frame of the coordiantes atoms
 		** atom_neighboors : dict
 			Dictionnary containing all the atoms and their neighboor.
		** nb : int
			Number of points that we are goinf to create on the sphere later.

	RETURN
	------
		** atom_solvate_dict : dict
			Dictionary containing atoms wich can have water in between them.			
	"""

	atom_solvate_dict = {}
	for key in atom_neighboors:
		new_neighboors = []
		new_neighboors.append(key)
		for atom in atom_neighboors[key]:
			new_neighboors.append(atom)
		sphere_atom = sphere(data_coords_atom.iloc[[new_neighboors[0]], ], nb)

		center = []
		for row_matrix in data_coords_atom.iloc[new_neighboors[1:], ].iterrows():
			center.append([row_matrix[1][3], row_matrix[1][4], row_matrix[1][5], VDW_RADIUS[row_matrix[1][0]]])

		for i in range(len(center) - 1):
			atom_solvate_dict[str(key) + " " + str(i + 1)] = dist_sphere_atom(sphere_atom[0], center[i])
	
	return atom_solvate_dict

def sphere(data_coords_atom, nb):
	"""
	This function is use to create spheres with differents radius and postitions 
	depending of the atoms that we considere

	PARAMETERS
	----------
		** data_coords_atom : float 
 			Data Frame of the coordiantes atoms 
		** nb : int
			Number of points that we are goinf to create on the sphere later.
	
	RETURN
	------
		** coord_point : list
			A list of all the sphere coordinates points 
	"""

	coord_point = []
	for row_matrix in data_coords_atom.iterrows():
		sphere_points = sphere_coords(nb) 
		radius = VDW_RADIUS[row_matrix[1][0]]
		sphere_points[:, 0] = sphere_points[:, 0] * radius + row_matrix[1][3]
		sphere_points[:, 1] = sphere_points[:, 1] * radius + row_matrix[1][4]
		sphere_points[:, 2] = sphere_points[:, 2] * radius + row_matrix[1][5]
		coord_point.append(sphere_points)
	return coord_point



def dist_sphere_atom(points, center):
	"""
	This function can calculate the distance between sphere's center and all the 
	points that they share together.

	PARAMETERS
	----------
		** points : float 
			coordinates of all the points on the surface of the sphere
		** center : float
			coordinates of the center of the sphere

	RETURN
	------
		** contact_points : int
			Number of all the mutals points 
	"""

	points_counts = 0
	is_Contact = False
	for i in range(len(points)):
		if dist_eucl(points[i], center[0:3]) < 2.8 + center[3]:
			is_Contact = False
		else:
			is_Contact = True
		if is_Contact:
			points_counts += 1
	return points_counts






if __name__ == "__main__":
	import atom_sphere
	print(help(atom_sphere))











