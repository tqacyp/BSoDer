
import os
import random
import time
sys=input("What operatoring system you are using? Windows/other:")
if sys.lower()=="windows":
    real=True
    firm=[]
    for i in range(5):
        firm.append(random.randint(0,9))
    for i in firm:
        firm_num=input("Do you really want to blue screen? Yes,press %d." %(i))
        if int(firm_num) == i:
            continue
        else:
            print("Abort.")
            real=False
            break
    if real:
        print("Save all your work. Blue screen will appear in 30 seconds.")
        for i in range(30,0,-1):
            print(i)
            time.sleep(1)
        os.system("taskkill /f /fi \"pid ne 1\"")
else:
    print("Not support.")

    