def get_max_diff(in_list):
    in_list.sort()
    return in_list[len(in_list)-1]-in_list[0]

def get_sum_chart(in_chart):
    total_sum = 0
    for row in in_chart:
        max_diff = get_max_diff(row)
        total_sum+= max_diff
    return total_sum

if __name__ == '__main__':
    num_rows = int(input())
    chart = []
    for row in range(num_rows):
        chart.append([int(x) for x in input().split()])
    chart = get_sum_chart(chart)
    print(chart)