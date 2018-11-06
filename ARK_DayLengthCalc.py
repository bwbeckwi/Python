'''
ARK Day length calculator
'''

from os import system

# Begin Script
# Clear the screen
system('cls')

'''
NOTES:
24 hours * 60 minute per hour = 1440 minutes
ARK Survival is 1 real minute = 28 game minutes
Adjusted time closer to 1  = 23.999996
TotalDailyLength = float(1440.0 / 28)
'''

# Used this to mimic as close to 60 minutes for a 24 hour
# game day/night.
num_minutes_a_day = 23.999996

TotalDailyLength = float(1440.0 / num_minutes_a_day)

DayLength = float((input("Day length in minutes:? ")))
NightLength = float(TotalDailyLength - DayLength)

DayCycleScaleSpeed = int(1)
DayTimeScaleSpeed = float(28.0/DayLength)
NightTimeScaleSpeed = float(DayLength / NightLength)

print("\nDay Cycle Scale: "+ str(DayCycleScaleSpeed))
print("Day length in minutes: " + str(DayLength))
print("Night length in minutes: " + str(NightLength))
print("Day Time Scale Speed: " + str(DayTimeScaleSpeed))
print("Night Time Scale Speed: " + str(NightTimeScaleSpeed))

# End of script