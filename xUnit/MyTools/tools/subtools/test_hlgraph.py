#coding: utf-8
import matplotlib.pyplot as plt

import xiKeysKabuka
import xtNextStart_Agehaba as agehaba
import xtNextStart_Sagehaba as sagehaba
import xdDataKabuka
import numpy as np
import xcToolList as xl
import xdKabukaTyousei
import xpPlot as xpp
import xcStatistics as xcs

import xDict
import xcRandom
import xaShift
import xiKeysOrder
import xbMax
import xaMax
import xbMin
import xcDivSub
import xaShiftMax
import xaShiftMin
import xcToolList

import xpRosoku

'''
20211005

- 正解データのグラフ表示、N日後に上昇は△、下降は▽、横ばいは□、データがまだないところは◯と言うグラフ
- グラフの描画とデータ。
- データは、1日後のデータをまずは持ってくる、1＋N日後のデータを持ってくる。
- 1＋N日後のデータを1日後のデータで割る
- 閾値はxパーセントとする。上がx、下がyとする。
- 割った値がx閾値を超えて入れば上昇、y閾値を下回ると下降、それ以外は横ばい。それぞれのTF列を作る
- グラフを書く列を決める。グラフはとりあえず折れ線
- TF列とデータ列を合成する。穴埋めはNONE
- グラフ描画する
- とりあえずここまでか？

'''

kk=xiKeysKabuka.Keys_Kabuka()
kos=xiKeysOrder.Keys_OrderSig()


def load_kabukadata(code):
	kabuka=xdDataKabuka.load_byCode(code)
	#kdt=xdKabukaTyousei.xKabukaTyousei(kabuka)
	kdt=xdKabukaTyousei.tyousei_xD(kabuka)
	return kdt

def _shiftStart(xD,n):
	retD=xaShift.xD_Key_shiftA_byNum(xD,kk.start,n)
	return retD

def _a_divsub_b(xD,keya,keyb):
	retD=xcDivSub.xD_aK_divisub_bK(xD,keya,keyb)
	return retD

class keys_This (object):
	def __init__(self):
		self.an_St='after_start_n'
		self.anr_St='after_reg_start_n'
		self.reg_den='reg_denominater'
		
		self.tf_up='TF_Up'
		self.tf_dn='TF_Down'
		self.tf_yk='TF_Yoko'
		self.tf_mt='TF_Mitei'
		
		self.pd_up='plotData_Up'
		self.pd_dn='plotData_Down'
		self.pd_yk='plotData_Yoko'
		self.pd_mt='plotData_Mitei'
		
		
	def lst(self):
		return 'lst'
		
kt=keys_This()

def _hantei_Up(xd,sikiti):
	retD=[False for i in xd[kt.anr_St]]
	for i,l in enumerate(xd[kt.anr_St]):
		if l>sikiti:retD[i]=True
	return retD

def _hantei_Dn(xd,sikiti):
	retD=[False for i in xd[kt.anr_St]]
	for i,l in enumerate(xd[kt.anr_St]):
		if l<sikiti:retD[i]=True
	return retD

		


def _TF_byxd_sikitiUD(xd,sikitiUp,sikitiDn):
	


def xd_by_xd_num(xd,n):
	retD=xDict.copy(xd)
	retD[kt.reg_den]=_shiftStart(retD,1)
	retD[kt.an_St]=_shiftStart(retD,n)
	retD[kt.anr_St]=_a_divsub_b(retD,kt.an_St,kt.reg_den)
	
	
	return retD
	



def _plt_plot_lst_mak_col(pl,lst,mak,col):
	pl.plot(lst,marker=mak,color=col,markersize=10)
	return pl


def _xd_plot_key_num(xD,k,num=None):
	if num==None:num=50
	d=xD[k]
	plt.plot(d[-num:])
	pl=_plt_plot_lst_mak_col(plt,d[-num:],'^','b')
	pl.show()
	pl.close()



def _test_loaddata(code,num):

	data=load_kabukadata(code)
	xdd=xd_by_xd_num(data,num)	
	
	print(num)
	print(xdd.keys())

	return xdd
	

def xd_plothist(xD,k,bin=None):
	if bin==None:bin=50
	d=xcToolList.remove_None(xD[k])
	plt.hist(d,bin)
	plt.show()
	plt.close()



if __name__ == '__main__':
	print ('main test')
	
	xd=_test_loaddata(3154,5)
	
	xd_plothist(xd,kt.anr_St)
	
	
	
	

	

	
	print('main end')
