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
    seen = []
    for passphrase in password:
        sorted_passphrase = sorted(passphrase)
        if sorted_passphrase not in seen:
            seen.append(sorted_passphrase)
        else:
            return False
    return True

if __name__ == '__main__':
    main()