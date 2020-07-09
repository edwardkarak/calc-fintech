import math


def findTime():
    v = float(input("What is the initial vertical velocity in m/s?  "))
    theta = float(input("What is the firing angle, in degrees?  ")) * math.pi/180

    t1 = ((2 * v * math.sin(theta))/9.8)
    print("Time of flight is " + str(t1) + " s")
    print("Max height is " + str((v**2*(math.sin(theta)**2))/(2*9.8)) + " meters")

def findAngle():
    t = float(input("What is the time of flight, in seconds?  "))
    v = float(input("What is the velocity in m/s?  "))
    print(math.asin((0.5*t)*(9.8)/v) * 180/math.pi)

def findRange():
    # x = v_0 * t * cos(theta)
    v_0 = float(input("What is the initial velocity, in m/s?  "))
    theta = float(input("What is the firing angle, in degrees?  ")) * math.pi/180
    print((v_0 **2* math.sin(2*theta))/(9.8))

print("1:   Solve for time given v, theta and y_0")
print("2:   Solve for firing angle, given time, v, and y_0")
print("3:   Solve for range given initial velocity, firing angle and time of flight")
print("[Neglecting air resistance]")

choice = int(input("Select a choice:  "))

if choice==1:
    findTime()
elif choice == 2:
    findAngle()
elif choice == 3:
    findRange()