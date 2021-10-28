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


kk=xDictKabuka.kabuka_keys()


'''

'''


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


if __name__ == '__main__':
	print ('main test')

	
	
	
	
	print('main end')
	

