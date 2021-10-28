#coding: utf-8
import xDict

'''
インプット、アウトプット、インプットアウトプットの合計、その履歴のBalance この四つの要素で抽象化したもの。
終始計算とかの基本はこれにはめて仕舞えば楽になるように
インプットとアウトプットは正の数を入力する
合計はインプットーアウトプットで計算する
Balanceは初期値を取ることもある。計算は一つ前のBalance＋合計
データ型はxDict
Rowでのデータ追加がしたくなる。クラスにはそういう関数ただの関数でもありか、、、
'''

def _isequal_len(lst_a,lst_b):
	len_a=len(lst_a)
	len_b=len(lst_b)
	if len_a==len_b:return True
	else:False


def _sum_by_inout(lst_a,lst_b):
	retD=[a-b for a,b in zip(lst_a,lst_b)]
	return retD

def _balance_by_sum(lst,balance_ini=None):
	if balance_ini==None:balance_ini=0
	retD=[0 for i in range(len(lst))]
	retD[0]=balance_ini+lst[0]
	for i,l in enumerate(lst[1:]):
		retD[i+1]= retD[i]+l
	return retD
	

class keys_IOB (object):
	def __init__(self):
		self.income='In'
		self.outcome='Out'
		self.sumio='SumInOUT'
		self.balance='Balance'
		
		self.key_lst=[
			self.income,self.outcome,
			self.sumio,self.balance]

class IOB (object):
	def __init__(self,lst):
		pass


def sumio_byIO(l_in,l_out):
	retD=[a-b for a,b in zip(l_in,l_out)]
	return retD

def balance_by_sumio_initial(lst_sum,ini):
	retD=[0 for l in lst_sum]
	retD[0]=ini+lst_sum[0]
	for i,l in enumerate(lst_sum[1:]):
		retD[i+1]=retD[i]+l
	return retD
	
def balance_byIO(lst_in,lst_out,ini=None):
	if ini==0 : ini=0
	sum=sumio_byIO(lst_in,lst_out)
	retD=balance_by_sumio_initial(sum,ini)
	return retD
	

def newRowTemplate():
	kk=keys_IOB()
	retD={k:0 for k in kk}
	return retD


def xD_byRowIOB(xD,row):
	kk=keys_IOB()
	xdr=xDict.dic_to_rows(xD)
	previousBalance=xdr[-1][keys_IOB.balance]
	sumio=row[kesys_IOB.income]-row[kesys_IOB.outcome]
	newBalance=previousBalance+sumio
	newRow=newRowTemplate
	newRow[kk.income]=row[kk.income]
	newRow[kk.outcome]=row[kk.outcome]
	newRow[kk.isumio]=sumio
	newRow[kk.balance]=newBalance
	xdr.add(newRow)
	retD=xDict.rows_to_dic
	return retD


def print_lists(ll):
	#これってやろうとしていることはRowにして要素をプリントするだけ	
	#list no tenti
	row_num=len(ll)
	rows=[0 for i in range(len(ll[0]))]
	for i in range(len(ll[0])):
		rows[i]=[ll[i][n] for n in range(row_num)]
	[print(l) for l in rows]
		
				

def xD_IOB_byIOTF(d_in,d_out,tf_in,tf_out,init=None):
	import xcSelectTF.lst_select_byD_TF as selectlst
	kio=keys_IOB()
	retD={}
	retD[kio.income]=selectlst(d_in,tf_in,0)
	retD[kio.outcome]=selectlst(d_out,tf_out,0)
	retD[kio.sumio]=sumio_byIO(income,outcome)
	retD[kio.balance]=balance_by_sumio_initial(sumio,0)
	return retD

def xD_byxD_IOTF(xd,inTF,outTF,inKey=None,outKey=None):
	import xiKeysKabuka
	import xcSelectTF.lst_select_byD_TF as selectlst
	kk=xiKeysKabuka.Keys_Kabuka()
	kio=keys_IOB()
	if inKey==None:inKey=kk.start
	if outKey==None:outKey=kk.start
	
	retD={}
	retD[kio.income]=selectlst(xd[inKey],xd[inTF],0)
	retD[kio.outcome]=selectlst(xd[outKey],xd[outTF],0)
	retD[kio.sumio]=sumio_byIO(income,outcome)
	retD[kio.balance]=balance_by_sumio_initial(sumio,0)
	return retD
	
	


def _test():
	num=6
	balance_ini=3
	l_in=[2*x for x in range(num)]
	l_out=[x for x in range(num)]
	sum_io=sumio_byIO(l_in,l_out)
	bal=balance_by_sumio_initial(sum_io,balance_ini)
	[print(k,l) for k,l in zip(l_in,l_out)]
	print('__')
	[print(k,l) for k,l in zip(sum_io,bal)]




if __name__ == '__main__':
	print ('main test')
	
	_test()


	
	
	print('main end')
