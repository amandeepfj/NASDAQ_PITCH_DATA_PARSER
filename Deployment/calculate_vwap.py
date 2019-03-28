# Created by Amandeep
# "We are drowning in information, while starving for wisdom - E. O. Wilson"

# !/usr/bin/python

import sys
import os.path
import vwap
import time


def main(argv):
    if len(argv) == 1:
        itch_file_name = argv[0]
        if os.path.isfile(itch_file_name):
            start = time.time()
            vwap.calculate_vwap(itch_file_name)
            end = time.time()
            print("Time taken to execute(in seconds) = " + str(end - start))
        else:
            raise Exception('User Error - File not located at the location mentioned in argument')
    else:
        raise Exception('User Error - Invalid number of arguments passed!!')


if __name__ == "__main__":
    main(sys.argv[1:])