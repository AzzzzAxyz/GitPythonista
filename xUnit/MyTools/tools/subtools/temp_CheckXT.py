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

'''

'''

kk=xiKeysKabuka.Keys_Kabuka()

def age_num_plot(kabuka,num):
	age=agehaba.xtNextStart_Agehaba(kabuka,num)
	lst_age=age.by_num(num)
	xpp.plot(lst_age)
	xpp.hist_binsN(lst_age,50)
	retD=xl.remove_None(lst_age)
	return retD

def sage_num_plot(kabuka,num):
	age=sagehaba.xtNextStart_Sagehaba(kabuka,num)
	lst_age=age.by_num(num)
	xpp.plot(lst_age)
	xpp.hist_binsN(lst_age,50)
	retD=xl.remove_None(lst_age)
	return retD

def kurikaesu_plot():
	xd_stat={'num':[],'ave':[],'sigma':[],
		'max':[],'min':[],}
		
	for i in range(3,20,2):
		print(f'haba_n : {i}')
		lst_i=age_num_plot(d,i)
		lst_is=sage_num_plot(d,i)
		xd_stat['num'].append(i)
		xd_stat['ave'].append(np.average(lst_i))
		xd_stat['sigma'].append(np.std(lst_i))
		xd_stat['max'].append(max(lst_i))
		xd_stat['min'].append(min(lst_i))

def print_staticsummary(code,num):
	print(f'----- : ----- : -----')
	age_stat,sage_stat=return_staticsummary(code,num)
	print(f'--- :age summary haba_num : {num}')
	age_stat.print_summary()
	print(f'--- :sage summary haba_num : {num}')
	sage_stat.print_summary()

def return_staticsummary(code,num):
	kabuka = xdDataKabuka.load_byCode(code)
	xdKabukaTyousei.xKabukaTyousei(kabuka)
	age = agehaba.xtNextStart_Agehaba(kabuka, num)
	lst_age = age.by_num(num)
	age_stat = xcs.Stat(lst_age)
	sage = sagehaba.xtNextStart_Sagehaba(kabuka, num)
	lst_sage = sage.by_num(num)
	sage_stat = xcs.Stat(lst_sage)
	return age_stat,sage_stat

def stack_staticsummary(code,num_lst):
	age_stack=xcs.Stack_summary()
	sage_stack=xcs.Stack_summary()

	for num in num_lst:
		age, sage = return_staticsummary(code, num)
		age_stack.add_stack(age.sd)
		sage_stack.add_stack(sage.sd)

	return age_stack,sage_stack


if __name__ == '__main__':
	print ('main test')
	
	kabuka=xdDataKabuka.load_byCode(3154)
	xdKabukaTyousei.xKabukaTyousei(kabuka)
	print(kabuka.keys())


#	for i in range(3,20,5):
#		print_staticsummary(3154,i)

	num_lst=range(3,50,2)
	age,sage=stack_staticsummary(3154,num_lst)
	age_xd  = age.return_xDict()
	sage_xd = sage.return_xDict()

	ks=xcs.KeysStat()
	plt.plot(num_lst,age_xd[ks.ave])
	plt.plot(num_lst,age_xd[ks.max])
	plt.plot(num_lst,age_xd[ks.min])
	plt.plot(num_lst,sage_xd[ks.ave])
	plt.plot(num_lst,sage_xd[ks.max])
	plt.plot(num_lst,sage_xd[ks.min])


	plt.show()
	plt.close()

	
	print('main end')
