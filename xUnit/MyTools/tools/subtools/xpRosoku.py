#coding: utf-8
import matplotlib.pyplot as plt

import xDictKabuka
import xDictNearai
import xDict
import myMath



class rosoku_keys (object):
	def __init__(self):
		self.TF_in='insen_flag'
		self.TF_yo='yosen_flag'
		self.TF_dj='douji_flag'
		self.dt_in='insen_data'
		self.dt_yo='yosen_data'
		self.dt_dj='douji_data'
		self.index='x_index'
		
rk=rosoku_keys()
kk=xDictKabuka.kabuka_keys()


def _false_lst(lst):
	return [False for  l in lst]


def _kabuka_byTF(tf_lst,xd):
	xdr=xDict.dic_to_rows(xd)
	for i,l in enumerate(tf_lst):
		if l==False:
			xdr[i][kk.start]=None
			xdr[i][kk.end]=None
			xdr[i][kk.high]=None
			xdr[i][kk.low]=None
	retD=xDict.rows_to_dic(xdr)
	return retD

def _inyodj_datadict(xd):
	sabun=myMath.a_minus_b(xd[kk.end],xd[kk.start])
	xdd={}
	xdd[rk.TF_in]=_false_lst(sabun)
	xdd[rk.TF_yo]=_false_lst(sabun)
	xdd[rk.TF_dj]=_false_lst(sabun)
	for i in range(len(sabun)):
		if sabun[i]<0:	xdd[rk.TF_in][i]=True
		elif sabun[i]>0: xdd[rk.TF_yo][i]=True
		else:xdd[rk.TF_dj][i]=True
	xdd[rk.dt_in]=_kabuka_byTF(xdd[rk.TF_in],xd)	
	xdd[rk.dt_yo]=_kabuka_byTF(xdd[rk.TF_yo],xd)
	xdd[rk.dt_dj]=_kabuka_byTF(xdd[rk.TF_dj],xd)
	xdd[rk.index]=[i+1 for i in range(len(sabun))]
	return xdd


def _data_hige(xd,iyd):
	index=xd[rk.index]
	if iyd=='in':
		takane=xd[rk.dt_in][kk.high]
		yasune=xd[rk.dt_in][kk.low]
	elif iyd=='yo':
		takane=xd[rk.dt_yo][kk.high]
		yasune=xd[rk.dt_yo][kk.low]
	else:
		takane=xd[rk.dt_dj][kk.high]
		yasune=xd[rk.dt_dj][kk.low]
	ind=[i for i,l in zip(index,takane) if l!=None]
	taka=[l for l in takane if l!=None]
	yasu=[l for l in yasune if l!=None]
	return [ind,myMath.a_minus_b(taka,yasu),yasu]
	
def _data_body(xd,iyd):
	index=xd[rk.index]
	if iyd=='in':
		takane=xd[rk.dt_in][kk.start]
		yasune=xd[rk.dt_in][kk.end]
	elif iyd=='yo':
		takane=xd[rk.dt_yo][kk.end]
		yasune=xd[rk.dt_yo][kk.start]
	else:
		takane=xd[rk.dt_dj][kk.end]
		yasune=xd[rk.dt_dj][kk.start]
	ind=[i for i,l in zip(index,takane) if l!=None]
	taka=[l for l in takane if l!=None]
	yasu=[l for l in yasune if l!=None]
	return [ind,myMath.a_minus_b(taka,yasu),yasu]

def _data_tail(xd,num):
	xdr=xDict.dic_to_rows(xd)[-1*num:]
	return xDict.rows_to_dic(xdr)

def _showclose(pl):
	pl.show()
	pl.close()

def _plot_owarine(xd,num):
	ydata=[None]+xd[kk.owarine][-1*num:]
	xdata=[i for i in range(num)]
	plt.plot(ydata,marker=None)
	return plt
	
def _plot_bar_dummy(xd,num):
	hi=[0 for l in range(num)]
	lw=xd[kk.low]
	id=[i+1 for i in range(len(hi))]
	dmax=max(xd[kk.high])
	dmin=min(xd[kk.low])
	plt.bar(id,hi,bottom=hi,width=0,edgecolor='white')
	return plt

def _hige(pl,x,takane,yasune,iro):
	pl.bar(x,takane,bottom=yasune,width=0,	align='center' ,edgecolor=iro)
	return pl
	
def _body(pl,x,takane,yasune,iro):
	pl.bar(x,takane,bottom=yasune ,width=0.9,	align='center',color=iro, edgecolor=iro)
	return pl


def _plot_hige(pl,xd):
	in_d=_data_hige(xd,'in')
	yo_d=_data_hige(xd,'yo')
	dj_d=_data_hige(xd,'dj')
	pl=_hige(pl,in_d[0],in_d[1],in_d[2],'green')
	pl=_hige(pl,yo_d[0],yo_d[1],yo_d[2],'red')
	pl=_hige(pl,dj_d[0],dj_d[1],dj_d[2],'black')
	return pl

def _plot_body(pl,xd):
	in_d=_data_body(xd,'in')
	yo_d=_data_body(xd,'yo')
	dj_d=_data_body(xd,'dj')
	pl=_body(pl,in_d[0],in_d[1],in_d[2],'green')
	pl=_body(pl,yo_d[0],yo_d[1],yo_d[2],'red')
	pl=_body(pl,dj_d[0],dj_d[1],dj_d[2],'black')
	return pl

def candle_stick_plt(xd,num=None):
	if num==None:num=50
	pl=_plot_owarine(xd,num)
	data=_data_tail(xd,num)
	dt=_inyodj_datadict(data)
	pl=_plot_bar_dummy(data,num)
	pl=_plot_hige(pl,dt)
	pl=_plot_body(pl,dt)
	return pl


def candle_stick(xd,num=None):
	pl=candle_stick_plt(xd,num)
	_showclose(pl)



def plpl_CandleStick(pl,xd):
	dt=_inyodj_datadict(xd)
	#pl=_plot_bar_dummy(xd)
	pl=_plot_hige(pl,dt)
	pl=_plot_body(pl,dt)
	return pl


def pl_owarine(xd):
	num=len(xd[kk.owarine])
	ydata=[None]+xd[kk.owarine][-1*num:]
	xdata=[i for i in range(num)]
	plt.plot(ydata,marker=None)
	return plt


if __name__ == '__main__':
	print ('main test')
	
	
	
