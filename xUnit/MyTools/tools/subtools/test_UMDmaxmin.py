#coding: utf-8
import xcToolList as xl
import xaShiftMAV
import xaShiftMax
import xaShiftMin
import xiKeysKabuka
import xdDataKabuka
import xdKabukaTyousei

'''

'''
kk=xiKeysKabuka.Keys_Kabuka()



class maxminmav (object):
	def __init__(self,xd_kabuka,n=None):
		if n==None:n=10
		
	






if __name__ == '__main__':
	print ('main test')
	
	
	kabuka=xdDataKabuka.load_byCode(3154)
	xdKabukaTyousei.xKabukaTyousei(kabuka)
	print(kabuka.keys())
	
	
	print('main end')
