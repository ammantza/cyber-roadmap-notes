# log_parser.py

import sys

def parse_log(path):

    total = 0
    errors = 0

    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            total +1
            if 'ERROR' in line:
                errors += 1

    print(f"Total lines: {total}")
    print(f"Line with ERROR: {errors}")

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: python3 log_parser.py <logfile>")
        else:
            parse_log(sys.argv[1])