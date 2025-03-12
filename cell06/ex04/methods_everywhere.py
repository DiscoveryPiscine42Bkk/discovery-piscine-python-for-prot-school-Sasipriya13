import sys
def shrink(text):
    print(text[:8])
def main():
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            shrink(arg)
    else:
        print("none")
if __name__ == "__main__":
    main()