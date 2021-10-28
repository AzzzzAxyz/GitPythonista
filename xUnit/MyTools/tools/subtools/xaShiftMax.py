#coding: utf-8
import xaMax 
import xaShift

'''

'''

class xaShiftMax (object):
	def __init__(self,lst):
		self.lst_data=lst
		self.lst_shiftmax=lst
		self.n_max=2
		self.n_shift=5
		
	def by_num_shift_max(self,nshift,nmax):
		obj_max=xaMax.Max(self.lst_data)
		lst_max=obj_max.by_num(nmax)
		obj_shifted=xaShift.Shift_from_after(lst_max)
		self.lst_shiftmax=obj_shifted.by_num(nshift)
		return self.lst_shiftmax

def xD_Key_ShiftNum_MaxNum(xD,k,nshift,nmax):
	obj=xaShiftMax(xD[k])
	retD=obj.by_num_shift_max(nshift,nmax)
	return retD


if __name__ == '__main__':
	print ('main test')

	lst_a=[None,None]
	lst_b=[i for i in range(20)]
	lst=lst_a+lst_a+lst_b+lst_a+lst_b
	print('___')
	cls=xaShiftMax(lst)
	[print(i,l) for i,l in zip(lst,cls.by_num_shift_max(2,3))]
	
	
	
	print('main end')
