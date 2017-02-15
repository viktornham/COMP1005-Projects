#c)

light = str(input("What is the traffic light colour? "))

speed = float(input("What is the speed of the car in meters per second? "))

distance = float(input("What is the distance to the intersection in meters? "))

timeto = distance/speed

if light == "green" or light == "yellow" and timeto <= 5 or light == "red" and timeto <= 2:

    print("Go")

else:

    print("Stop")
