"""
This module will be used to calculate the area exposed to the solvant.
"""
import numpy as np 


VDW_RADIUS = {'H': 1.20, 'C': 1.7, 'N': 1.55, 'O': 1.52,'S': 1.80} 


def prop(points, nb):

       """
       This function can calcultate the proportion of the exposed points out of
       the total point on the surface of the sphere

       PARAMETERS 
       ----------
              ** points : dict 
                     Coordinates of all the points.
              ** nb : int 
                     number of points
       RETURN
       ------
              ** final_prop : dict 
                     Dictionnary containing the proportion of exposed point for each 
                     atom.
       """

       exposed = []
       dict_prop = {}
       val = '0'
       for key in points:
              if key.split()[0] != val:
                     dict_prop[val] = [exposed, len(exposed)]
                     exposed = []
              if points[key] != 0:
                     exposed.append(points[key])
              val = key.split()[0]
       dict_prop[val] = [exposed, len(exposed)]
       final_prop = {}
       for key in dict_prop:
              if dict_prop[key][1] != 0:
                     final_prop[key] = (sum(dict_prop[key][0]) / (dict_prop[key][1] * nb))
              else:
                     final_prop[key] = 0
       return final_prop

def surface(final_prop, data_coords_atom):
       """
       This function can calculate the portion of solvant that is expose to each atoms

       PARAMETERS
       ----------
              ** final_prop :  dict
                     The ratio of the exposed points.
              ** data_coords_atom : 
                     The atoms dataframe

       RETURN
       ------
              ** dict_surface : dict
                     A dictionnary of all the contact surface for 
                     each atom.                  
       """

       dict_surface = {}
       for key in final_prop:
              dict_surface[key] = final_prop[key] * 4 * np.pi + \
              (VDW_RADIUS[data_coords_atom.iloc[int(key), 0]])**2
       return dict_surface

def final_surface(dict_surface, data_coords_atom):
       """
       This fucntion can add the residu surface that is expoded to the solvant 
       by adding all the atoms (which constituate the residu himself) surface that are exposed to the solvant 

       PARAMETERS
       ----------
              ** dict_surface : 
                     A dictionnary of all the contact surface for 
                     each atom.
              ** data_coords_atom : 
                     The atoms dataframe.
       RETURN
       ------
              ** final_surf : dict
                     Dictionary with residus accessible surface
       """


       dico = {}
       i = 0
       for row_matrix in data_coords_atom.iterrows():
              if row_matrix[0] == 0:
                     val = str(row_matrix[1][1] + ' ' + str(row_matrix[1][2]))
              
              if str(row_matrix[1][1]) + ' ' + str(row_matrix[1][1]) == val:
                     if str(i) + ' ' + str(row_matrix[1][1]) not in dico:
                            dico[str(i)+' '+str(row_matrix[1][1])] = []
                     dico[str(i)+' '+str( row_matrix[1][1])].append(row_matrix[0])

              elif str(row_matrix[1][1]) + ' ' + str(row_matrix[1][1]) != val:
                     i += 1
                     val = str(row_matrix[1][1] +' '+str(row_matrix[1][1]))

                     if str(i)+ ' ' + str(row_matrix[1][1]) not in dico:
                            dico[str(i)+' '+ str(row_matrix[1][1])] = []
                     dico[str(i)+ ' ' + str(row_matrix[1][1])].append(row_matrix[0])

       final_surf = {}

       for j in dico:
              for k in dico[j]:
                     if j not in final_surf:
                            final_surf[j] = 0
                     final_surf[j] += dict_surface[str(k)]
       return final_surf

if __name__ == "__main__":
       import surface 
       print(help(surface))



























