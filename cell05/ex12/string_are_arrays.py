import sys
if len(sys.argv) == 2:
    input_string = sys.argv[1]
    count_z = input_string.count('z')
    if count_z > 0:
        for _ in range(count_z):
            print("z")
    else:
        print("none")
else:
    print("none")