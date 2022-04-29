def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    start_idx = 0 # index under reference (start)
    end_idx = len(sorted_array) - 1 # index under reference (end)
    while True :
        number_of_array = end_idx - start_idx + 1 # number of arrays in search
        if number_of_array % 2 == 0: # even
            EVENdivided2 = int(number_of_array/2)
            median_number = ( sorted_array[start_idx+EVENdivided2] + \
                              sorted_array[start_idx+EVENdivided2-1] )/2 # calculate the median
            if target_number < median_number: # explore the previous array
                end_idx = start_idx + EVENdivided2 - 1 # refresh index
            elif median_number < target_number: # explore the backward array
                start_idx = start_idx + EVENdivided2 # refresh index
        elif number_of_array % 2 == 1: # odd
            ODDdivided2 = int( (number_of_array-1)/2 )
            median_number = sorted_array[start_idx+ODDdivided2] # calculate the median
            if target_number == median_number: # exist in the array
                return start_idx + ODDdivided2 # return target index
            elif number_of_array == 1: # target number does not exist in the array
                break
            elif target_number < median_number: # explore the previous array
                end_idx = start_idx + ODDdivided2 - 1 # refresh index
            elif median_number < target_number: # explore the backward array
                start_idx = start_idx + ODDdivided2 + 1 # refresh index
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
