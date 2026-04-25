import sys
if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("none")
    else:
        args = sys.argv[1:]
        for arg in reversed(args):
            print(arg)