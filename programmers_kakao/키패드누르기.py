def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))


def get_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solution(numbers, hand):
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, "#"]]
    n = len(numbers)
    result = []
    cur_left = '*'
    cur_right = '#'
    for i in range(n):
        cur_num = numbers[i]
        if cur_num in [1, 4, 7, '*']:
            cur_left = cur_num
            result.append('L')
        elif cur_num in [3, 6, 9, "#"]:
            cur_right = cur_num
            result.append('R')
        else:
            cur_num_coord = index_2d(arr, cur_num)
            cur_left_coord = index_2d(arr, cur_left)
            cur_right_coord = index_2d(arr, cur_right)
            left_dist = get_dist(cur_left_coord, cur_num_coord)
            right_dist = get_dist(cur_right_coord, cur_num_coord)
            if left_dist == right_dist:
                if hand == "left":
                    cur_left = cur_num
                    result.append('L')
                else:
                    cur_right = cur_num
                    result.append('R')
            elif left_dist < right_dist:
                cur_left = cur_num
                result.append('L')
            else:
                cur_right = cur_num
                result.append('R')
    answer = ''.join(result)
    # print(cur_x, cur_y) col row

    return answer