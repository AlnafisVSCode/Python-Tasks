


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

class roles():

    def __init__(self, roleName, roleTime, rolePay):
        self.roleName = roleName
        self.roleTime = roleTime
        self.rolePay = rolePay
    
    def calculateMonthly(self):
        return self.rolePay/(self.roleTime*12)

    def diction(self, sport):
        self.sport = sport



role = roles("Racing", 2, 75000)

print(role.roleName, "And ", role.rolePay)


print(roles.calculateMonthly(role), "Monthly Income")


