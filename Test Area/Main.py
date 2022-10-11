from one import *
from two import *

print("""
~~~~~~~~~~ Welcome To Text To Speech Converter ~~~~~~~~~~
""")
print("""
Menu :
1| Converts The Typed Text Into Speech [Your preferred Language]
2| Converts The .txt File Into Speech 
""")

ans = "Yes"
while ans in ['Yes','y','Y','YES']:
  opt = int(input("\nEnter Option Number : "))
  if opt == 1:
    Op1()
  elif opt == 2:
    Op2()
  else:
    print("|Invalid Option|")
  ans = input("\n Continue ?")
