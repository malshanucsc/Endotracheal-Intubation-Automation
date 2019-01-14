def getNextDirection(new_location, movement_type):
    if movement_type == "forward":

        if (new_location == 2 or new_location == 7):
            # bend the  tube downward due to curves in the nasal  cavity and trachea
            return 1
        elif new_location == 4:
            # due to sensitivity in this area tracheal opening close and open quickly.
            #  waiting sometimes there will stabilize the opening
            return 2
        elif new_location == 5:
            # when tracheal openning closed it always tend to close it a obstacle is near the opening
            return 3
        elif new_location == 8:
            # reduce touching with wall of wind pipe spirals to reduce bleedings
            return 4
        elif new_location == 9:
            # if sped is high and miss the location 10 tube will move further and then it is difficult to capture due to locations beyond 10 is similar as 8-10
            return 5
        elif new_location == 10:
            # since intubation tube should stop 2cm above to spread air for both lungs
            return 6
        else:
            return 7

    if movement_type == "backward":
        if (new_location == 2 or new_location == 7):
            # bend the  tube upward due to curves in the nasal  cavity and trachea
            return 8
        else:
            return 9