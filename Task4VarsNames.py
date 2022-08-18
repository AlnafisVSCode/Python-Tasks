cars = 100
space_in_a_car = 4.0 #Ths is a floating point which is a decimal number
drivers= 30
passengers = 90
#More
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
avg_passenger_perCar = passengers / cars_driven
#Space
x = 11
j = 100

print("There are: ", cars ,"Cars Avalable to be used when asked")
print("there are good", drivers, "in the list of drivers")
#Space
print("today there are undrivers cars that total to", cars_not_driven)
print("we can transport", carpool_capacity, "peoplle today?")

print("put about", avg_passenger_perCar, "in each car")
#Space
print("Calculating 100 / 10 is :", j/x)
#Space
print("is 100 equal to 10??", x == j)

#s1
var_acs = 200
var_kd = 2.0
print(f"So my acs is {var_acs}, and my kd is around: {var_kd}. So can you add them?: {var_kd == var_acs}")