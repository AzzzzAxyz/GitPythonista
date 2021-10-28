#coding: utf-8
import xiKeysKabuka
import xtNextStart_Agehaba as xt_age
import xtNextStart_Sagehaba as xt_sage
'''

'''

kk=xiKeysKabuka.Keys_Kabuka()



class xtNS_MaxMin (object):
	def __init__(self,xd_kabu,n=None):
		if n==None:n=5
		
		age=xt_age.xtNextStart_Agehaba(xd_kabu,n)
		sage=xt_sage.xtNextStart_Sagehaba(xd_kabu,n)

		self.xd_kabuka=xd_kabu
		self.lst_nextstart=_nextstart(xd_kabu)
		self.lst_sftmax=
		self.lst_sftmin=_minLow(xd_kabu,n_min)
		self.lst_agehaba=_divsub(self.lst_sftmin,self.lst_nextstart)
		
		
	def by_num(self,num):
		self.lst_sftmin=_minLow(self.xd_kabuka,num)
		self.lst_agehaba=_divsub(self.lst_sftmin,self.lst_nextstart)
		return self.lst_agehaba


if __name__ == '__main__':
	print ('main test')

	
	
	
	
	print('main end')
