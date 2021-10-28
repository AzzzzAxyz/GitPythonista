#coding: utf-8

'''
TFリストと終値とかを合成して、Trueのところだけに入れる
'''

def _single_fnc(a,b):
	if a==True: return b
	else: return None

def _calc(lst_a,lst_b):
	retD=[_single_fnc(a,b) for a,b in zip(lst_a,lst_b)]
	return retD

class TF_Gousei (object):
	def __init__(self,lst):
		self.data=lst
	
	def by_val(self,val):
		lst_b=[val for i in range(len(self.data))]
		retD=_calc(self.data,lst_b)
		return retD
	
	def by_lst(self,lst_b):
		retD=_calc(self.data,lst_b)
		return retD
		


if __name__ == '__main__':
	print ('main test')

	lst_a=[None,None]
	lst_b=[i for i in range(20)]
	lst=lst_a+lst_a+lst_b+lst_a+lst_b
	
	cls=TF_Gousei(lst)
	[print(i,l) for i,l in zip(lst,cls.by_val(3))]
	
	
	
	print('main end')
