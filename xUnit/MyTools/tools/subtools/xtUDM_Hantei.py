# coding: utf-8
import xiKeysKabuka
import xaMax
import xaMin
import 
'''
UpDownMotiaiの判定をする
とりあえず　
・Maxが更新されているのがUp、Minが更新されているのがDown、どちらでもないが持ち合い
・MaxMinの幅を平均値で割って、それがある程度の大きさがあれば相場が動いていると考える。
・正解データとして作るので、前にシフトする
'''

kk = xiKeysKabuka.Keys_Kabuka()

def _maxminhaba(xd):
    retD=



class ByMaxMin(object):
    def __init__(self, xd_kabu, n=None):
        if n == None: n = 10
        max_high=xaMax.Max(xd[kk.high])
        min_low=xaMin.Min(xd[kk.low])


        self.high_max=max_high.by_num(n)
        self.low_min=min_low.by_num(n)



    def by_num(self, num):
        self.lst_sftmin = _minLow(self.xd_kabuka, num)
        self.lst_agehaba = _divsub(self.lst_sftmin, self.lst_nextstart)
        return self.lst_agehaba


if __name__ == '__main__':
    print('main test')

    print('main end')
