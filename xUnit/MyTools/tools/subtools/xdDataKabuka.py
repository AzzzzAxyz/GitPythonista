#coding: utf-8
import xDictKabuka
import xDataFile


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




class syugo (object):
	def __init__(self,x):
		self.x=x
	
	def mtd(self):
		
		retD='return'
		return retD


def mtd(x):
	pass




if __name__ == '__main__':
	print ('main test')
	
	kd=load_byCode(3154)
	kousin_byCode(3154)
	
	
	print('main end')
