with open("./2022/day6/day6_input") as datafile:
    data = datafile.read()

for i in range(3, len(data)):
    test_set = set()
    test_set.update([data[i], data[i-1], data[i-2], data[i-3]])
    if len(test_set) == 4:
        print(f"Number of characters until first start of packet: {i+1}")
        print(test_set)
        break

for i in range(13, len(data)):
    test_set = set()
    test_list = []
    for j in range(13, -1, -1):
        test_list.append(data[i-j])
    test_set.update(test_list)
    # print(test_set)
    if len(test_set) == 14:
        print(f"Number of characters until first start of message: {i+1}")
        print(test_set)
        break
