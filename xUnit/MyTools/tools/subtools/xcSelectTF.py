#coding: utf-8
import xDict


'''
TFリストとデータのリストから、データを選択する
Tはデータを入れる
Fは指定しなければnoneで埋める



'''


def _lst_select_byLstTF(lstD,lstTF,anaume=None):
	retD=[anaume for i in lstTF]
	for i in range(len(retD)):
		if lstTF[i]==True:retD[i]=lstD[i]
	return retD
	

def lst_select_byD_TF(lstD,lstTF,anaume=None):
	return _lst_select_byLstTF(lstD,lstTF,anaume)

class syugo (object):
	def __init__(self,x):
		self.x=x
	
	def mtd(self):
		
		retD='return'
		return retD


def _test():
	lstD=[l for l in range(5)]
	lstTF=[False,True,False,True,True]
	sel=lst_select_byD_TF(lstD,lstTF)
	print(sel)
	
	
	
	pass







if __name__ == '__main__':
	print ('main test')
	
	_test()

	print('main end')
