#coding: utf-8
import xDict
import xdIOB
import xcSelectTF
import xdKabukaTyousei
import xiKeysKabuka

import xiKeysOrder

import matplotlib.pyplot as plt

'''
どうにか、検証して結果という流れを簡単にできないか？
IOBを使えばいけるはず



'''


kk=xiKeysKabuka.Keys_Kabuka()
kos=xiKeysOrder.Keys_Order()
kib=xdIOB.keys_IOB()


def load_kabukadata(code):
	import xdDataKabuka
	kabuka=xdDataKabuka.load_byCode(code)
	kdt=xdKabukaTyousei.tyousei_xD(kabuka)
	return kdt


def signalB_bylst_n(lst,n):
	retD=[False for l in lst]
	for i,l in enumerate(lst):
		if i%n==0:retD[i]=True
	return retD

def signalS_bylst_n(lst,n):
	retD=[False for l in lst]
	for i,l in enumerate(lst):
		if i%n==0:retD[i]=True
	return retD



def IOB_bylst_sigBS(lst,sigB,sigS):
	
	lst_i=xcSelectTF.lst_select_byD_TF(lst,sigB,0)
	lst_o=xcSelectTF.lst_select_byD_TF(lst,sigS,0)
	
	print(lst_i[:10])
	print(lst_o[:10])
	
	
	sumio=xdIOB.sumio_byIO(lst_i,lst_o)
	balance=xdIOB.balance_by_sumio_initial(sumio,1000)
	xd={
		kib.income:lst_i,
		kib.outcome:lst_o,
		kib.sumio:sumio,
		kib.balance:balance,
	}
	return xd



def test(code):
	d=load_kabukadata(code)
	sb=signalB_bylst_n(d[kk.start],3)
	ss=signalS_bylst_n(d[kk.start],4)
	print(sb[:10])
	print(ss[:10])
	
	ibd=IOB_bylst_sigBS(d[kk.start],sb,ss)
	r_ibd=xDict.dic_to_rows(ibd)
	print(r_ibd[:10])
	
	plt.plot(ibd[kib.sumio][:50])
	plt.show()
	plt.close()
	
	plt.plot(ibd[kib.balance][:100])
	plt.show()
	plt.close()


if __name__ == '__main__':
	print('main test')
	
	
	
	test(3154)

	
	
	
	
	
	
	
	
	
	
	
	
	
