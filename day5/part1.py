if __name__ == "__main__":
    with open("input") as f:
        for line in f.readlines():
            start, end = line.split(" -> ")
            startx, starty = start.split(",")
            endx, endy = end.split(",")