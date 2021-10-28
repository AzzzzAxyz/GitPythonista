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
import xaSeikai

'''
20211014
まずは、正解データの終値プロット
上昇は△上三角、下降は▽下三角、横は四角のマーカー





'''

kk=xiKeysKabuka.Keys_Kabuka()






def load_kabukadata(code):
	kabuka=xdDataKabuka.load_byCode(code)
	kdt=xdKabukaTyousei.tyousei_xD(kabuka)
	return kdt



def _seikai_test(xd):
	n=10
	sikiti_u=0.05
	sikiti_d=-0.05
	
	dup=xaSeikai.seldup_bylsta_lstd_n_sikiti(xd[kk.start],xd[kk.end],n,sikiti_u)
	ddn=xaSeikai.selddn_bylsta_lstd_n_sikiti(xd[kk.start],xd[kk.end],n,sikiti_d)
	dyk=xaSeikai.seldyk_bylsta_lstd_n_sikitiUD(xd[kk.start],xd[kk.end],n,sikiti_u,sikiti_d)
	
	
	tfup=xaSeikai.TFup_bylst_n_sikiti(xd[kk.start],n,sikiti_u)
	tfdn=xaSeikai.TFdn_bylst_n_sikiti(xd[kk.start],n,sikiti_d)
	tfyk=xaSeikai.TFyk_bylst_n_sikitiUD(xd[kk.start],n,sikiti_u,sikiti_d)
	
	all=len(xd[kk.start])-n
	
	tfup_n=sum(xcToolList.remove_None(tfup))
	tfdn_n=sum(xcToolList.remove_None(tfdn))
	tfyk_n=sum(xcToolList.remove_None(tfyk))
	
	print(tfup_n/all)
	print(tfdn_n/all)
	print(tfyk_n/all)
	print((tfup_n+tfdn_n+tfyk_n),all)
	
	
	
	
	grph_n=100
	plt.plot(xd[kk.end][-grph_n:])
	plt.plot(dup[-grph_n:],marker='^',color='r')
	plt.plot(ddn[-grph_n:],marker='v',color='g')
	plt.plot(dyk[-grph_n:],marker='o',color='b')
	
	plt.show()
	plt.close()


def lst_plothist(lst,bin=None):
	if bin==None:bin=50
	d=xcToolList.remove_None(lst)
	plt.hist(d,bin)
	plt.show()
	plt.close()



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
	
	d=load_kabukadata(9418)
	print(xDict.dic_to_rows(d)[-3])
	_seikai_test(d)
	


	
	print('main end')
