
import numpy as np
import scipy.io as io
from glacier import glacier
from landlab import RasterModelGrid

def main():

	input_file = 'mb4_spin1.mat'
	mat = io.loadmat(input_file)
	B = mat['B']
	b_dot = mat['b_dot']
	dx = mat['dx'][0,0]
	dy = mat['dy'][0,0] 
	nx = np.int_(mat['nx'][0,0])
	ny = np.int_(mat['ny'][0,0])
	

	t_STOP = 0.1        ### 1000
	dt = 0.08333
	t = 0	

	grid = RasterModelGrid(ny,nx,dx)

	B,b_dot,S = flatten(B,b_dot)



	dictionary = {'S':S,'B':B,'b_dot':b_dot,'dt':dt,'t_STOP':t_STOP,'t':t,'dx':dx,'nx':nx,'ny':ny}
	gla = glacier.Glacier(grid,dictionary)

	gla.recursive_steps()

	S_map = gla.grid['node']['ice_elevation'] 
	B_map = gla.grid['node']['B_map'] 
	I_map = gla.grid['node']['I_map'] 
	np.savetxt('S_map.txt',S_map)
	np.savetxt('B_map.txt',B_map)
	np.savetxt('I_map.txt',I_map)

def flatten(B,b_dot):
	B = B.T.flatten()
	B[np.isnan(B)] = 0
	S = B
	b_dot = b_dot.T.flatten()
	return B,b_dot,S

if __name__ == "__main__":
	main()





