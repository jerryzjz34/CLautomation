#!/Users/jeremiahzamora/opt/anaconda3/bin/python

#import modules
import numpy as np
import decimal
import math
import os
import sys
import json

with open('job.sh', 'r') as file1:
	file_data2 = file1.read()

with open('KPOINTS','r') as file2:
	file_data3 = file2.read()

with open('INCAR','r') as file3:
	file_data4 = file3.read()

with open('POTCAR','r') as file4:
	file_data5 = file4.read()

parent = os.getcwd()

#with open('PeriodicTableJSON.json', 'r') as pt:
#     pt_data = json.load(pt)
#starting Positions of AP w/ respect to a lattice vector
cl_a1_old = 0.1
o_a1_old = 0.013466144132375
o_a2_old = 0.186533855867625
o_a3_old = 0.1
o_a4_old = 0.1
n_a1_old = 0.37106466361855
h_a1_old = 0.37106466361855
h_a2_old = 0.310222077073808
h_a3_old = 0.37106466361855
h_a4_old = 0.431907250163292

#starting positios of AP w/respect to b lattice vector

cl_b1_old = 0.1
o_b1_old = 0.161593729588504
o_b2_old = 0.161593729588504
o_b3_old = 0.041715654256477
o_b4_old = 0.0370346178968
n_b1_old = 0.1
h_b1_old = 0.174907467885913
h_b2_old = 0.078761158284346
h_b3_old = 0.069018070977575
h_b4_old = 0.078761158284346

#not too worried about this part right now. Trying to work with one direction first then do the other. Then we can implement the two differently.
#Think it wouldnt be that hard...
for y in np.arange(0.0, 0.9, 0.1):
	cl_b1 = cl_b1_old+y
	o_b1 = o_b1_old+y
	o_b2 = o_b2_old+y
	o_b3 = o_b3_old+y
	o_b4 = o_b4_old+y
	n_b1 = n_b1_old+y
	h_b1 = h_b1_old+y
	h_b2 = h_b2_old+y
	h_b3 = h_b2_old+y
	h_b4 = h_b4_old+y
	for x in np.arange(0.0, 0.6, 0.1):
		#reason for this is that we do not want the molecule being separated along the finite unit cell.
		#writes the POSCAR files to individual directories
		with open('POStempl', 'r') as file:
		#elements = file.readlines()ZZ
			file_data = file.read()
		#string based on position of chlorine atom
			directory = str(round(x,1)) + str(round(y,1))
			os.makedirs(directory, exist_ok = True)
			numdir = os.path.join(parent,directory)
			print(numdir)
			cl_a1 = cl_a1_old+x
			o_a1 = o_a1_old+x
			o_a2 = o_a2_old+x
			o_a3 = o_a3_old+x
			o_a4 = o_a4_old+x
			n_a1 = n_a1_old+x
			h_a1 = h_a1_old+x
			h_a2 = h_a2_old+x
			h_a3 = h_a3_old+x
			h_a4 = h_a4_old+x
			print(cl_a1)
			print(o_a1)
			print(o_a2)
			print(o_a3)
			print(o_a4)

			file_data = file_data.replace('%cl_a1', str(cl_a1))
			file_data = file_data.replace('%o_a1', str(o_a1))
			file_data = file_data.replace('%o_a2', str(o_a2))
			file_data = file_data.replace('%o_a3', str(o_a3))
			file_data = file_data.replace('%o_a4', str(o_a4))
			file_data = file_data.replace('%n_a1', str(n_a1))
			file_data = file_data.replace('%h_a1', str(h_a1))
			file_data = file_data.replace('%h_a2', str(h_a2))
			file_data = file_data.replace('%h_a3', str(h_a3))
			file_data = file_data.replace('%h_a4', str(h_a4))

			file_data = file_data.replace('%cl_b1', str(cl_b1))
			file_data = file_data.replace('%o_b1', str(o_b1))
			file_data = file_data.replace('%o_b2', str(o_b2))
			file_data = file_data.replace('%o_b3', str(o_b3))
			file_data = file_data.replace('%o_b4', str(o_b4))
			file_data = file_data.replace('%n_b1', str(n_b1))
			file_data = file_data.replace('%h_b1', str(h_b1))
			file_data = file_data.replace('%h_b2', str(h_b2))
			file_data = file_data.replace('%h_b3', str(h_b3))
			file_data = file_data.replace('%h_b4', str(h_b4))

		with open(os.path.join(parent,directory,'POSCAR'), 'w') as file:
			file.write(file_data)


		#Obtaining species for POTCAR
		#This is future me problem. I am not too woried about this because I only work with a minor amount of 
		with open(os.path.join(parent,directory,'POSCAR'), 'r') as file:
			elements = file.readlines()
			species = elements[5]
			#print(species)

			#need to write other necessary files for VASP

		with open(os.path.join(parent,directory,'job.sh'), 'w') as file1:
			file1.write(file_data2)

		with open(os.path.join(parent,directory,'KPOINTS'), 'w') as file2:
			file2.write(file_data3)

		with open(os.path.join(parent,directory,'INCAR'), 'w') as file3:
			file3.write(file_data4)

		with open(os.path.join(parent,directory,'POTCAR'), 'w') as file4:
			file4.write(file_data5)
	#os.chdir(os.path.join(parent,directory))
os.rename('job.sh', 'oldjob.sh')
