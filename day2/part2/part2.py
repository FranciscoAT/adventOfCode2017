def get_max_divis(in_list):
    in_list.sort()
    for index in range(len(in_list)):
        divisor = in_list[index]
        for ref in range(index+1, len(in_list)):
            if in_list[ref]%divisor == 0:
                return int(in_list[ref]/divisor)
    return 0

def get_sum_chart(in_chart):
    total_sum = 0
    for row in in_chart:
        max_diff = get_max_divis(row)
        total_sum+= max_diff
    return total_sum

if __name__ == '__main__':
    num_rows = int(input())
    chart = []
    for row in range(num_rows):
        chart.append([int(x) for x in input().split()])
    sum = get_sum_chart(chart)
    print(sum)