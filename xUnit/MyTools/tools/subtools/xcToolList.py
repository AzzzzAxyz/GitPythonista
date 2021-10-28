#coding: utf-8
'''

'''

def remove_None(lst):
	retD=[l for l in lst if l!=None]
	return retD


def remove_None_xylst(lx,ly):
	pass
	



def _check_length(la,lb):
	if len(la)!=len(lb):return False
	else: return True


def _enzan(a,b,func):
	if a==None:return None
	if b==None:return None
	return  func(a,b)


def plus(la,lb):
	retD=[_enzan(a,b,lambda a,b:a+b) for a,b in zip(la,lb)]
	return retD

def sabun(la,lb):
	retD=[_enzan(a,b,lambda a,b:a-b) for a,b in zip(la,lb)]
	return retD

def divide(la,lb):
	retD=[_enzan(a,b,lambda a,b:a/b) for a,b in zip(la,lb)]
	return retD
	
def multi(la,lb):
	retD=[_enzan(a,b,lambda a,b:a*b) for a,b in zip(la,lb)]
	return retD
	


if __name__ == '__main__':
	print ('main test')
	
	la=[0,1,2,4,None]
	lb=[None,5,6,7,8]
	lc=[2,2,2]
	print(sabun(la,lb))
	print(sabun(lb,lc))

	
	
	print('main end')

