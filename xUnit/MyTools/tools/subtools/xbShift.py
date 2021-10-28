#coding: utf-8

'''

'''

def _single_lst(lst):
	if None in lst:return None
	retD=lst
	return retD

def _calc(lst,num):
	lst_none=[None]*(num)
	retD=lst_none+lst[:-num]
	return retD

class Shift_from_before (object):
	def __init__(self,lst):
		self.data=lst
	
	def by_num(self,num):
		retD=_calc(self.data,num)
		return retD


def xD_Key_shiftB_byNum(xD,K,n):
	obj=Shift_from_before(xD[k])
	retD=obj.by_num(n)
	return retD




if __name__ == '__main__':
	print ('main test')

	lst_a=[None,None]
	lst_b=[i for i in range(20)]
	lst=lst_a+lst_a+lst_b+lst_a+lst_b
	
	cls=Shift_from_before(lst)
	[print(i,l) for i,l in zip(lst,cls.by_num(3))]
	
	
	
	print('main end')
