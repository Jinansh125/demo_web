#first_name="Jinansh"
#Last_name="Shah"
#Full_name= first_name+" "+Last_name
#print("hello "+Full_name)
#print(type("name"))
#age = 16
#age+=1
#print("your age is: "+str(age))
#print(type(age))
#height = 176.5
#print("your height is: "+str(height)+"cm")
#print(type(height))
#human = True
#print("are you a human: "+str(human))
#print(type(human)
#print("aadil is a bot")
#name="jinansh"
#print(len(name))
#print(name.find("j"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("n"))
#print(name.replace("n","m"))
#print(name*3)
#x=1#int.
#y=2.0#float
#z="3"#str.
#print("X is"+str(x))
#print("Y is"+str(y))
#print(3+int(z))
#name=input("What is your name? ")
#age=int(input("How old are you? "))
#height=float(input("How tall are you? "))
#print("hello "+ name)
#print("You are "+str(age)+" years old ")
#print("You are "+str(height)+" cm tall ")
#import math
#x=1
#y=2
#z=3
#pi=3.14
#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(pi))
#print(max(x,y,z))
#print(min(x,y,z))
#name="Jinansh Shah"
#first_name= name[0:3]
#last_name=name[8:12]
#funky_name=name[1:12:2]
#reversed_name=name[::-1]
#print(reversed_name)
#website="http://google.com"
#website2="http://wikipedia.com"
#slice=slice(7,-4)
#print(website2[slice])
#age=int(input("How old are you? "))
#if age>=18:
    #print("you are an adult")
#elif age<0:
    #print("you haven't been born yet")
#else:
    #print("you are a child")
#temp=int(input("What is the temperature today? "))
#if not(temp>=0 and temp<=30):
    #print("weather is bad")
#elif not(temp<0 or temp>30):
   #print("the weather is good today")
#while 1==1:
    #print("Help")
#name=""
#while len(name)==0:
 #   name=input("Enter you name:")
#print("Hello"+name)
#for i in range(10):
    #print(i)
#for i in range(50,100,2):
    #print(i)
#for k in "bro code":
   # print(k)
#import time

#for seconds in range(10,0,-1):
   # print(seconds)
    #time.sleep(1)
   # print("Happy new year")
#rows= int(input("How many rows?"))
#columns= int(input("How many columns?"))
#Symbol= input("Enter a symbol to use:")

#for i in range(rows):
  #  for j in range (columns):
   #     print(Symbol,end="")
#print()
#food=["pizza","hamburger","spaghetti"]
#food[2]="sushi"
#print(food[2])
#food.append("ice cream")
#food.remove("pizza")
#food.pop()
#food.insert(0,"cake")
#food.clear()
#for x in food:
    #print(x)
import streamlit as st

st.title("Jinansh Shah")
st.header("Cas")
st.subheader("Python coding")
st.markdown("I have accomplished my goal!")
name = st.text_input("Enter your name: ")
fname= st.text_input("Enter your Father name: ")
adr= st.text_area("Enter your adress: ")
classdata = st.selectbox("enter your class:",(1,2,3,4,5))
button = st.button("Done")
if button :
    st.markdown(f"""
    Name: {name} 
    Father name: {fname}
    address: {adr}
    class:{classdata}""")












