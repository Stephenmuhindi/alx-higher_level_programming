#!/usr/bin/python3
import sys
''' adds all integers au'''
def main():
    arguments = sys.argv[1:]
    total = sum(int(arg) for arg in arguments)
    print(total)
if __name__ == "__main__":
    main()
