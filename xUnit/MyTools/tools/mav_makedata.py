#coding: utf-8
import urllib
import ixMave
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
import xDictPlot
import xGraphRosoku

import myMath

import DataHandler

kk=xDictKabuka.kabuka_keys()


'''
移動平均でグラフ描くだけで、中間データがかなり増える
移動平均
移動平均間の差分
差分を元にした、tf
tfと元のデータによる描画用データFをNoneにしているやつ


20210315
クラスによるデータ生成を考えていたけど、データ作る関数を出た瞬間にアクセスできなくなる。並列に書いている関数内では取り回しやすいが、関数を出た後はそれをオブジェクトとして取り扱うのもちょっと苦労する。
辞書データのキー名にはクラスで個別に名前定義するやり方に変更して描き直し

一つのクラスにキーを固める。いままで通りだがキーの名前は長めに、またキーの名前にパラメータの値を入れずに意味を入れる
mav3 とはつけずにmavDayShortとかつけるということ
パラメータの値は後から降るし

29210321

正解データをグラフにプロットする。関数をまずは整理



'''

kk=xDictKabuka.kabuka_keys()

def _mav(lst,para):
	#print(len(lst),para)
	return ixMave.ave_list(lst,para)

def _ijouTF(lst,para):
	sikiti_lst=[para for l in lst]
	retD=myMath.a_GreaterThan_b(lst,sikiti_lst)
	return retD

def _ijouTF_AB(lst_a,lst_b):
	retD=myMath.a_GreaterThan_b(lst_a,lst_b)
	return retD

def _sabun_AB(lst_a,lst_b):
	return myMath.a_minus_b(lst_a,lst_b)

def _divided_AB(lst_a,lst_b):
	return myMath.a_divided_b(lst_a,lst_b)
	
def _selectTF(lst_a,lst_tf):
	retD=myMath.select_TFlst(lst_a,lst_tf)
	return retD

def _andTF_AB(lst_a,lst_b):
	return myMath.truefalse_a_and_b(lst_a,lst_b)
	
def _ijouTF_divsub_AB_B(lst_a,lst_b,sikiti):
	sub=_sabun_AB(lst_a,lst_b)
	divsub=_divided_AB(sub,lst_b)
	tf=_ijouTF(divsub,sikiti)
	return tf
	
def _shiftFront(lst,n):
	return myMath.shift_to_Front(lst,n)

def _sabunShift_NN(lst,n_a,n_b):
	lst_a=_shiftFront(lst,n_a)
	lst_b=_shiftFront(lst,n_b)
	sabun=_sabun_AB(lst_a,lst_b)
	return sabun

def _ijouTF_DivSubSft_NN(lst,n_a,n_b,sikiti):
	lst_a=_shiftFront(lst,n_a)
	lst_b=_shiftFront(lst,n_b)
	tf=_ijouTF_divsub_AB_B(lst_a,lst_b,sikiti)
	return tf

def _ikaTF_DivSubSft_NN(lst,n_a,n_b,sikiti):
	lst_a=_shiftFront(lst,n_b)

def _divsub_zen(lst):
	lst_b=[None]+[l for l in lst[:-1]]
	lst_sub=_sabun_AB(lst,lst_b)
	lst_subdiv=_divided_AB(lst_sub,lst_b)
	return lst_subdiv

def _divsub_AB(lst_a,lst_b):
	sub=_sabun_AB(lst_a,lst_b)
	divsub=_divided_AB(sub,lst_b)
	return divsub



def _plot_rosoku(xd,num):
	n=num-1
	pl=xGraphRosoku.candle_stick_plt(xd,n)
	return pl
	

class para_mav (object):
	def __init__(self,kabusikicode):
		self.mavDayShort='mavDS'
		self.mavDayLong='mavDL'
		self.mavWeekShort='mavWS'
		self.mavWeekLong='mavWL'
		self.code='Code'
		
		self.para_xd={
			self.code:kabusikicode,
			self.mavDayShort:3,
			self.mavDayLong:7,
			self.mavWeekShort:15,
			self.mavWeekLong:35,
		}
		
		self.key_lst=[self.code,
			self.mavDayShort,self.mavDayLong,
			self.mavWeekShort,self.mavWeekLong,
			]

class data_mav (object):
	def __init__(self):
		self.mavDS='mavDS'
		self.mavDL='mavDL'
		self.mavWS='mavWS'
		self.mavWL='mavWL'
		
		self.sub_DSDL='sabun_DS_DL'
		self.sub_WSWL='sabun_WS_WL'
		self.divsub_DSDL='divided_subDSDL_mavDL'
		self.divsub_WSWL='divided_suvWSWL_mavWL'
		
		self.tf_DSDL_u='TF_DSDL_Up'
		self.tf_WSWL_u='TF_WSWL_Up'
		self.select_DSDL_u='owarine_DSDL_up'
		self.select_WSWL_u='owarine_WSWL_up'
		
		self.zensa_DS='zenjitu_sabun_DS'
		self.divsubzensaDS='div_zensa_DS_mavDS'
		self.tf_zensaDS_u='TF_DS_up'
		self.select_zensaDS_u='owarine_DS_up'
		
		self.tf_DSDL_zensaDS_uu='TF_DSDL_zensaDS_upup'
		self.select_DSDL_zensaDS_uu='owarine_DSDL_zensaDS_upup'
		
		self.tf_5daysUp='TF_StartUp_after5'
		self.slct_5daysUp='start_Up_afer5'
		self.tf_5daysDown='TF_StartDown_after5'
		self.slct_5daysDown='start_Down_after5'
		
		self.slct_5daysUp_divsubDSDL='start_Up_after5_divsubDSDL'
		self.slct_5daysDown_divsubDSDL='start_Down_after5_divsubDSDL'
		
		
		self.divsub_DSzen='divsub_DSzen'
		self.divsub_DLzen='divsub_DLzen'
		self.divsub_WSzen='divsub_WSzen'
		self.divsub_WLzen='divsub_WLzen'
		
		self.divsub_OpenDS='divsub_OpenDS'
		self.divsub_HighDS='divsub_HighDS'
		self.divsub_LowDS='divsub_LowDS'
		self.divsub_CloseDS='divsub_CloseDS'

dm=data_mav()
		

def make_data_byCode(code):
	#print('makedatabycode:',code)
	kd=xDictKabuka.load_byCode(code)
	xDictKabuka.xKabukaTyousei(kd)
	pr=para_mav(code)
	dm=data_mav()
	
	lst_owa=kd[kk.owarine]
	kd[dm.mavDS]=_mav(
		lst_owa,pr.para_xd[pr.mavDayShort])
	kd[dm.mavDL]=_mav(
		lst_owa,pr.para_xd[pr.mavDayLong])
	kd[dm.mavWS]=_mav(
		lst_owa,pr.para_xd[pr.mavWeekShort])
	kd[dm.mavWL]=_mav(
		lst_owa,pr.para_xd[pr.mavWeekLong])
	
	#規格化操作に近い、これで閾値を0.01とか指定できる
	kd[dm.sub_DSDL]=_sabun_AB(kd[dm.mavDS],kd[dm.mavDL])
	kd[dm.sub_WSWL]=_sabun_AB(kd[dm.mavWS],kd[dm.mavWL])
	kd[dm.divsub_DSDL]=_divided_AB(
		kd[dm.sub_DSDL],kd[dm.mavDL])
	kd[dm.divsub_WSWL]=_divided_AB(
		kd[dm.sub_WSWL],kd[dm.mavWL])		
	kd[dm.tf_DSDL_u]=_ijouTF(kd[dm.divsub_DSDL],0.001)
	kd[dm.tf_WSWL_u]=_ijouTF(kd[dm.divsub_WSWL],0.001)
	kd[dm.select_DSDL_u]=_selectTF(
		lst_owa,kd[dm.tf_DSDL_u])
	kd[dm.select_WSWL_u]=_selectTF(
		kd[dm.mavDL],kd[dm.tf_WSWL_u])
	
	kd[dm.zensa_DS]=myMath.zen_diff(kd[dm.mavDS])
	kd[dm.divsubzensaDS]=_divided_AB(
		kd[dm.zensa_DS],kd[dm.mavDL])
	kd[dm.tf_zensaDS_u]=_ijouTF(
		kd[dm.divsubzensaDS],0.001)
	kd[dm.select_zensaDS_u]=_selectTF(
		kd[dm.mavDS],kd[dm.tf_zensaDS_u])
		
	kd[dm.tf_DSDL_zensaDS_uu]=_andTF_AB(
		kd[dm.tf_DSDL_u],kd[dm.tf_zensaDS_u])
	kd[dm.select_DSDL_zensaDS_uu]=_selectTF(
		lst_owa,kd[dm.tf_DSDL_zensaDS_uu])
	
	kd[dm.tf_5daysUp]=_ijouTF_DivSubSft_NN(
		kd[kk.start],5,1,0.01)
	kd[dm.slct_5daysUp]=_selectTF(
		kd[kk.high],kd[dm.tf_5daysUp])
	
	kd[dm.tf_5daysDown]=_ijouTF_DivSubSft_NN(
		kd[kk.start],1,5,0.01)
	kd[dm.slct_5daysDown]=_selectTF(
		kd[kk.low],kd[dm.tf_5daysDown])
		
	kd[dm.slct_5daysUp_divsubDSDL]=_selectTF(
		kd[dm.divsub_DSDL],kd[dm.tf_5daysUp])
	kd[dm.slct_5daysDown_divsubDSDL]=_selectTF(
		kd[dm.divsub_DSDL],kd[dm.tf_5daysDown])
		
	kd[dm.divsub_DSzen]=_divsub_zen(kd[dm.mavDS])
	kd[dm.divsub_DLzen]=_divsub_zen(kd[dm.mavDL])
	kd[dm.divsub_WSzen]=_divsub_zen(kd[dm.mavWS])
	kd[dm.divsub_WLzen]=_divsub_zen(kd[dm.mavWL])
	
	lst_b=kd[dm.mavDS]
	kd[dm.divsub_OpenDS]=_divsub_AB(kd[kk.start],lst_b)
	kd[dm.divsub_HighDS]=_divsub_AB(kd[kk.high],lst_b)
	kd[dm.divsub_LowDS]=_divsub_AB(kd[kk.low],lst_b)
	kd[dm.divsub_CloseDS]=_divsub_AB(kd[kk.end],lst_b)
	
	return kd



def plot_test(xd,num):
	pr=para_mav('dummy')
	dm=data_mav()
	xdr=xDict.dic_to_rows(xd)[-num:]
	xd=xDict.rows_to_dic(xdr)
	
	pl=_plot_rosoku(xd,num)
	pl.plot(xd[kk.owarine],color='black')
	
	pl.plot(xd[dm.mavDS])
	pl.plot(xd[dm.mavDL])
	pl.plot(xd[dm.mavWS])
	pl.plot(xd[dm.mavWL])
	#plt.plot(xd[dm.select_DSDL_zensaDS_uu],'^',color='red')
	#plt.plot(xd[dm.select_DSDL_u],'^',color='red')
	#plt.plot(xd[dm.select_WSWL_u],'x',color='blue')
	#plt.plot(xd[dm.select_zensaDS_u],'o')
	plt.plot(xd[dm.slct_5daysUp],'^',color='red')
	plt.plot(xd[dm.slct_5daysDown],'v',color='green')
	pl.show()
	pl.close()

def pl_rosoku_mav(xd,width):
	pr=para_mav('dummy')
	dm=data_mav()
	xdr=xDict.dic_to_rows(xd)[-width:]
	xd=xDict.rows_to_dic(xdr)
	pl=_plot_rosoku(xd,width)
	pl.plot(xd[kk.owarine],color='black')
	
	pl.plot(xd[dm.mavDS])
	pl.plot(xd[dm.mavDL])
	pl.plot(xd[dm.mavWS])
	pl.plot(xd[dm.mavWL])

	return pl

def make_data_byCodelst():
	cd=DataHandler.code_dict()
	cdlst=cd['code']
	retD={}
	for c in cdlst:
		kd=make_data_byCode(c)
		retD[c]=kd
	return retD

	

def print_graph_codelst():
	cd=DataHandler.code_dict()
	cdlst=cd['code']
	retD={}
	for c in cdlst:
		print('start code: ',c)
		kd=make_data_byCode(c)
		print_graph_sequensialy(kd,0)
		retD[c]=kd
		print('+++ end +++')
	return retD

def plot_start_haba(xd,start,haba):
	xdr=xDict.dic_to_rows(xd)[:-start]
	xdn=xDict.rows_to_dic(xdr)
	pl=pl_rosoku_mav(xdn,haba)

	pl.plot(xdr[dm.slct_5daysUp],'^',color='red')
	pl.plot(xdr[dm.slct_5daysDown],'v',color='green')


def print_graph_sequensialy(
	xd,start_n=None,end_n=None,haba=None):
	if start_n==None:start_n=3
	if end_n==None:end_n=0
	if haba==None:haba=50
	xdr=xDict.dic_to_rows(xd)
	n=[i for i in range(start_n,end_n-1,-1)]
	retD=xdr
	
	for i in n:
		print('---: ',i,' :---')
		last_n=len(xdr)-i
		xdn=xDict.rows_to_dic(xdr[:last_n])
		pl=pl_rosoku_mav(xdn,haba)
		
		pl.plot(xdn[dm.slct_5daysUp][-haba:],
			'^',color='red')
		pl.plot(xdn[dm.slct_5daysDown][-haba:],
			'v',color='green')
		pl.show()
		pl.close()
		
		plt.plot(xdn[dm.mavDS][-haba:])
		plt.plot(xdn[dm.mavDL][-haba:])
		plt.plot(xdn[dm.mavWS][-haba:])
		plt.plot(xdn[dm.mavWL][-haba:])
		plt.plot(xdn[dm.slct_5daysUp][-haba:],
			'^',color='red')
		plt.plot(xdn[dm.slct_5daysDown][-haba:],
			'v',color='green')
		plt.show()
		plt.close()
	
	haba=100
	plt.plot(xdn[dm.mavDS][-haba:])
	plt.plot(xdn[dm.mavDL][-haba:])
	plt.plot(xdn[dm.mavWS][-haba:])
	plt.plot(xdn[dm.mavWL][-haba:])
	plt.plot(xdn[dm.slct_5daysUp][-haba:],
			'^',color='red')
	plt.plot(xdn[dm.slct_5daysDown][-haba:],
			'v',color='green')
	plt.show()
	plt.close()
	
	plt.ylim(-0.2,0.2)
	plt.grid()
	plt.plot(xdn[dm.divsub_DSDL][-haba:],)
	plt.plot(xdn[dm.divsub_WSWL][-haba:])
	plt.plot(xdn[dm.slct_5daysUp_divsubDSDL][-haba:],
				'^',color='red')
	plt.plot(xdn[dm.slct_5daysDown_divsubDSDL][-haba:],
			'v',color='green')
	plt.show()
	plt.close()
	
	return retD
	




if __name__ == '__main__':
	print ('main test')

	
	
	
	
	print('main end')
	


