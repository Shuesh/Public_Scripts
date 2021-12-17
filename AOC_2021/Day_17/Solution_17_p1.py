import re
import copy

#Example: target area: x=20..30, y=-10..-5
#Input: target area: x=111..161, y=-154..-101
def main():
    #Example
    target_zone_definition = [[20,-10], [30,-5]]
    #Input
    # target_zone_definition = [[111,-154],[161,-101]]

    x_range = [i for i in range(target_zone_definition[0][0], target_zone_definition[1][0] + 1)]
    y_range = [j for j in range(target_zone_definition[0][1], target_zone_definition[1][1] + 1)]

    target_zone = []
    for y_coord in range(target_zone_definition[0][1],target_zone_definition[1][1]):
        for x_coord in range(target_zone_definition[0][0],target_zone_definition[0][0]):
            target_zone.append([x_coord,y_coord])

    x_velocities = X_Velocities(x_range)
    y_velocities = Y_Velocities(y_range, x_velocities)
    
    max_y = y_velocities[-1]
    max_height = 0
    while max_y > 0:
        max_height += max_y
        max_y -= 1

    print(max_height)

#Only shoots to the right
def X_Velocities(x_range):
    x_coord = 0
    x_velocity = 0
    x_velocities = []

    while x_coord < x_range[-1]:
        x_coord += x_velocity
        x_velocity += 1
        if x_coord >= x_range[0] and x_coord <= x_range[-1]:
            x_velocities.append(x_velocity)

    return x_velocities


#Start from the negative point, then reach 0 y velocity at the halfway point
def Y_Velocities(y_range, x_velocities):
    
    y_velocities = []
    for velocity in x_velocities:
        step_number = 0
        y_coord = 0
        y_velocity = velocity
        while y_coord > y_range[0]:
            step_number += 1
            y_coord += y_velocity
            y_velocity -= 1
            if y_coord >= y_range[0] and y_coord <= y_range[-1] and step_number >= x_velocities[0]:
                y_velocities.append(y_velocity)

    return y_velocities



if __name__ == '__main__':
    main()

