#this a solo run

#A function first


def weather(arg1, arg2):
    print("Rain == 1\nLightning == 2")
    print(f"Today there will be a lot of rain, {arg1} drops ")
    print("There could be a potential lightnings, up to", arg2)
    return arg1 + arg2

def temp(arg1):
    print("Temp will be == 3")
    print("Average temp will be:", arg1)
    return arg1 * 3

rain = int(input("Input rain: "))
lightning = int(input("Input Lightning: "))
# rain = 1
# lightning = 2
lightning = lightning * 2

arg_var = (weather(rain, lightning))
# print("is equal to:", rain + lightning) METHOD 1
print("is equal to:", arg_var)  #METHOD 2

print("-"*20)

arg_temp = temp(int(input("Temp C: ")))
print("Totals temp:", arg_temp)



