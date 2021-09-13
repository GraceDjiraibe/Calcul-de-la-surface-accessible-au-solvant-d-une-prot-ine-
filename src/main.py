"""
Main of the project 

To be used from the Shell
-------------------------
	$ python main.py arg1 arg2 arg3
		** arg 1 : str
			pdb file (file.pdb)
		** arg 2 : str
			the Naccess file obtain from the pdb (file.rsa)
		** arg 3 : int
			number of points that we want to simulate on the sphere 
			surface 	
			
"""
import argparse
import pandas as pd 
import atom_coord
import atom_sphere
import extract_compar 
import atom_surface 

if __name__ == "__main__":

	PARSER = argparse.ArgumentParser()

	PARSER.add_argument("file_pdb", help = "Enter the pdb file name", type = str)
	PARSER.add_argument("number_point", help = "Number of points you want to simulate onto the sphere surface", type = int)
	PARSER.add_argument("file_rsa", help = "The rsa file obtain on NACCESS from the pdb ")
	

	ARGS = PARSER.parse_args()

	
	PDB = ARGS.file_pdb
	POINT = ARGS.number_point
	RSA = ARGS.file_rsa

	print("=============================================================================")

	print(" 1: PARSING THE PDB FILE AND CREATING A DATA FRAME FROM IT. ")

	DATA_FRAME = atom_coord.atoms_coords(PDB)

	print("=============================================================================")
	#=================================================================================
	#=================================================================================

	print(" 2: DISTANCE MATRIX OF THE ATOMS. ")

	MAT_DIST = atom_sphere.dist_matrix(DATA_FRAME)
	print("=============================================================================")
	

	#=================================================================================
	#=================================================================================

	print(" 3: SELECTING THE ATOMS NEIGHBOORS.")

	NEW_MAT_DIST = atom_sphere.neighboors(MAT_DIST)
	print("=============================================================================")
	

	#=================================================================================
	#=================================================================================

	print(" 4: CREATION OF THE SPHERES AROUND EVERY ATOMS AND CALCULATING THE DISTANCES. ")

	SPHERE = atom_sphere.contact_atom(DATA_FRAME, NEW_MAT_DIST, POINT)
	print("=============================================================================")
	

	#=================================================================================
	#=================================================================================
	print(" 5:PROPORTION OF EXPOSED POINT. ")

	RATIO = atom_surface.prop(SPHERE,POINT)
	print("=============================================================================")
	

	#=================================================================================
	#=================================================================================

	print(" 6: SASA FOR EACH ATOMS. ")

	ATOM_ACCESS_SURF = atom_surface.surface(RATIO, DATA_FRAME)
	print("=============================================================================")
	

	#=================================================================================
	#=================================================================================

	print(" 7: SASA FOR EVERY RESIDU. ")

	RESIDU_ACCESS_SURF = atom_surface.final_surface(ATOM_ACCESS_SURF, DATA_FRAME)
	print("=============================================================================")
	

	#=================================================================================
	#=================================================================================

	result = {}
	res_name = []
	access = []

	for key in RESIDU_ACCESS_SURF:
		res_name.append(key.split()[1])
		access.append(RESIDU_ACCESS_SURF[key])

	result["residu"] = res_name
	result["Accesibility"] = access

	data_result = pd.DataFrame(result)
	data_result.to_csv(PDB.split('/')[-1].split('.')[0]+'.csv')
	print("=============================================================================")
	

	#=================================================================================
	#=================================================================================

	print(data_result)
	print("=============================================================================")
	

	#=================================================================================
	#=================================================================================

	print(" The Protein accessibility is : {} ".format(sum(access)))
	print("=============================================================================")
	

	#=================================================================================
	#=================================================================================


	RSA_FILE = extract_compar.extract_file(RSA)
	
	

	#=================================================================================
	#=================================================================================

	# Plot showing the differences between the rsa file and our program.

	extract_compar.result_plot(RSA_FILE["access"].tolist(), data_result["Accesibility"].tolist(),
	RSA_FILE["residu"].tolist())




