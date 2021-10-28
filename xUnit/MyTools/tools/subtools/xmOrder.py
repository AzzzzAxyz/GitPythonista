#coding: utf-8
import xiKeysOrder
import xiKeysKabuka

kord=xiKeysOrder.Keys_Order()
kcord=xiKeysOrder.Keys_ContractOrder()
klog=xiKeysOrder.Keys_KingakuLog()
kosig=xiKeysOrder.Keys_OrderSig()
kk=xiKeysKabuka.Keys_Kabuka()

def _order_template():
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

def set_flag(dct,sig):
	if sig[kosig.sig_BN]==True:new_buy(dct)
	elif sig[kosig.sig_BC]==True:close_buy(dct)
	elif sig[kosig.sig_SN]==True:new_sell(dct)
	elif sig[kosig.sig_SC]==True:close_sell(dct)

def set_amount(dct,amount):
	dct[kord.amount]=amount

def set_orderprice(dct,price):
	dct[kord.price]=price

def set_contractprice(dct,price):
	dct[kcord.price]=price

def _kensaku_dateNext(xd,ord):
	dlst=xd[kk.date]
	n=dlst.index(ord[kord.date_o])
	datenext=dlst[n+1]
	return datenext
	


def single_from_ordersig(kabuka_xd,ordersig):
	
	od=_order_template()
	






def _test():
	print(kord.lst_keys)





if __name__ == '__main__':
	print ('main test')
	
	_test()
	
	
	print('main end')
