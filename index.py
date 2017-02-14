# GET Speed
# 
# Author:
#   nobe4 (Victor Haffreinge)
#
# Usage:
#   python <this> <https?://hostname>
#
# You can stop the program with <C-C> (That's CTRL + C).
#
# Result will be displayed and appened to results.txt.
# e.g.
#   python index.py http://google.com

import sys
import requests

# Use default timer
# ref: http://stackoverflow.com/a/25823885/2558252
from timeit import default_timer as timer

# File use to append the stats
file = open("result.txt", "a")

def p(s):
    ''' Print to the screen and write to the file. '''
    print s
    file.write(s + "\n")

def get(url):
    ''' Get the url, print a stat line and return the timing for that request. '''
    start = timer()
    r = requests.get(url)
    diff = timer() - start

    # Print the time, the status code and a fancy graph.
    p("{}\t\t{}\t{}".format(diff, r.status_code, "|"*int(diff * 10)))

    # Return the diff time for average computation.
    return diff

def main(url):
    ''' Main function, print header and loop to infinity and beyond. '''

    # Used for average computation
    total = 0
    count = 1

    # Print header
    p("Stats for : {}".format(url))
    p("Time\t\t\tStatus\tFanciness")
    p("-"*50)

    try:
        # Looping until
        while True:
            total += get(url)
            count += 1
    except KeyboardInterrupt:
        # Don't hang up on ^C, instead print this.
        p("\nAverage over {} request{}: {}".format(count-1,  "s" if count > 2 else "", total/float(count)))


if __name__ == "__main__":

    # We need an url...
    if len(sys.argv) == 1:
        print "Usage: {} <url (with protocol)>".format(sys.argv[0])
    else:
        # Don't write that in the results.
        print "Cancel with CTRL-C...\n\n"

        # Let's go!
        main(sys.argv[1])

