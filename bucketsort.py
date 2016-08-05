# -*- coding: utf-8 -*-
def setData(pattern, num):

    datalist = []
    print('データを{}個入力してください'. format(num))

    for var in range(0, num):
        tmp = input('>>> ')
        while ((pattern-1) < int(tmp)) or (0 > int(tmp)):
            print('エラー：数字が範囲を超えています')
            tmp = input('>>> ')
        datalist.append(tmp)

    return datalist

def bucketSort(pattern, data, num):

    results = list()
    buckets = [[] for x in range(pattern)]
    print('INPUT: {}'. format(data))

    for x in range(0, num):
        buckets[ int(data[x]) ].append(data[x])

    i=0
    for x in range(0, pattern):
        y = 0
        maxlen = len(buckets[x])
        if maxlen is not 0:
            while y < maxlen:
                results.append(buckets[x][y])
                y += 1

    return results

def main():

    pattern = 10 # 0-9
    data = []
    result = []

    print('いくつのデータをソートしますか？')
    dataNum = input('>>> ')
    data = setData(pattern, int(dataNum))

    result = bucketSort(pattern, data, int(dataNum))
    print('RESULT: {}'. format(result))

if __name__ == '__main__':
    main()
