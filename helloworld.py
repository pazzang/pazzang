from random import *
cnt = 0 
for i in range(1, 51):
    time = randrange(5, 51)
    if time >= 5 and time <= 15:
        cnt += 1
        print ("[O] {0}번째 손님 (소요시간: {1}분)".format(i, time))
    else: 
        print ("[ ] {0}번째 손님 (소요시간: {1}분)".format(i, time))

print("총 탑승 승객 : {0} 분".format(cnt))