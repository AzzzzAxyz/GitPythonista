#coding: utf-8
import xiKeysOrder


kord=xiKeysOrder.Keys_ContractOrder()
klog=xiKeysOrder.Keys_KingakuLog()

def _newKingakuLog(code):
	retD={k:None for k in klog.lst_keys}
	retD[klog.code]=code
	return retD


class Kingaku (object):
	def __init__(self,cont_ord):
		self.klog=_newKingakuLog(code)
		

	


if __name__ == '__main__':
	print ('main test')
	
	
	
	
	print('main end')
