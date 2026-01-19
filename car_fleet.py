target = 10
position = [1,4]
speed = [3,2]


def car_fleet(target,position,speed):
    fleet = 0
    
    for i in range(len(position)):
        movement = (target - position[i])/speed[i]
        

print(car_fleet(target,position,speed))