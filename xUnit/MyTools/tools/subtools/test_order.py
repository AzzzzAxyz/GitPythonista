#coding: utf-8
import urllib

class syugo (object):
	def __init__(self,x):
		self.x=x
	
	def mtd(self):
		
		retD='return'
		return retD


def mtd(x):
	pass


def dataByCode(code):
	import xFileData as xFD
	retD=xFD.loadJikeiByCode(code)
	return retD


if __name__ == '__main__':
	print ('main test')
	


