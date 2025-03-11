import sys
if len(sys.argv) > 1:
    for param in sys.argv[1:]:
        if not param.endswith('ism'):
            print(param + 'ism')
else:
    print("none")