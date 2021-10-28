#coding: utf-8

'''

'''

def _single_lst(lst):
	import statistics
	if None in lst:return None
	retD=lst
	return retD

def _calc(lst,num):
	lst_none=[None]*(num)
	retD=lst[num:]+lst_none
	return retD

class Shift_from_after (object):
	def __init__(self,lst):
		self.data=lst
	
	def by_num(self,num):
		#print(len(self.data),'in xaShif')
		retD=_calc(self.data,num)
		#print(len(retD),'in xaShift')
		return retD

def bylst_num(lst,n):
	obj=Shift_from_after(lst)
	retD=obj.by_num(n)
	return retD

def byxd_key_num(xD,k,n):
	obj=Shift_from_after(xD[k])
	retD=obj.by_num(n)
	return retD




'''破壊的関数のため、使用しない
def shift_xDict(xd,num,keys=None):
	if keys==None:keys=[k for k in xd.keys()]
	for k in keys:
		xd[k]=_calc(xd[k],num)
	return xd
'''

if __name__ == '__main__':
	print ('main test')

	lst_a=[None,None]
	lst_b=[i for i in range(20)]
	lst=lst_a+lst_a+lst_b+lst_a+lst_b
	
	cls=Shift_from_after(lst)
	[print(i,l) for i,l in zip(lst,cls.by_num(3))]
	
	
	
	print('main end')
