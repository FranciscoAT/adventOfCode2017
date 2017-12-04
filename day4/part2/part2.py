def main():
    password_list = []
    for i in range(int(input())):
        password_list.append(input().split())
    print(count_valid(password_list))

def count_valid(password_list):
    valid_count = 0
    for password in password_list:
        if(check_valid(password)):
            valid_count += 1
    return valid_count

def check_valid(password):
    uniques = set([''.join(sorted(list(passphrase))) for passphrase in password])
    return len(uniques) == len(password)

if __name__ == '__main__':
    main()
