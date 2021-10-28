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


def _random(num):
	pass






if __name__ == '__main__':
	print ('main test')
	
	kabuka=xdDataKabuka.load_byCode(3154)
	xdKabukaTyousei.xKabukaTyousei(kabuka)
	
	
	kabuka=_test_randomorder(3154)
	kabuka_rows=xDict.dic_to_rows(kabuka)
	
	

	
	print('main end')

