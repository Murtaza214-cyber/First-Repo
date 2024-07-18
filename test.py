class dog:

    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def meow(self):
        print("Meow Meow!?")
    def intro(self):
        print(Pet.name +" is "+ str(Pet.age)+"year's old")
    def birthday(self):
        self.age+=1
    def setBuddy(self,buddy):
        self.buddy=buddy
        buddy.buddy=self


Ozzy=dog("Ozzy",2)
Pet=dog("Pet",5)
Tim=dog("Tim",8)
Pet.meow()
Ozzy.intro()
print(Tim.name)
print(Tim.age)
Tim.birthday()
print(Tim.age)
