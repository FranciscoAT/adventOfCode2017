def check_valid(password_list):
    valid_count = 0
    for password in password_list:
        if check_unique(password):
            valid_count+=1
    return valid_count

def check_unique(phrase_list):
    seen = set()
    for phrase in phrase_list:
        if phrase not in seen:
            seen.add(phrase)
        else:
            return False
    return True

if __name__ == '__main__':
    input_lists = []
    for i in range(int(input())):
        input_lists.append(input().split())
    num_valid = check_valid(input_lists)
    print(num_valid)
