#coding: utf-8

'''
始値の次の日からの比率を取る
・一つ前にシフトする
・MaxとMinを作る　期間はn
リスト同士で(Max -始値)/始値、minimum側も同様に
閾値で切ってTF列を作る

あー、divsubMaxMinて言う名前で作っておくか？


'''

import xcDivSub

def _calc(lst_a,lst_b):
	retD=[_single_fnc(a,b) for a,b in zip(lst_a,lst_b)]
	return retD

class  divsubMaxMin (object):
	def __init__(self,lst):
		self.data=lst
		self.data_max=lst
		self.data_min=lst
		self.divsub_max_lst=self.calc_divsub_max()
		self.divsub_min_lst
		self.tf_max
		self.tf_min
	
	
	def calc_divsub_max(self):
		
		ds=xcDivSub.DivSub(self.lst)
		d_max=ds.by_lst(self.data_max)
		return 
	
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
