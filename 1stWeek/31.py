import random

print('베스킨라빈스 31 게임 프로그램')

# 유효성 범위(valid_list) 내에서 입력 받기


def validate_input(prompt, valid_list):
    while True:
        value = input(prompt)
        if value in valid_list:
            value = int(value)
            break
        else:
            print("잘못된 입력입니다. 재입력해주세요.")
    return value

# 컴퓨터가 이기는 숫자 반환


def call_computer(call_status):
    if call_status % 4 == 0:
        computer_call = 2
    elif call_status % 4 == 1:
        computer_call = 1
    elif call_status % 4 == 3:
        computer_call = 3
    else:
        computer_call = random.randint(1, 3)

    return computer_call


def call_numbers(size, called):
    for _ in range(size):
        called += 1
        print("'{0}'!!!".format(called))

        if called == 31:
            break

    return called


# 게임 시작
order = validate_input('순서를 입력하세요. (선공 1, 후공 0 입력) : ', ['0', '1'])

call = 0
count = 1

while call < 31:
    if count % 2 == order:
        print('사용자 차례')
        size_of_call = validate_input("호출할 개수를 입력하세요 : ", ['1', '2', '3'])

        call = call_numbers(size_of_call, call)

    else:
        print('컴퓨터 차례')
        size_of_call = call_computer(call)

        call = call_numbers(size_of_call, call)

    count += 1

if count % 2 == order:
    print("사용자의 승리!")
else:
    print("컴퓨터의 승리!")
