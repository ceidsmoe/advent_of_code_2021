if __name__ == "__main__":
    with open("example") as f:
        valid_lines = []

        for line in f.readlines():
            start, end = line.split(" -> ")
            startx, starty = start.split(",")
            endx, endy = end.split(",")
            if int(startx) == int(endx) or int(starty) == int(endy):
                valid_lines.append([[int(startx), int(starty)], [int(endx), int(endy)]])
                

        intersections = 0

        for i in range(len(valid_lines)):
            startx_i, starty_i = valid_lines[i][0]
            endx_i, endy_i = valid_lines[i][1]

            if i < len(valid_lines)-1:
                for j in range(i+1, len(valid_lines)):
                    startx_j, starty_j = valid_lines[j][0]
                    endx_j, endy_j = valid_lines[j][1]


                    print("i: (", startx_i, starty_i, ") -> (", endx_i, endy_i, ")")
                    print("j: (", startx_j, starty_j, ") -> (", endx_j, endy_j, ")")

                    # check if horizon + vertical
                    # i is vertical j is horizontal
                    if startx_i == endx_i and starty_j == endy_j:
                        if (starty_i <= starty_j <= endy_i or starty_i >= starty_j >= endy_i) and (startx_j <= startx_i <= endx_j or startx_j >= startx_i >= endx_j):
                            print("horiz + vert")
                            intersections += 1

                    # i is horiz j is vertical 
                    if starty_i == endy_i and startx_j == endx_j:
                        if (startx_i <= startx_j <= endx_i or startx_i >= startx_j >= endx_i) and (starty_j <= starty_i <= endy_j or starty_j >= starty_i >= endy_j):
                            print("horiz + vert")                            
                            intersections += 1
                    
                    # check if both vertical
                    if startx_i == endx_i == startx_j == endx_j:
                        if starty_i <= starty_j <= endy_i:
                            intersections += (endy_i+1 - starty_j)
                        elif starty_j <= starty_i <= endy_j:
                            intersections += (endy_j+1 - starty_i)
                        print("vert")
                    # check if horizontal
                    if starty_i == endy_i == starty_j == endy_j:
                        if startx_i <= startx_j <= endx_i:
                            intersections += (endx_i+1 - startx_j)
                        elif startx_j <= startx_i <= endx_j:
                            intersections += (endx_j+1 - startx_i)
                        elif startx_i <= endx_j <= endx_i:
                            intersections += (endx_i+1 - endx_j)
                        print("horizon")

                    print("------------------------------")
        
        print(intersections)
            