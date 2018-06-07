with open("C:/Users/shara/Documents/test1.txt","r") as f:
    for line in f:
        data1 = line.strip()
        data = line.strip().split()
        print(data1, len(data))




