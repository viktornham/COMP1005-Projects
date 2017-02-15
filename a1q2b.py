#b

light = str(input("What is the traffic light colour? "))

speed = float(input("What is the speed of the car in meters per second? "))

distance = float(input("What is the distance to the intersection in meters? "))

timeto = distance/speed

if timeto <= 2:

    print("Go")

elif light == "red":

    print("Stop")

elif timeto <= 5:

    print("Go")

elif light == "yellow":

    print("Stop")

elif light == "green":

    print("Go")

else:

    print("Stop")
    
