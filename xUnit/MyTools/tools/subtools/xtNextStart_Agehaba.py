#coding: utf-8
import xiKeysKabuka
import xaShiftMax
import xaShift
import xcDivSub
import xcGreaterThan
'''

'''

kk=xiKeysKabuka.Keys_Kabuka()


def _nextstart(xd):
	sft_strt=xaShift.Shift_from_after(xd[kk.start])
	retD=sft_strt.by_num(1)
	return retD

def _maxHigh(xd,num):
	sm=xaShiftMax.xaShiftMax(xd[kk.high])
	retD=sm.by_num_shift_max(2,num)
	return retD

def _divsub(la,lb):
	ds=xcDivSub.DivSub(la)
	retD=ds.by_lst(lb)
	return retD


def _tf_greater_by_sikiti(lst,sikiti):
	obj_tf=xcGreaterThan.GreaterThan(lst)
	return obj_tf.by_val(sikiti)



class xtNextStart_Agehaba (object):
	def __init__(self,xd_kabu,n_max=None):
		if n_max==None:n_max=5

		self.xd_kabuka=xd_kabu
		self.lst_nextstart=_nextstart(xd_kabu)
		self.lst_sftmax=_maxHigh(xd_kabu,n_max)
		self.lst_agehaba=_divsub(self.lst_sftmax,self.lst_nextstart)
		
		self.tf_age=_tf_greater_by_sikiti(self.lst_agehaba,0.01)
		
		
	def by_num(self,num):
		self.lst_sftmax=_maxHigh(self.xd_kabuka,num)
		self.lst_agehaba=_divsub(self.lst_sftmax,self.lst_nextstart)
		return self.lst_agehaba
	
	def tf_by_sikiti(self,sikiti):
		self.tf_age=_tf_greater_by_sikiti(self.lst_agehaba,sikiti)
		return self.tf_age

		


if __name__ == '__main__':
	print ('main test')

	
	
	
	
	print('main end')
