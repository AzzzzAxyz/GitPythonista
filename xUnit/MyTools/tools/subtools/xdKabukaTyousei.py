#coding: utf-8
'''

'''
import xiKeysKabuka as xikk
import xDict


#xDictKabuka.xKabukaTyousei(kd) から引っ張って来た



#調整後終値から、分割併合の処理する関数のための関数
def _xAmultiBdividedC(lstA,lstB,lstC):
	retD=[a*b/c for (a,b,c) in zip(lstA,lstB,lstC) ]
	return retD

#調整後終値から分割併合の対応をする関数
#20210823 辞書への追加ではなく新しい辞書を返す形に変更

def xKabukaTyousei(kabuka_bef):
	kk=xikk.Keys_Kabuka()
	rkk=xikk.Keys_rawKabuka()
	
#	kyl=[l for l in kabuka_bef.keys()]
#	val=[kabuka_bef[k] for k in kyl]
#	kabuka={k:v for k,v in zip(kyl,val)}
	kabuka=xDict.copy(kabuka_bef)
	
	kabuka[rkk.start]=kabuka[kk.start]
	kabuka[rkk.high]=kabuka[kk.high]
	kabuka[rkk.low]=kabuka[kk.low]
	kabuka[rkk.end]=kabuka[kk.end]
	
	lstB=kabuka[kk.owarine]
	lstC=kabuka[kk.end]
	kabuka[kk.start]=_xAmultiBdividedC(
		kabuka[kk.start],lstB,lstC)
	kabuka[kk.high]=_xAmultiBdividedC(
		kabuka[kk.high],lstB,lstC)
	kabuka[kk.low]=_xAmultiBdividedC(
		kabuka[kk.low],lstB,lstC)
	kabuka[kk.end]=_xAmultiBdividedC(
		kabuka[kk.end],lstB,lstC)
	return kabuka

def tyousei_xD(kabuka):
	retD=xKabukaTyousei(kabuka)
	return retD


if __name__ == '__main__':
	print ('main test')
	

	print('main end')





