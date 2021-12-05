if __name__ == "__main__":
    with open("input") as f:
        binary_strings = []
        for line in f.readlines():
            binary_strings.append(line)
        
        # do o2 first
        old_array = list(binary_strings)
        new_array = [[], []]
        bit_count = 0
        
        while len(old_array) > 1:
            for line in old_array:
                if line[bit_count] == '0':
                    new_array[0].append(line)
                else:
                    new_array[1].append(line)
            if len(new_array[1]) >= len(new_array[0]):
                old_array = new_array[1]
            else: 
                old_array = new_array[0]
            
            bit_count += 1
            new_array = [[], []]
        
        oxygen = int(old_array[0], 2)

        # now do co2
        old_array = list(binary_strings)
        new_array = [[], []]
        bit_count = 0
        
        while len(old_array) > 1:
            for line in old_array:
                if line[bit_count] == '0':
                    new_array[0].append(line)
                else:
                    new_array[1].append(line)
            if len(new_array[1]) >= len(new_array[0]):
                old_array = new_array[0]
            else: 
                old_array = new_array[1]
            
            bit_count += 1
            new_array = [[], []]

        co2 = int(old_array[0], 2)

        print(oxygen, co2, oxygen * co2)