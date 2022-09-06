
tangerine = "Livin ref of a dream! | OOP"

class Employees():


    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first+last}@gmail.com"

    def fullname(arg):
        # return self.first + self.last
        return (f"{arg.first} {arg.last}")
        

employe1 = Employees("Alnafis", "Chowdhury", 76500)
employee2 = Employees("Test", "Number", 1)


# print(employe1.fullname())
# print(employee2.fullname())
# employee2.fullname()

# print(Employees.fullname(employee2))
print("------------------------")
print(employe1.email)


dic1 = {
    "RC": "Racing",
    "HT": "Hunting",
    "SM": "Swimming",
    "FT": "Fighting"
}

region = {
    "London": "Ilford",
    "Birmingham" : "Spoons",
    "Chelsea" : "Chelsea FC",
    "Liverpool" : "FCClub",
    "Fighting" : "United"
}

class roles():
  

    def __init__(self, roleName, roleTime, rolePay):
        self.roleName = roleName
        self.roleTime = roleTime
        self.rolePay = rolePay
    
    def calculateMonthly(self):
        return self.rolePay/(self.roleTime*12)

    def diction():
        for abbrv, sport in list(dic1.items()):
            print(f"{abbrv} is short for {sport} which is name of the activity.")
        else:
            return ""
    def skip_to_region():
        choice = input(">> ")
        
        try:
            print(region[dic1[choice]], ">>> IS THE FINAL DESTINATION!!!")
        except:
            print("What you have written does not exist!")


for value in region.values():
    print(value)


for keys in dic1.keys():
    print(keys)


class apple():
    def apples():
        print("I am Apples!! and from OOP.py")
        print(tangerine)

role = roles("Racing", 2, 75000)

print(role.roleName, "And ", role.rolePay)


print(roles.calculateMonthly(role), "Monthly Income")

print(roles.diction())











roles.skip_to_region()

