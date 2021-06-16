import random
def create_answer():
    a=[x for x in range(1,10)]
    random.shuffle(a)
    lis = []
    for _ in range(3):
        lis.append(a.pop())
    return(lis)
def input_num():
    a = b = c = 0 
    input_lis = [a,b,c]
    for i in range(1,4):
        input_lis[i-1] = input("{}번 숫자를 입력해주세요. : ".format(i))
        while input_lis[i-1].isalpha() or int(input_lis[i-1]) not in range(1,10):
            input_lis[i-1] = input("{}번 숫자를 다시 입력해주세요. : ".format(i))
    return int(input_lis[0]), int(input_lis[1]), int(input_lis[2])
def baseball(a,b,c,lis):
    strike = ball = flag = 0
    input_lis = [a,b,c]
    for i in range(3):
        if input_lis[i] in lis:
            ball += 1
        if input_lis[i] == lis[i]:
            strike += 1
        if strike == 3:
            flag = 1
    ball -= strike
    return strike,ball,flag
def game_start():
    restart = ''
    answer = create_answer()
    count = 0
    print("시작합니다.\n")
    while True: 
        a, b, c = input_num() 
        strike, ball, flag = baseball(a,b,c,answer)
        count += 1 
        print("\n입력 숫자 : {}{}{}입니다.".format(a,b,c))
        print("결과 : {}스트라이크 {}볼입니다.".format(strike,ball))
        if flag:
            print("정답입니다! 총 문제를 푼 횟수 : {}번입니다.\n".format(count))
            while restart not in ['y','Y','n','N']:
                restart = input("게임을 다시 시작하시겠습니까? [Y] / [N] \n")
            if restart == 'y' or restart == 'Y':
                game_start()
            else:
                print("종료합니다.")
                break
        else:
            print("현재 까지 문제를 푼 횟수 : {}번입니다.".format(count),end='\n\n')
game_start()
