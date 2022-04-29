def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    start_idx = 0
    end_idx = len(array) - 1
    while True:
        while True:
            if array[start_idx] >= pivot:
                flag = 0
                break
            elif start_idx+1 == end_idx:
                flag = 1
                break
            else: start_idx = start_idx  + 1
        while True:
            if array[end_idx] < pivot:
                flag = flag + 10
                break
            elif start_idx+1 == end_idx:
                flag = flag + 100
                break
            else: end_idx = end_idx  - 1

        if flag == 10:
            array[start_idx], array[end_idx] = array[end_idx], array[start_idx]
        elif (flag == 11) or (flag == 101):
            if end_idx == 0:
                prev_array = array[0:1]
                next_array = array[1:len(array)]
            else:
                prev_array = array[0:end_idx]
                next_array = array[end_idx:len(array)]
            print(prev_array,end=' ')
            print(next_array)
            return sort(prev_array) + sort(next_array)
        elif flag == 100:
            if start_idx == 0:
                prev_array = array[0:1]
                next_array = array[1:len(array)]
            else:
                prev_array = array[0:start_idx]
                next_array = array[start_idx:len(array)]
            print(prev_array,end=' ')
            print(next_array)
            return sort(prev_array) + sort(next_array)

    # ここまで記述

if __name__ == '__main__':
    main()
