# Calcul-de-la-surface-accessible-au-solvant-d-une-prot-ine-



## Projet Court : Calcul de la surface accessible au solvant d'une proétine


This project was made to calculate the accessible surface of a protein to the solvate, in order to predict the structure.


## To be used with 

First you have to create the right environment where the code will be compiled, you'll find the file projetcourt.yml in the repertory. 

```
$ conda env create -f projet.yml
```
 You can also create and install the library needed just like bellow 
 
 ```
 $ conda create -n env yourproject
 $ activate yourproject
 $ conda install pandas
 $ conda insall matplotlib
 $ conda install -c conda-forge argparse
 $ conda install scipy
 
 ```
 
 ## System 
 
 This program can be run on both Linux and windows environnemnt
 
 
 ## Data 
 
 input files : 1UBQ.pdb 1UBQ.rsa 1BOQ.pdb 1BOQ.rsa
 
 ## Scripts 
 
 * atom_coord.py
 * atom_sphere.py
 * atom_surface.py
 * extract_compar.py
 * mains.py
 
 ## Programs 
 
 NACCESS or FreeSASA
 
 ## Manual
 
 * Make a clone of this repository 

```
$ git clone https://github.com/GraceDjiraibe/Calcul-de-la-surface-accessible-au-solvant-d-une-prot-ine-.git

```

* Run the code 

```
$ python main.py file.pdb point_numbre file.rsa

```
 
 
