
#1. What does model do

This model aims to simulate mountain glaciers in computational domains containing many grid nodes over century-long model periods.


#2. Running the model

Inputs
----------------------
`B`: bed elevation 

`b_dot`: mass of ice added or subtracted from each cell, unit: m w.e./yr

`dt`: time step interval, unit: years

`t_STOP`: ending time for modeling

`t`: starting time for modeling

`dx`: node spacing (dx = dy), unit: m

`nx`: number of columns of nodes

`ny`: number of rows of nodes

Outputs
----------------------
`S_map`: matrix of ice surface elevation

`H_map`: matrix of ice thickness

`mask`: masks of simulated and observed ice

How to run the model
----------------------
`glacier_example.py` is one driver example. 

Inputs are prepared and put in one dictionary. Create a grid: `grid = RasterModelGrid(nx,ny,dx)`.

Create an object of the Glacier class: `gla = glacier.Glacier(grid,dictionary)`

Run the model with `gla.recursive_steps()`

The outputs are stored in the grid attributes, and can be retrieved by

	S_map = gla.grid['node']['ice_elevation'] 

	H_map = gla.grid['node']['ice_thickness']

	I_map = gla.grid['node']['I_map']


#3. Visualizing model outputs

Plot thickness
------------------------------
	plt.figure(figsize=(8,6))

	plt.imshow(H_map)

	plt.colorbar()

	plt.savefig('H_map_{0}yrs.pdf'.format(t_STOP),dpi=300)
![thickness](images/h_map.png)

Plot DEM with glaciers 
------------------------------
	plt.figure(figsize=(8,6))

	plt.imshow(S_map)

	plt.colorbar()

	plt.savefig('S_map_{0}yrs.pdf'.format(t_STOP),dpi=300)
![DEM](images/S_map.pdf)

Plot masks of glaciers
-------------------------------
	plot_mask('I_map.txt','obs_map.txt')
![mask](images/mask.pdf)
