#coding: utf-8

'''

'''

def _single_fnc(a,b):
	if a==None: return None
	if b==None: return None
	if a==True:
		if b==True:return True
		else: return False
	else:return False

def _calc(lst_a,lst_b):
	retD=[_single_fnc(a,b) for a,b in zip(lst_a,lst_b)]
	return retD

class TF_And (object):
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
	
	cls=TF_And(lst)
	[print(i,l) for i,l in zip(lst,cls.by_val(1))]
	
	
	
	print('main end')
