#coding: utf-8

'''
xiはインターフェースとかインデックスとか
今まで作った関数とかのアダプターとか
'''


class Keys_Order (object):
	def __init__(self):
		self.date_o = 'Order_date'
		self.date_c = 'Contract_date'
		self.flag_buy = 'BuyFlag'
		self.flag_sell = 'SellFlag'
		self.flag_new = 'NewFlag'
		self.flag_close = 'CloseFlag'
		self.amount='Amount'
		self.ord_method = 'OrderMethod'
		self.ord_price = 'OrderPrice'
		self.fee = 'Fee'
		self.ord_preprice = 'PrerequisitesPrice'
		self.ord_result = 'OrderResult'
		self.lst_keys = [
			self.date_o,self.date_c,
			self.flag_buy,self.flag_close,
			self.flag_new,self.flag_close,
			self.ord_method,self.ord_price,
			self.ord_preprice,self.ord_result,
			self.fee,
		]
		
	def return_order_dict(self):
		retD={k:None for k in self.lst_keys}
		return retD


def _check_order(xd):
	kord=Keys_Order()

"""
class KeysOrderTF (object):
	def __init__(self):
		self.date = 'date'
		self.date_next='date_next'
		self.sig_BN = 'BN_signal'
		self.sig_BC = 'BC_signal'
		self.sig_SN = 'SN_signal'
		self.sig_SC = 'SC_signal'
		
		self.lst_keys = [
			self.date,self.date_next,
			self.sig_BN,self.sig_BC,
			self.sig_SN,self.sig_SC,
			]
"""

class Keys_OrderSig (object):
	def __init__(self):
		self.date = 'date'
		self.date_next='date_next'
		self.sig_BN = 'BN_signal'
		self.sig_BC = 'BC_signal'
		self.sig_SN = 'SN_signal'
		self.sig_SC = 'SC_signal'
		
		self.lst_keys = [
			self.date,self.date_next,
			self.sig_BN,self.sig_BC,
			self.sig_SN,self.sig_SC,
			]
		





class Keys_ContractOrder (object):
	def __init__(self):
		self.code='Code'
		self.date_o = 'Order_date'
		self.date_c = 'Contract_date'
		self.flag_buy = 'BuyFlag'
		self.flag_sell = 'SellFlag'
		self.flag_new = 'NewFlag'
		self.flag_close = 'CloseFlag'
		self.amount='Amount'
		self.price = 'Price'
		self.fee = 'Fee'
		self.tax = 'Tax'
		self.otherpay = 'OtherPayment'
		self.money='AmountOfMoney'
		self.lst_keys = [
			self.code,
			self.date_o,self.date_c,
			self.flag_buy,self.flag_close,
			self.flag_new,self.flag_close,
			self.amount,self.price,
			self.fee,self.tax,self.otherpay,
			self.money,
		]
		
	def return_order_dict(self):
		retD={k:None for k in self.lst_keys}
		return retD

	



class Keys_KingakuLog(object):
	def __init__(self):
		self.code='code'
		self.cont_date='ContractDate'
		self.BN_Price = 'BuyNewPrice'
		self.BN_Num = 'BuyNewNum'
		self.BN_Fee = 'BuyNewFee'
		self.BN_Tax = 'BuyNewTax'
		self.BN_PxN = 'BuyNewPxN'
		self.BN_BoP = 'BuyNewBalanceOfPayments'

		self.BC_Price = 'BuyClosePrice'
		self.BC_Num = 'BuyCloseNum'
		self.BC_Fee = 'BuyCloseFee'
		self.BC_Tax = 'BuyCloseTax'
		self.BC_PxN = 'BuyClosePxN'
		self.BC_BoP = 'BuyCloseBalanceOfPayments'

		self.SN_Price = 'SellNewPrice'
		self.SN_Num = 'SellNewNum'
		self.SN_Fee = 'SellNewFee'
		self.SN_Tax = 'SellNewTax'
		self.SN_PxN = 'SellNewPxN'
		self.SN_BoP = 'SellNewBalanceOfPayments'

		self.SC_Price = 'SellClosePrice'
		self.SC_Num = 'SellCloseNum'
		self.SC_Fee = 'SellCloseFee'
		self.SC_Tax = 'SellCloseTax'
		self.SC_PxN = 'SellClosePxN'
		self.SC_BoP = 'SellCloseBalanceOfPayments'

		self.lst_keys=[
			self.code,self.cont_date,
			self.BN_Price,self.BN_Num,self.BN_Fee,
			self.BN_Tax,self.BN_PxN ,self.BN_BoP,
			self.BC_Price ,self.BC_Num ,self.BC_Fee,
			self.BC_Tax,self.BC_PxN,self.BC_BoP,
			self.SN_Price,self.SN_Num,self.SN_Fee,
			self.SN_Tax,self.SN_PxN,self.SN_BoP,
			self.SC_Price,self.SC_Num,self.SC_Fee,
			self.SC_Tax,self.SC_PxN,self.SC_BoP,
		]


class Keys_Position(object):
	def __init__(self):
		self.date='yakujoubi'
		self.code='syoukenCode'
		self.unit='tangen'
		self.BS_Fee='BS_Fee'
		self.otherLoss='otherLoss'

		self.B_posPay='BuyPosPayments'
		self.B_posNum='BuyPositionNum'
		self.B_posAveKakaku='BuyPositionAverageKakaku'
		self.B_posAmari='BuyKakakuTyousei'

		self.S_posPay='SellPosPayments'
		self.S_posNum='SellPositionNum'
		self.S_posAveKakaku='SellPositionAverageKakaku'
		self.S_posAmari='SellKakakuTyousei'






if __name__ == '__main__':
	print ('main test')
	
	obj_order=Keys_ContractOrder()
	order =obj_order.return_order_dict()
	print(order)
	




	
	print('main end')
