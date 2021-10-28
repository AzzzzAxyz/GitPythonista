#coding: utf-8
import xiKeysOrder

kord=xiKeysOrder.Keys_Order()
kcord=xiKeysOrder.Keys_ContractOrder()


def _contract_order_template():
	#retD={k:None for k in kord.lst_keys}
	retD=kord.return_order_dict()
	return retD

def _flag_False(dct):
	dct[kord.flag_new]=False
	dct[kord.flag_buy]=False
	dct[kord.flag_close]=False
	dct[kord.flag_sell]=False


def new_buy(dct):
	_flag_False(dct)
	dct[kord.flag_new]=True
	dct[kord.flag_buy]=True

def new_sell(dct):
	_flag_False(dct)
	dct[kord.flag_new]=True
	dct[kord.flag_sell]=True

def close_buy(dct):
	_flag_False(dct)
	dct[kord.flag_close]=True
	dct[kord.flag_buy]=True

def close_sell(dct):
	_flag_False(dct)
	dct[kord.flag_close]=True
	dct[kord.flag_sell]=True


def makeFromOrder(order_dct):
	
	pass















def _test():
	print(kord.lst_keys)
	print(kcord.lst_keys)





if __name__ == '__main__':
	print ('main test')
	
	_test()
	
	
	print('main end')
