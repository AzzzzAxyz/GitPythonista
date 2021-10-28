#coding: utf-8
import statistics
import xcToolList as xl
import xDict
'''

'''

class KeysStat (object):
	def __init__(self):
		self.ave='average'
		self.sigma='sigma'
		self.ave_p1sd='ave_p1sd'
		self.ave_m1sd='ave_m1sd'
		self.max='max'
		self.min='min'
		self.median='median'
		self.med_H='median_High'
		self.med_L='median_Low'
		self.mode='mode'
		self.klst=[
			self.ave,self.sigma,self.ave_p1sd,self.ave_m1sd,
			self.max,self.min,
			self.median,self.med_H,self.med_L,self.mode,
		]

ks=KeysStat()

class Stat (object):
	def __init__(self,lst_origin):
		lst=xl.remove_None(lst_origin)
		self.dl=lst
		self.sd={}
		self.data_summary()
	
	def data_summary(self):
		self.sd[ks.ave]=statistics.mean(self.dl)
		self.sd[ks.sigma]=statistics.stdev(self.dl)
		self.sd[ks.ave_p1sd]=self.sd[ks.ave]+self.sd[ks.sigma]
		self.sd[ks.ave_m1sd]=self.sd[ks.ave]-self.sd[ks.sigma]
		self.sd[ks.max]=max(self.dl)
		self.sd[ks.min]=min(self.dl)
		self.sd[ks.median]=statistics.median(self.dl)
		self.sd[ks.med_H]=statistics.median_high(self.dl)
		self.sd[ks.med_L]=statistics.median_low(self.dl)
		self.sd[ks.mode]=statistics.mode(self.dl)
		return self.sd

	def print_summary(self):
		kl=KeysStat()
		for l in kl.klst:
			print(f'{l} : {self.sd[l]:3f}')


class Stack_summary(object):
	def __init__(self):
		self.stack_sum=[]

	def add_summary(self,lst):
		st=Stat(lst)
		self.stack_sum.append(st.data_summary())

	def add_stack(self,xd):
		self.stack_sum.append(xd)

	def return_xDict(self):
		retD=xDict.rows_to_dic(self.stack_sum)
		return retD


if __name__ == '__main__':
	print ('main test')
	d=[l for l in range(10)]+[1,3,5,None]
	st=Stat(d)
	summary=st.data_summary()
	st.print_summary()


	
	
	
	
	print('main end')
