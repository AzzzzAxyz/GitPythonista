#coding: utf-8
import xDict
import xiKeysKabuka
import xaShift
import xcDivSub


'''
正解データを作る
アフターなので、N日後の値
基準は次の日の始値
N日間のMax値との比、N日後との比
まずはdivsubを計算する。



'''

kk=xiKeysKabuka.Keys_Kabuka()

def _lst_select_byLstTF(lstD,lstTF,anaume=None):
	retD=[anaume for i in lstTF]
	for i in range(len(retD)):
		if lstTF[i]==True:retD[i]=lstD[i]
	return retD
	

def _lst_select_byD_TF(lstD,lstTF,anaume=None):
	return _lst_select_byLstTF(lstD,lstTF,anaume)

def divsub_bylst_n(lst,n):
	lst_after=xaShift.bylst_num(lst,n)
	ds=xcDivSub.by_lsta_lstb(lst_after,lst)
	return ds

def divsub_byxd_key_n(xd,k,n):
	lst_origin=xd[k]
	#lst_after=xaShift.byxd_key_num(xd,k,n)
	lst_after=divsub_bylst_n(xd[k],n)
	ds=xcDivSub.by_lsta_lstb(lst_after,lst_origin)
	return ds


def TFup_bylstdivsub_sikiti(lst_ds,sikiti):
	retD=[False for i in range(len(lst_ds))]
	for i,l in enumerate(lst_ds):
		if l==None:retD[i]=None
		elif l>sikiti:retD[i]=True
	return retD

def TFup_bylst_n_sikiti(lst,n,sikiti):
	lst_ds=divsub_bylst_n(lst,n)
	retD=TFup_bylstdivsub_sikiti(lst_ds,sikiti)
	return retD


def TFdn_bylstdivsub_sikiti(lst_ds,sikiti):
	retD=[False for i in range(len(lst_ds))]
	for i,l in enumerate(lst_ds):
		if l==None:retD[i]=None
		elif l<sikiti:retD[i]=True
	return retD

def TFdn_bylst_n_sikiti(lst,n,sikiti):
	lst_ds=divsub_bylst_n(lst,n)
	retD=TFdn_bylstdivsub_sikiti(lst_ds,sikiti)
	return retD


def TFyk_bylstdivsub_sikitiUD(lst_ds,siki_u,siki_d):
	tf_u=TFup_bylstdivsub_sikiti(lst_ds,siki_u)
	tf_d=TFdn_bylstdivsub_sikiti(lst_ds,siki_d)
	retD=[False for i in range(len(tf_u))]
	for i,l in enumerate(tf_u):
		if tf_u[i]==None:retD[i]=None
		else:
			tf_add=tf_u[i]+tf_d[i]
			if tf_add==False:retD[i]=True
	return retD

def TFyk_bylst_n_sikitiUD(lst,n,sk_u,sk_d):
	ds=divsub_bylst_n(lst,n)
	retD=TFyk_bylstdivsub_sikitiUD(ds,sk_u,sk_d)
	return retD


def TFup_byxd_n_sikiti(xd,n,sikiti):
	retD=TFup_bylst_n_sikiti(xd[kk.start],n,sikiti)
	return retD			

def TFdn_byxd_n_sikiti(xd,n,sikiti):
	retD=TFdn_bylst_n_sikiti(xd[kk.start],n,sikiti)
	return retD

def TFyk_byxd_n_sikitiUD(xd,n,siki_u,siki_d):
	retD=TFyk_bylst_n_sikitiUD(xd[kk.start],n,siki_u,siki_d)
	return retD


def seldup_bylsta_lstd_n_sikiti(lst,lstd,n,sikiti):
	lstTF=TFup_bylst_n_sikiti(lst,n,sikiti)
	retD=_lst_select_byLstTF(lstd,lstTF)
	return retD
	
def selddn_bylsta_lstd_n_sikiti(lst,lstd,n,sikiti):
	lstTF=TFdn_bylst_n_sikiti(lst,n,sikiti)
	retD=_lst_select_byLstTF(lstd,lstTF)
	return retD
	
def seldyk_bylsta_lstd_n_sikitiUD(lst,lstd,n,su,sd):
	lstTF=TFyk_bylst_n_sikitiUD(lst,n,su,sd)
	retD=_lst_select_byLstTF(lstd,lstTF)
	return retD


def _test():
	lstD=[l for l in range(5)]
	lstTF=[False,True,False,True,True]
	sel=_lst_select_byD_TF(lstD,lstTF)
	print(sel)




def _test2():
	n=3
	d=[i for i in range(1,10)]
	xd={kk.start:d}
	ds=divsub_byxd_key_n(xd,kk.start,n)
	tflu=TFup_byxd_n_sikiti(xd,n,1.1)
	tfld=TFdn_byxd_n_sikiti(xd,n,0.7)
	tfyk=TFyk_byxd_n_sikitiUD(xd,n,1.1,0.7)
	
	[print(tflu[i],tfld[i],tfyk[i],ds[i]) for i,l in enumerate(ds)]
	pass







if __name__ == '__main__':
	print ('main test')
	
	_test2()

	print('main end')
