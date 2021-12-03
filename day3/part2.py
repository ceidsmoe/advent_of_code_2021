if __name__ == "__main__":
    with open("input") as f:
        ones = [0] * 12
        num_lines = 0
        for line in f.readlines():
            num_lines += 1
            for i, bit in enumerate(line):
                if bit == '1':
                    ones[i] += 1
        
        oxygen = 0
        co2 = 0
        for i, bit in enumerate(ones):
            if bit >= (num_lines/2):
                oxygen |= (1 << (11 - i))
            else:
                co2 |= (1 << (11 - i))
        
        print(oxygen, co2, oxygen * co2)