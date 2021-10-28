#coding: utf-8
import xaMin
import xaShift

'''

'''

class xaShiftMin (object):
	def __init__(self,lst):
		self.lst_data=lst
		self.lst_shiftmin=lst
		self.n_min=5
		self.n_shift=2
		
	def by_num_shift_min(self,nshift,nmin):
		#print(len(self.lst_data))
		obj_min=xaMin.Min(self.lst_data)
		#print(len(obj_min.data),'obj_min')
		lst_min=obj_min.by_num(nmin)
		#print(len(lst_min),'lst_min')
		obj_shifted=xaShift.Shift_from_after(lst_min)
		self.lst_shiftmin=obj_shifted.by_num(nshift)
		#print(len(self.lst_shiftmin))
		return self.lst_shiftmin

def xD_Key_ShiftNum_MinNum(xD,k,nshift,nmin):
	obj=xaShiftMin(xD[k])
	retD=obj.by_num_shift_min(nshift,nmin)
	return retD

if __name__ == '__main__':
	print ('main test')

	lst_a=[None,None]
	lst_b=[i for i in range(20)]
	lst=lst_a+lst_a+lst_b+lst_a+lst_b
	print('___')
	cls=xaShiftMin(lst)
	[print(i,l) for i,l in zip(lst,cls.by_num_shift_min(2,3))]
	
	
	
	print('main end')
