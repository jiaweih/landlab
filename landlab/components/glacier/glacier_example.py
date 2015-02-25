
import numpy as np
import scipy.io as io
from glacier import glacier

def main():
	# is_grid = True
	# print is_grid

	if 1:
		input_file = 'mb4_spin1.mat'
		mat = io.loadmat(input_file)
		B = mat['B']
		b_dot = mat['b_dot']
		dx = mat['dx'][0,0]
		dy = mat['dy'][0,0] 
		nx = np.int_(mat['nx'][0,0])
		ny = np.int_(mat['ny'][0,0])
	else:
		print 'not reading'


	t_STOP = 0.1        ### 1000
	dt_SAVE = 5*t_STOP
	dt = 0.08333
	
	B = B.T.flatten()
	B[np.isnan(B)] = 0
	S = B
	b_dot = b_dot.T.flatten()
	t = 0
	dictionary = {'S':S,'B':B,'b_dot':b_dot,'dt':dt,'t_STOP':t_STOP,'t':t,'dx':dx,'nx':nx,'ny':ny}
	gla = glacier.Glacier(dictionary)

	gla.initialize()
	gla.recursive_steps()

if __name__ == "__main__":
	main()





