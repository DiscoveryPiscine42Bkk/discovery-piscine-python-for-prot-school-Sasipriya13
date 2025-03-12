import sys
def doecase_it(text):
    return text.lower()
def main():
    if len(sys.argv) == 1:
        print("none")
    else:
        for param in sys.argv[1:]:
            print(doencase_it(param))
if __name__ == "__main__":
    main()