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
import xdIOB


'''
20211024
とにかくIOBと組み合わせて、収支を作ってみる雛形


'''

kk=xiKeysKabuka.Keys_Kabuka()


def _random(num):
	pass

def load_kabukadata(code):
	kabuka=xdDataKabuka.load_byCode(code)
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




def _test_loaddata(code,num):

	data=load_kabukadata(code)

	print(code,num)
	
	
	
	return data
	
	



def lst_plothist(lst,bin=None):
	if bin==None:bin=50
	d=xcToolList.remove_None(lst)
	plt.hist(d,bin)
	plt.show()
	plt.close()


if __name__ == '__main__':
	print ('main test')
	
	
	_test_loaddata(3154,n)
	

	
	print('main end')
