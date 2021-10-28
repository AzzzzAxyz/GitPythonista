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
20210823
上でも下でも、2%を取る時の勝率を出したい
どのくらいのスパンが必要か見るのに日数は可変
次の日の始値を基準とする
次の次の日を1日目と数える。
そこからn日を抜き出して、高値のMAX、安値のminimumを計算する
Maxとminimumは次の日の始値で割って規格化する。




'''

kk=xiKeysKabuka.Keys_Kabuka()
kos=xiKeysOrder.Keys_OrderSig()


def _random(num):
	pass

def load_kabukadata(code):
	kabuka=xdDataKabuka.load_byCode(code)
	#kdt=xdKabukaTyousei.xKabukaTyousei(kabuka)
	kdt=xdKabukaTyousei.tyousei_xD(kabuka)
	return kdt

def _shiftMax(xD,k,ns,nm):
	retD=xaShiftMax.xD_Key_ShiftNum_MaxNum(xD,k,ns,nm)
	return retD

def _shiftMin(xD,k,ns,nm):
	retD=xaShiftMin.xD_Key_ShiftNum_MinNum(xD,k,ns,nm)
	return retD

def _a_divsub_b(xD,keya,keyb):
	retD=xcDivSub.byxd_keya_keyb(xD,keya,keyb)
	return retD


class keys_This (object):
	def __init__(self):
		self.an_H='after_High_n'
		self.an_L='after_Low_n'
		self.an_maxH='after_maxH_n'
		self.an_minL='after_minL_n'
		self.anr_maxH='after_reg_maxH_n'
		self.anr_minL='after_reg_minL_n'
		self.reg_den='reg_denominater'
	def lst(self):
		return 'lst'

khl=keys_This()

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
	data[khl.an_maxH]=_shiftMax(data,kk.high,2,num)
	data[khl.an_minL]=_shiftMin(data,kk.high,2,num)
	
	data[khl.anr_maxH]=_a_divsub_b(data,khl.an_maxH,kk.start)
	data[khl.anr_minL]=_a_divsub_b(data,khl.an_minL,kk.start)
	
	print(num)
	plt.plot(data[khl.anr_maxH][-50:])
	plt.plot(data[khl.anr_minL][-50:])
	plt.show()
	plt.close()
	xd_plothist(data,khl.anr_maxH)
	xd_plothist(data,khl.anr_minL)
	
	_xd_plot_key_num(data,kk.start,80)
	_xd_plot_key_num(data,kk.end,80)
	
	xpRosoku.candle_stick(data,50)
	
	print(num)
	
	
	
	return data
	
	



def xd_plothist(xD,k,bin=None):
	if bin==None:bin=50
	d=xcToolList.remove_None(xD[k])
	plt.hist(d,bin)
	plt.show()
	plt.close()



if __name__ == '__main__':
	print ('main test')
	
	kabuka=xdDataKabuka.load_byCode(3154)
	kdt=xdKabukaTyousei.xKabukaTyousei(kabuka)
	
	
	
	kabuka_rows=xDict.dic_to_rows(kdt)
	#print(kabuka_rows[-3:])
	
	[_test_loaddata(3154,n) for n in range(5,15,10)]
	#print(d[khl.an_minL])
	#[print(k,':',len(d[k])) for k in d.keys()]
	#rd=xDict.dic_to_rows(d)
	#print(rd[-15:-14])
	

	
	print('main end')
