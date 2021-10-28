#coding: utf-8

'''
xiはインターフェースとかインデックスとか
今まで作った関数とかのアダプターとか
'''

import xDictKabuka
kk=xDictKabuka.kabuka_keys()

def _single_fnc(a,b):
	if a==None: return None
	if b==None: return None
	if a==True: return True
	elif b==True: return True
	else: return False

def _calc(lst_a,lst_b):
	retD=[_single_fnc(a,b) for a,b in zip(lst_a,lst_b)]
	return retD

class Keys_Kabuka (object):
	def __init__(self):
		self.date=kk.date
		self.start=kk.start
		self.high =kk.high 
		self.low =kk.low
		self.end =kk.end
		self.owarine =kk.owarine
		self.dekidaka =kk.dekidaka
		self.kabuka_kl =kk.kabuka_kl

class Keys_rawKabuka(object):
	def __init__(self):
		self.date='raw_'+kk.date
		self.start='raw_'+kk.start
		self.high ='raw_'+kk.high
		self.low ='raw_'+kk.low
		self.end ='raw_'+kk.end
		self.owarine ='raw_'+kk.owarine
		self.dekidaka ='raw_'+kk.dekidaka
		self.kabuka_kl =[
			self.date,
			self.start,
			self.high ,
			self.low ,
			self.end ,
			self.owarine,
			self.dekidaka,
		]

if __name__ == '__main__':
	print ('main test')
	
	kkk=Keys_Kabuka()
	print(kkk.kabuka_kl,type(kkk.kabuka_kl))

	kkr=Keys_rawKabuka()
	print(kkr.date,type(kkr.date ))
	print(kkr.kabuka_kl,type(kkk.kabuka_kl))

	
	print('main end')
