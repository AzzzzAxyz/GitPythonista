#coding: utf-8

'''

'''

def _single_fnc(a,b):
	if a==None: return None
	if b==None: return None
	if a==b: return False
	elif a==True : return True
	else : return False

def _calc(lst_a,lst_b):
	retD=[_single_fnc(a,b) for a,b in zip(lst_a,lst_b)]
	return retD

def _calc_to_True(lst):
	before=[None] + lst[:-1]
	after_today=lst
	return _calc(after_today,before)
	

	

class TF_Henkaten (object):
	def __init__(self,lst):
		self.data=lst
	
	def to_True(self):
		return _calc_to_True(self.data)
	
	def to_False(self):
		hanten_lst=[not l for l in self.data]
		return _calc_to_True(hanten_lst)
		


if __name__ == '__main__':
	print ('main test')

	lst_a=[None,None]
	lst_b=[i for i in range(20)]
	lst=lst_a+lst_a+lst_b+lst_a+lst_b
	
	cls=TF_Henkaten(lst)
	[print(i,l) for i,l in zip(lst,cls.to_True())]
	
	tf=[0,0,0,1,0,1,1,0,0]
	cls=TF_Henkaten(tf)
	[print(i,l) for i,l in zip(tf,cls.to_True())]
	print('====:=====:====')
	[print(i,l) for i,l in zip(tf,cls.to_False())]
	print('main end')
