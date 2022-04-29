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
    start_idx = 0 # define index for the starting value
    end_idx = len(array) - 1 # define index for the last value
    while True:
        while True:
            if array[start_idx] >= pivot: # search for values larger than the pivot
                flag = 0 # set Flag
                break # break infinite loops
            elif start_idx+1 == end_idx: # if neighboring values
                flag = 1 # set Flag
                break # break infinite loops
            else: start_idx = start_idx  + 1
        while True:
            if array[end_idx] < pivot: # search for values smaller than the pivot
                flag = flag + 10 # set Flag
                break # break infinite loops
            elif start_idx+1 == end_idx: # if neighboring values
                flag = flag + 100 # set Flag
                break # break infinite loops
            else: end_idx = end_idx  - 1

        # Process each flag that was set.
        if flag == 10:
            array[start_idx], array[end_idx] = array[end_idx], array[start_idx] # Swap
        elif (flag == 11) or (flag == 101):
            if end_idx == 0: # 0 is an exception because it cannot be split well
                prev_array = array[0:1]
                next_array = array[1:len(array)]
            else:
                prev_array = array[0:end_idx]
                next_array = array[end_idx:len(array)]
            return sort(prev_array) + sort(next_array) # recursive processing
        elif flag == 100:
            if start_idx == 0: # 0 is an exception because it cannot be split well
                prev_array = array[0:1]
                next_array = array[1:len(array)]
            else:
                prev_array = array[0:start_idx]
                next_array = array[start_idx:len(array)]
            return sort(prev_array) + sort(next_array) # recursive processing
    # ここまで記述

if __name__ == '__main__':
    main()
