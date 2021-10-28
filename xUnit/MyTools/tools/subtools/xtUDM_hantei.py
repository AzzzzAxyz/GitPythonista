#coding: utf-8
import xcToolList as xl
import xaShiftMAV
import xaShiftMax
import xaShiftMin
import xiKeysKabuka
import xdDataKabuka
import xdKabukaTyousei
import xcToolList as xct
import xpPlot as xpp
import xpRosoku

import xcGreaterThan as xcgt


'''

'''
kk=xiKeysKabuka.Keys_Kabuka()



class maxminmav (object):
	def __init__(self,xd_kabuka,n=None):
		if n==None:n=5
		
		obj_smax=xaShiftMax.xaShiftMax(xd_kabuka[kk.high])
		obj_smin=xaShiftMin.xaShiftMin(xd_kabuka[kk.low])
		obj_save=xaShiftMAV.xaShiftMAV(xd_kabuka[kk.end])
		lst_smax=obj_smax.by_num_shift_max(1,n)
		lst_smin=obj_smin.by_num_shift_min(1,n)
		lst_save=obj_save.by_num_shift_mav(1,n)
		
		self.s_max=lst_smax
		self.s_min=lst_smin
		self.s_ave=lst_save
		
		haba_maxmin=xct.sabun(lst_smax,lst_smin)
		maxmin_ave=xct.divide(haba_maxmin,lst_save)
		maxmin_min=xct.divide(haba_maxmin,lst_smin)
		sa_maxmin_min_ave=xct.sabun(maxmin_min,maxmin_ave)
	
		xpp.scatter_plot(haba_maxmin,maxmin_ave)
		xpp.scatter_plot(haba_maxmin,maxmin_min)
		xpp.scatter_plot(maxmin_ave,maxmin_min)
		xpp.hist_binsN(maxmin_min,60)
		xpp.oresen(sa_maxmin_min_ave)
		
		print(maxmin_ave[-(n+10):-n])
		
		obj_tf_mm=xcgt.GreaterThan(maxmin_min)
		tf_mmm=obj_tf_mm.by_val(0.2)
		
		print(tf_mmm[-(n+10):-n])
		
		
		n_rosoku=100
		
	#	pl=xpRosoku.pl_owarine(xd_kabuka,50)
	#	pl.plot(lst_smax[-50:])
		pl=xpRosoku.candle_stick_plt(xd_kabuka,n_rosoku)
		pl.plot(lst_smax[-n_rosoku:])
		pl.plot(lst_smin[-n_rosoku:])
		pl.plot(lst_save[-n_rosoku:])
		pl.show()
		pl.close()
		
	






if __name__ == '__main__':
	print ('main test')
	
	
	kabuka=xdDataKabuka.load_byCode(3154)
	xdKabukaTyousei.xKabukaTyousei(kabuka)
	print(kabuka.keys())
	
	mmm=maxminmav(kabuka,10)
	
	
	
	
	print('main end')
