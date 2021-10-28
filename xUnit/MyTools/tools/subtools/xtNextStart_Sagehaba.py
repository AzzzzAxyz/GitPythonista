#coding: utf-8
import xiKeysKabuka
import xaShiftMin
import xaShift
import xcDivSub
'''

'''

kk=xiKeysKabuka.Keys_Kabuka()


def _nextstart(xd):
	sft_strt=xaShift.Shift_from_after(xd[kk.start])
	retD=sft_strt.by_num(1)
	return retD

def _minLow(xd,num):
	sm=xaShiftMin.xaShiftMin(xd[kk.low])
	retD=sm.by_num_shift_min(2,num)
	return retD

def _divsub(la,lb):
	ds=xcDivSub.DivSub(la)
	retD=ds.by_lst(lb)
	return retD




class xtNextStart_Sagehaba (object):
	def __init__(self,xd_kabu,n_min=None):
		if n_min==None:n_min=5

		self.xd_kabuka=xd_kabu
		self.lst_nextstart=_nextstart(xd_kabu)
		self.lst_sftmin=_minLow(xd_kabu,n_min)
		self.lst_agehaba=_divsub(self.lst_sftmin,self.lst_nextstart)
		
		
	def by_num(self,num):
		self.lst_sftmin=_minLow(self.xd_kabuka,num)
		self.lst_agehaba=_divsub(self.lst_sftmin,self.lst_nextstart)
		return self.lst_agehaba


if __name__ == '__main__':
	print ('main test')

	
	
	
	
	print('main end')
