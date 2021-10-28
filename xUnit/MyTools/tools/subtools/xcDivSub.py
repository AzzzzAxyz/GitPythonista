#coding: utf-8

'''

'''

def _single_fnc(a,b):
	if a==None: return None
	if b==None: return None
	retD=(a-b)/b
	return retD


def _calc(lst_a,lst_b):
	retD=[_single_fnc(a,b) for a,b in zip(lst_a,lst_b)]
	return retD

class DivSub (object):
	def __init__(self,lst):
		self.data=lst
	
	def by_val(self,val):
		lst_b=[val for i in range(len(self.data))]
		retD=_calc(self.data,lst_b)
		return retD
	
	def by_lst(self,lst_b):
		retD=_calc(self.data,lst_b)
		return retD
		
class DivSubZen (object):
	def __init__(self,lst):
		obj_divsub=DivSub(lst)
		lst_zen= [None]+lst[:-1]
		self.data=obj_divsub.by_lst(lst_zen)
		
	def by_lst(self):
		retD=_calc(self.data,lst_b)
		return retD

def divsubzen_n(lst,n):
	obj_divsub=DivSub(lst)
	lst_zen= [None]*n +lst[:-n]
	retD=obj_divsub.by_lst(lst_zen)
	return retD
		
def divsubzen(lst):
	return divsubzen_n(lst,1)
	

def byxd_keya_keyb(xD,keya,keyb):
	lst_a=xD[keya]
	lst_b=xD[keyb]
	obj=DivSub(lst_a)
	retD=obj.by_lst(lst_b)
	return retD

def by_lsta_lstb(lst_a,lst_b):
	obj=DivSub(lst_a)
	retD=obj.by_lst(lst_b)
	return retD


def xD_aK_divsub_bK(xd,ak,bk):
	return byxd_keya_keyb(xd,ak,bk)
	




def _test():
	

	lst_a=[None,None]
	lst_b=[i for i in range(1,20)]
	lst=lst_a+lst_a+lst_b+lst_a+lst_b
	
	cls=DivSub(lst)
	[print(i,l) for i,l in zip(lst,cls.by_val(3))]
	print('ffffffffff')
	zen=divsubzen_n(lst_b,1)
	[print(i,l) for i,l in  zip(lst_b,zen)]
	
	
	



if __name__ == '__main__':
	print ('main test')
	
	_test()


	
	
	print('main end')
