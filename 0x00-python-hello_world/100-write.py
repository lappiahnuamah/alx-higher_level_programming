#!/usr/bin/python3
import sys

def main():
    message = "and that piece of art is useful - Dora Korpar, 2015-10-19"

    # Write the message to stderr
    sys.stderr.write(message + '\n')

    # Exit with status code 1
    sys.exit(1)

if __name__ == "__main__":
    main()
