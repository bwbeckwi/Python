'''
ARK Day length calculator
'''

from os import system


# Clear the screen
system('cls')


# 24 hours * 60 minute per hour = 1440 minutes
# ARK Survival is 1 real minute = 28 game minutes

TotalDailyLength = float(1440.0 / 28)
DayLength = float((input("Day length (minutes):? ")))
NightLength = float(TotalDailyLength - DayLength)

DayCycleScaleSpeed = int(1)
DayTimeScaleSpeed = float(28.0/DayLength)
NightTimeScaleSpeed = float(DayLength / NightLength)

print("\nDay Cycle Scale: "+ str(DayCycleScaleSpeed))
print("Day length (minutes): " + str(DayLength))
print("Night length (minutes): " + str(NightLength))
print("Day Time Scale Speed: " + str(DayTimeScaleSpeed))
print("Night Time Scale Speed: " + str(NightTimeScaleSpeed))

# End of script