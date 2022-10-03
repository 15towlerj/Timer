import time
import webbrowser
print ("Hello this is an automated timer.")
def Timer1(t):
    while t>0:
        print(t)
        t -= 1
        time.sleep(1)
    print("Blast off!")
    webbrowser.open("https://www.youtube.com/watch?v=SyimUCBIo6c")
Timer1M = float(input("How many minutes do you want to time?"))
Timer1S = Timer1M*60
Timer1(Timer1S)




