# coding: utf-8

import subtools.xbMax as xbmax
import subtools.xaMax
import subtools.xaMin
import subtools.xaShift
import subtools.xaDivSubMaxMin

'''
１日後の始値を基準としてn日後の高値、安値をヒストグラム化
平均とシグマなどの統計値を計算する
教師データの妥当性、短期取引の目標をどこに置くかということの判断基準とする
'''






if __name__ == '__main__':
    print('main test')

    lst_a = [None, None]
    lst_b = [i for i in range(20)]
    lst = lst_a + lst_a + lst_b + lst_a + lst_b

    cls = xbmax.Max(lst)
    [print(i, l) for i, l in zip(lst, cls.by_num(3))]

    print('main end')
