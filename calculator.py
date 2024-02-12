a=int(input("enter number one: "))
b=int(input("enter number two: "))

command=(input('command:'))
if command=='+':
    print('sum:' ,a+b)
elif command=='-':
    print('subtract:' ,a-b)
elif command=='*':
    print('mul:',a*b)
elif command=='/':
    print('div:',a/b)
else:
    print("no operation entered")