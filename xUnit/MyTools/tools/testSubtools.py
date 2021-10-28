#coding: utf-8

import subtools.xbMax as xbmax





'''

'''



if __name__ == '__main__':
	print ('main test')

	lst_a=[None,None]
	lst_b=[i for i in range(20)]
	lst=lst_a+lst_a+lst_b+lst_a+lst_b
	
	cls=xbmax.Max(lst)
	[print(i,l) for i,l in zip(lst,cls.by_num(3))]
	
	
	
	print('main end')
