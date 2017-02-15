#a)

light = str(input("What is the traffic light colour? "))

speed = float(input("What is the speed of the car in meters per second? "))

distance = float(input("What is the distance to the intersection in meters? "))

timeto = distance/speed

if light == "yellow":

    if timeto <= 5:

        print("Go")

    else:

        print("Stop")

else:

    if light == "red":

        if timeto <= 2:
            print ("Go")

        else:

            print("Stop")

    else:

        if light == "green":
            print("Go")

        else:
            print("Stop")
          
    
                    
