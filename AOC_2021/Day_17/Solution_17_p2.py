import re
import copy

#Example: target area: x=20..30, y=-10..-5
#Input: target area: x=111..161, y=-154..-101
def main():
    #Example
    target_zone_definition = [[20,-10], [30,-5]]
    #Input
    # target_zone_definition = [[111,-154],[161,-101]]

    x_range = [target_zone_definition[0][0], target_zone_definition[1][0]]
    y_range = [target_zone_definition[0][1], target_zone_definition[1][1]]

    minimum_x, maximum_x = X_Limits(x_range)
    x_velocities = X_Velocities(minimum_x, maximum_x, x_range)
    minimum_y, maximum_y = Y_Limits(y_range)
    y_velocities = Y_Velocities(minimum_y, maximum_y, y_range)

#Finds the minimum and maximum starting x velocities that will hit within the range
def X_Limits(x_range):

    maximum_x = x_range[1]

    x_coord = 0
    x_velocity = 0
    x_velocities = []

    while x_coord < x_range[1]:
        x_coord += x_velocity
        x_velocity += 1
        if x_coord >= x_range[0] and x_coord <= x_range[1]:
            minimum_x = x_velocity
            break

    return minimum_x, maximum_x


#Uses the limits found above and finds which initial velocities in the range have points within the range
def X_Velocities(minimum_x, maximum_x, x_range):

    x_velocities = []

    for x in range(minimum_x, maximum_x+1):
        x_velocity = x
        x_coord = 0
        while x_coord < x_range[1]:
            x_coord += x_velocity
            x_velocity -= 1
            if x_coord <= maximum_x and x_coord >= minimum_x:
                x_velocities.append([x,x-x_velocity])
                break

    return x_velocities


#x_velocity is in the following form: x_velocity, step_where_it's_in_range
def Y_Limits(y_range, x_velocity):
    maximum_y = y_range[0] - 1




def Y_Velocities(minimum_y, maximum_y, y_range):
    pass



if __name__ == '__main__':
    main()

