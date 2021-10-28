#coding: utf-8
import xDict
import os
import xFlag
import xTime
import xFile
import xPath
import xDataFile
import matplotlib.pyplot as plt

import xDictKabuka
import xDictNearai

import myMath
import myNearai
import myMoving

import xGraphTrade
import xGraphRosoku
import ixSakataPlot


'''
20190107作成
05
値洗いはmyNearaiを使う
mDDとかmyMathを使う

データの入出力のみをこのファイルに入れる
特に株価データ


xDictKabuka にデータフォルダがあること前提の関数を書いてしまえばいらなくなる。
ファイル名の取り扱い関数二つだけの問題。


'''

'''dokuji para'''

def _fn_teikei(code,date):
	return 'data/'+str(code)+'_'+date[0:4]+'.csv'

def _filename_with_dir(code,dr=None):
	if dr==None:dr='data/'
	fn=dr+str(code)+'_kabuka.csv'
	return fn


def load_byCode(code):
	return xDataFile.load_to_xDic((_filename_with_dir(code)))
	
def kousin_byCode(code):
	xDictKabuka.kousin_code(code)
	print('___ ',code,' kousin end ___')
	
def kousin_byCodeList(cl):
	#xDictKabuka.kousin_code_lst(cl)
	[kousin_byCode(c) for c in cl]



def _plot_byCode(code):
	d=xDictKabuka.load_byCode(code)
	kk=xDictKabuka.kabuka_keys()
	print('--- ',code,' ---')
	plt.plot(d[kk.start][-40:])
	plt.plot(d[kk.end][-40:])
	plt.show()
	plt.close()
	print('--- ',code,' ---')


def _takeTogather_byTurn(lst1,lst2):
	retD=[0 for i in range(len(lst1)*2)]
	for i,l in enumerate(lst1):
		retD[i*2]=lst1[i]
		retD[i*2+1]=lst2[i]
	return retD


def _se_plot(code):
	d=xDictKabuka.load_byCode(code)
	kk=xDictKabuka.kabuka_keys()
	print('--- ',code,' ---')
	d_s=d[kk.start][-80:]
	d_e=d[kk.end][-80:]
	together_d=_takeTogather_byTurn(d_s,d_e)
	plt.plot(together_d)
	plt.show()
	plt.close()
	print('--- ',code,' ---')



	
	





'''__data save load:::__start__'''
	
	
def _test03(code_lst):
	for c in code_lst:
		_test01(c)
	print('+++ _test03 end +++')
	

def _test_dataload(c):
	d=xDataFile.load_to_xDic(_filename_with_dir(c))
	[print(k) for k in d.keys()]
	print(d['start'][-10:])

'''__data save load:::__end__'''

def code_dict():
	retD={}
	retD['code']=[2031,2032,1928,3154,3278,3436,3778,3281,4344,6630,7201,8053,8253,8591,8601,8604,8628,8963,9449,9418,9832]
	retD['name']=['HK Bull','HK Bear','sekisui','mediasHD',
	'kenedikus',
	'sumco','sakura internet',
	'GLP',
	'sourcenext','yaman','nissan','sumitomo','crediseason',
	'orix','daiwasyouken','nomura',
	'matuisyouken','invincible','mizuho','GMO','U-next','autobacks']
	
	retD['number']=[i for i in range(1,len(retD['code'])+1)]
	return retD

def _test_codedict():
	xd=code_dict()
	xDictKabuka.kousin_code_lst(xd['code'])
	for c,n in zip(xd['code'],xd['name']):
		print('++ code:',c,'  name:',n,' ++')
		xDictKabuka.graph_byCode(c)
		print('++ code:',c,'  name:',n,' ++')
	print('+++ test end +++')

def _CSV_Code_xD():
	fn='data/code_dict.csv'
	xDict.to_csv(fn,code_dict())





def _sakata_test(code,name):
	import ixSakata
	
	d=xDictKabuka.load_byCode(code)
	sk=ixSakata.sakata_keys()
	dd=ixSakata.sakata_sinne(d)
	print(code,name)
	'''
	high=dd[sk.sin_H][-50:]
	low=dd[sk.sin_L][-50:]
	ow=dd['owarine'][-50:]
	plt.plot(high)
	plt.plot(low)
	plt.plot(ow)
	plt.show()
	plt.close()
	'''
	xGraphTrade.sakata_sinne(dd,200)
	#xGraphRosoku.candle_stick(d,50)
	
	ixSakataPlot.sakata_sinne(dd,35)
	ixSakata.print_sakata_hantei(dd)
	print(ixSakata.hind(dd))
	print(code,name)



if __name__ == '__main__':
	print ('main test')
	code_dct=code_dict()
	print(code_dct)
	code_lst=code_dct['code']
	code_name=code_dct['name']
	
	
	kousin_byCodeList(code_lst)
	
	#[_se_plot(c) for c in code_lst]
	[_sakata_test(c,n) for c,n in zip(code_lst,code_name)]
	#_test02()

	

	_CSV_Code_xD()
	


	

	
	



	
	
