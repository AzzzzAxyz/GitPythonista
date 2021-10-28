#coding: utf-8

import matplotlib.pyplot as plt
import xcToolList as xl

'''

'''


def hist_binsN(data,bins_num):
	d_without_None=xl.remove_None(data)
	plt.hist(d_without_None,bins=bins_num)
	plt.show()
	plt.close()

def oresen(data):
	d_without_None=xl.remove_None(data)
	plt.plot(d_without_None)
	plt.show()
	plt.close()

def plot(d_x,d_y):
	
	plt.plot(d_x,d_y)
	plt.show()
	plt.close()



def scatter_plot(d_x,d_y):
	
	plt.scatter(d_x,d_y)
	plt.show()
	plt.close()




if __name__ == '__main__':
	print ('main test')
	

	
	
	print('main end')
