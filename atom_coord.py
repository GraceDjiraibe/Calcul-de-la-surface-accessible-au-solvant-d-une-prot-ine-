"""
Read the PDB format file and also extract the atom x,y and z coordinates numbers.

"""

import pandas as pd 

def atoms_coords(pdb_file):

	"""
	This function can read all the pdb file and extract all the atom coordiantes number 
		,which are return as a list the which contains the atom and its coordinates.

	PARAMETERS
	----------
		** pdb_file : str
			The pdb extension file.
	RETURN
	------
		** atoms_data : list
			Atoms and their x,y,z coordinates 
	"""

	with open(pdb_file,"r") as my_seq:
		coords = []
		for line in my_seq:
			if line[0:4] == "ATOM":
				dict_atom = {}
				dict_atom["atom"] = str(line[77:99].strip())
				dict_atom["residu"] = str(line[17:21].strip())
				dict_atom["N° resid"] = int(line[22:26].strip())
				dict_atom["x"] = float(line[22:26].strip())
				dict_atom["y"] = float(line[38:46].strip())
				dict_atom["z"] = float(line[46:54].strip())
				coords.append(dict_atom)
		data_atom = pd.DataFrame(coords)
	return data_atom

if __name__ == "__main__":
	import atom_coord
	print(help(atom_coord))


