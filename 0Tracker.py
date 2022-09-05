from time import time

#Calculate your Time! Edited By RacingXHunter

#Weeks 1-4 > Mins
Week_1 = 886  #09 - 18 Aug
Week_2 = 870   #18 - 25 Aug
Week_3 = 806    #25 - 03 Aug
Week_4 = 0       #04 - 10 Sep
Week_5 = 0

#In Minutes
day1 = 171      #04
day2 = 0        #05
day3 = 0        #06
day4 = 0        #07
day5 = 0
day6 = 0
day7 = 0        #10

total_time = day1+day2+day3+day4+day5+day6+day7
total_timeH = total_time/60
time_remaining = (840-total_time)
hour_remaining = (time_remaining / 60)
#Space
print("Daily Information\n", "Day1: {} Mins\n" .format(day1),
        "Day2: {} Mins\n".format(day2),
        "Day3: {} Mins\n" .format(day3),
        "Day4: {} Mins\n" .format(day4),
        "Day5: {} Mins\n" .format(day5),
        "Day6: {} Mins\n" .format(day6),
        "Day7: {} Mins\n" .format(day7))
        


#mylist = [day1, day2, day3, day4, day5, day6, day7]
   # for i in mylist:
  #      print(i)
 #       


#print(day1,day2 ,day3,day4,day5,day6,day7)
print("Total Time Spent:", total_time, ">", total_timeH, "Hours")
print(f"Time Remaining: {time_remaining} Minutes")
print("Hours Remaining: ", hour_remaining)
print("Helper:", 120+51 )

