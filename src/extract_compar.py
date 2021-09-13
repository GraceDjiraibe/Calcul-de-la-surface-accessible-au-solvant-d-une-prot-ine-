"""
Module that will extract the data from the NACCESS file and 
then compare with the result that we find 
"""

import pandas as pd 
from matplotlib import pyplot as plt 

def extract_file(naccess_file):
	"""
	This function extract the residu name, the accessibility and the number
	from the NACCES file.

	PARAMETERS
	----------
		** naccess_file : str
			file containingbthe surface of residu 
			accessible to the solvant.

	RETURN
	------
		** result_data : data framr 
	"""

	result_dict = {'residu':[], 'access':[], 'number':[]}
	with open(naccess_file, 'r') as res:
		for line in res:
			if line.startswith("RES"):
				result_dict['residu'].append(line[3:7].strip())
				result_dict['access'].append(float(line[14:23].strip()))
				result_dict['number'].append(line[11:14].strip())
	result_data = pd.DataFrame(result_dict)
	return result_data



def result_plot(naccess_file, my_file, residus):
	"""
	Plot that compared the result that we find on NACCESS and our results.

	PARAMETERS
	----------
		** naccess_file : str
			file containingbthe surface of residu 
			accessible to the solvant.
		** my_file : str
			file with our residu accessibility results.
		** residus : 
			Residus names.
	"""

	diff = []
	for i in range(len(naccess_file)-(len(naccess_file)-len(my_file))):
		#diff.append(abs(naccess_file[i]-my_file[i]))

		plt.plot(naccess_file, label="Naccess result")
		plt.plot(my_file, label="Our result")
		#plt.plot(diff, label="Difference")
		plt.xticks(range(len(naccess_file)), residus)
		plt.xlabel("Residus")
		plt.ylabel("Accessibility")
		plt.legend()
		plt.show()

if __name__ == "__main__":
	import extract_compar
	print(help(extract_compar))
    

