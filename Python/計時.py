import time

time_start = time.time() #開始計時

#要執行的程式碼，或函式
#要執行的程式碼，或函式
def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

n = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999997

if n ==1:
    print('不是質數')
elif is_prime(n):
    print('是質數')
else:
    print('不是質數')


time_end = time.time()    #結束計時

time_c= time_end - time_start   #執行所花時間
print('time cost', time_c, 's')