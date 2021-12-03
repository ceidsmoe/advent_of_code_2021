if __name__ == "__main__":
    with open("input") as f:
        horizontal = 0
        depth = 0
        for line in f.readlines():
            direction, pos = line.split()
            if direction == "forward":
                horizontal += int(pos)
            elif direction == "up":
                depth -= int(pos)
            else:
                depth += int(pos)

        print(horizontal, depth, horizontal*depth)