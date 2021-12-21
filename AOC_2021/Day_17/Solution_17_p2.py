import numpy as np

#Example: target area: x=20..30, y=-10..-5
#Input: target area: x=111..161, y=-154..-101
def main():
    #Example
    # target_zone_definition = [[20,-10], [30,-5]]
    #Input
    target_zone_definition = [[111,-154],[161,-101]]

    x_range = [target_zone_definition[0][0], target_zone_definition[1][0]]
    y_range = [target_zone_definition[0][1], target_zone_definition[1][1]]

    minimum_x, maximum_x = X_Limits(x_range)
    x_velocities = X_Velocities(minimum_x, maximum_x, x_range)
    minimum_y, maximum_y = Y_Limits(y_range)
    all_velocities = Velocity_Pairs(minimum_y, maximum_y, x_range, y_range, x_velocities)
    
    total = Count_Velocities(all_velocities)
    print(total)

#Finds the minimum and maximum starting x velocities that will hit within the range
def X_Limits(x_range):

    maximum_x = x_range[1]

    x_coord = 0
    x_velocity = 0
    x_velocities = []

    while x_coord < x_range[1]:
        x_velocity += 1
        x_coord += x_velocity
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
            if x_coord <= x_range[1] and x_coord >= x_range[0]:
                x_velocities.append(x)
                break

    return x_velocities


#x_velocity is in the following form: x_velocity, step_where_it's_in_range
def Y_Limits(y_range):
    maximum_y = abs(y_range[0]) - 1
    minimum_y = y_range[0]

    return minimum_y, maximum_y


def Velocity_Pairs(min_y, max_y, x_range, y_range, x_velocities):

    velocity_dict = {}

    for x in x_velocities:
        for y in range(min_y, max_y+1):
            x_loc = 0
            y_loc = 0
            x_vel = x
            y_vel = y
            while y_loc > y_range[0]:
                if x_vel > 0:
                    x_loc += x_vel
                    x_vel -= 1
                y_loc += y_vel
                y_vel -= 1
                if y_loc >= y_range[0] and y_loc <= y_range[1] and x_loc >= x_range[0] and x_loc <= x_range[1]:
                    try:
                        if y not in velocity_dict[x]:
                            velocity_dict[x].append(y)
                    except Exception:
                        velocity_dict[x] = [y]
                    break

    return velocity_dict


def Count_Velocities(dictionary):
    total = 0

    for term in dictionary:
        total += len(dictionary[term])

    return total


if __name__ == '__main__':
    main()

