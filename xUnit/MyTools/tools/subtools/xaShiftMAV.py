#coding: utf-8
import xaMAV
import xaShift

'''

'''

class xaShiftMAV (object):
	def __init__(self,lst):
		self.lst_data=lst
		self.lst_shiftmav=lst
		self.n_mav=5
		self.n_shift=2
		
	def by_num_shift_mav(self,nshift,n):
		obj_mav=xaMAV.MAV(self.lst_data)
		lst_mav=obj_mav.by_num(n)
		obj_shifted=xaShift.Shift_from_after(lst_mav)
		self.lst_shiftmav=obj_shifted.by_num(nshift)
		return self.lst_shiftmav


if __name__ == '__main__':
	print ('main test')

	lst_a=[None,None]
	lst_b=[i for i in range(20)]
	lst=lst_a+lst_a+lst_b+lst_a+lst_b
	print('___')
	cls=xaShiftMAV(lst)
	[print(i,l) for i,l in zip(lst,cls.by_num_shift_mav(2,3))]
	
	
	
	print('main end')
