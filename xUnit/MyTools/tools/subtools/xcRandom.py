#coding: utf-8
import random
import matplotlib.pyplot as plt
import xcTF_Henkaten


'''

'''

def single_TF(true_probability):
	r=random.random()
	retD=False
	if r<=true_probability:retD=True
	return retD


def lst_TF(num,true_probability):
	retD=[single_TF(true_probability) for i in range(num)]
	return retD

def _lst_None(num):
	return [None for i in range(num)]


class RandomTF (object):
	def __init__(self,num,t_probability):
		self.lst_tf = lst_TF(num,t_probability)

		henka=xcTF_Henkaten.TF_Henkaten(self.lst_tf)
		self.henka_tf = henka.to_False()
		self.henka_ft = henka.to_True()


if __name__ == '__main__':
	print ('main test')
	
	n_sikou=10000
	lst=[single_TF(0.2) for i in range(n_sikou)]
	lst=lst_TF(n_sikou,0.4)
	
	obj=RandomTF(100,0.4)
	
	n_true=obj.lst_tf.count(True)
	to_tf=obj.henka_tf
	to_ft=obj.henka_ft
	print(n_true,to_tf.count(True),to_ft.count(True))
	[print(obj.lst_tf[i],':',obj.henka_tf[i],':',obj.henka_ft[i]) for i in range(20)]
	


	
	print('main end')

