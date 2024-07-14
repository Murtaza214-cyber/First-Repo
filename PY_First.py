#This program says hello and asks for my name.
x=1
while x<4 :
    print('Hello world!',x)
    x=x+1
    break
x=["apple","banan","iueow"]
ooooo=input()
for i in x:
    print(i)
    x.append(input())
print('What is your name?')    # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')    # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
print('I have eaten'+str(99)+'burritos')
