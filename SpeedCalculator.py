while True:
    rpm = float(input("Enter rpm: "))
    one = float(input("Enter motor gear size: "))# number of teeth
    two = float(input("Enter wheel gear size: "))# number of teeth
    radius = float(input("Enter wheel radius: "))# radius of the wheel in inches
    print(rpm*(one/two)*(2*3.14*radius*2.54*60*0.00001))# speed is in km/h