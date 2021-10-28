#coding: utf-8
import xDict
import xcSelectTF
import xdIOB
import xiKeysKabuka
import xdDataKabuka
import xdKabukaTyousei
import xcRandom
import matplotlib.pyplot as plt


kk=xiKeysKabuka.Keys_Kabuka()

def load_kabukadata(code):
	kabuka=xdDataKabuka.load_byCode(code)
	#kdt=xdKabukaTyousei.xKabukaTyousei(kabuka)
	kdt=xdKabukaTyousei.tyousei_xD(kabuka)
	return kdt

def dataByCode(code):
	xdk=xdKabukaTyousei.xKabukaTyousei()
	retD=xFD.loadJikeiByCode(code)
	return retD

def _teat(code):
	d=load_kabukadata(code)
	len_d=len(d[kk.date])
	random=xcRandom.lst_TF(len_d,0.2)
	tf_in=xcRandom.lst_TF(len_d,0.2)
	tf_out=xcRandom.lst_TF(len_d,0.2)
	print(len_d,sum(random),sum(random)/len_d)
	
	income=xcSelectTF.lst_select_byD_TF(d[kk.start],tf_in,0)
	outcome=xcSelectTF.lst_select_byD_TF(d[kk.start],tf_out,0)
	sumio=xdIOB.sumio_byIO(income,outcome)
	balance=xdIOB.balance_by_sumio_initial(sumio,0.1)
	
	plt.plot(sumio)
	plt.plot(balance)
	plt.show()
	plt.close()
	
	

if __name__ == '__main__':
	print ('main test')
	
	[_teat(3436) for i in range(10)]
	
	

	print('main end')
