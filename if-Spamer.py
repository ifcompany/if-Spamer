#if
#007
#www.ifcompany.ir
import time
import os
global time1
time1 = time.strftime('%H:%M:%S')
os.system("clear")

print("""
        \033[0;33m Welcome to if spamer
            ifompany.ir\033[0m
   \033[0;35m    ___      /---\033[0;94mif if if if
   \033[0;35m       |----/    \033[0;94mif if if if
  if \033[0;33m -> \033[0;32m Spamer \033[0;33m-> \033[0;94mif if if if
      \033[0;35m ___|----\  \033[0;94m  if if if if
            \033[0;35m    \---\033[0;94mif if if if
      \033[0;33m  V 1.0.0 """,time1)
for _ in range(100):

    text=input("\033[0;32mEnter Text : ")
    number1=float(input("Enter Number : "))
    print("""\033[0;34m1.Write
2.Writeline\033[0;32m""")
    mode1=input("\033[0;32mEnter mode : ")
    if (mode1=="1"): 
        while (number1 >= 1):
            print('\033[0;37m',text,end = " ")
            number1-=1
    elif (mode1=="2"):
        while (number1 >= 1):
            print(text)
            number1-=1
    else:
        print("\033[0;31mErorr mode")
    exit1=input('\033[0;35m\nDo you Exit [Y/n] : ')
    if (exit1=="y"):
        exit()
    elif (exit1=="Y"):
        exit()
    elif (exit1=="N"):
        print("OK")
    elif (exit1=="n"):
        print("OK")
    else:
        print('\033[0;31mErorr\033[0m')
