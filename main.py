import time

def countdown(countdown_t):
    while countdown_t:
        min, sec = divmod(countdown_t,60)
        timer = '{:02d}:{:02d}'.format(min,sec)
        print(timer,end="\r")
        time.sleep(1)
        countdown_t-=1
    print("Done!")

countdown_t= input("Enter the time(sec)")
countdown(int(countdown_t))