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


text=input("\033[0;32mEnter Text /> ")
number1=int(input("Enter Number /> "))
name1=input("\033[0;32mEnter Name for file /> ")
f = open(name1+".txt","a")
print("""\033[0;34m
1.Write
2.Writeline
\033[0;32m""")
mode1=input("\033[0;32mEnter mode : ")
if (mode1=="1"): 
    while (number1 >= 1):
        print('\033[0;37m',text,end = " ")
        f.write(text+" ")
        number1-=1
elif (mode1=="2"):
    while (number1 >= 1):
        print(text)
        f.write(text+"\n")
        number1-=1
else:
    print("\033[0;31mErorr mode")
