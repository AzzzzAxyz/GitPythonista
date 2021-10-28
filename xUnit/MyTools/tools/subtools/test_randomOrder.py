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

'''

'''

kk=xiKeysKabuka.Keys_Kabuka()
kos=xiKeysOrder.Keys_OrderSig()


def _randomTF(num):
	pass



def _kabuka_order(xd_kabuka,xd_sig):
	pass
	




def _test_randomorder(code):
	
	kabuka=xdDataKabuka.load_byCode(3154)
	xdKabukaTyousei.xKabukaTyousei(kabuka)
	kabuka_lst=xDict.dic_to_rows(kabuka)
	rdmB=xcRandom.RandomTF(len(kabuka_lst),0.4)
	rdmS=xcRandom.RandomTF(len(kabuka_lst),0.2)
	
	kabuka_shift=xaShift.shift_xDict(kabuka,10)
	kabuka[kos.date_next]= kabuka_shift[kk.date]
	
	return kabuka


if __name__ == '__main__':
	print ('main test')
	
	kabuka=xdDataKabuka.load_byCode(3154)
	xdKabukaTyousei.xKabukaTyousei(kabuka)
	
	
	kabuka=_test_randomorder(3154)
	kabuka_rows=xDict.dic_to_rows(kabuka)
	print(kabuka_rows[:2])
	
	[print(l[kk.date],l[kos.date_next])   for l in kabuka_rows[:10]]
	
	
	

	
	print('main end')


