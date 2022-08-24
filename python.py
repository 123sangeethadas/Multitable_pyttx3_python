import pyttsx3

num= int(input("Enter a Number:"))

val=int(input("enter the range to be displayed:"))
txt=""
for i in range(1,val+1):
    result=i*num
    print(i,'x',num,'=',result)
    mul=str(i)," multiplies",str(num) ,'is equal to ',str(result) 
    txt+=str(mul)


engine = pyttsx3.init()
engine.say(txt)
engine.runAndWait()

    
    
    