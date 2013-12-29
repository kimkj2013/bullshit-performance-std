# The Bullshit Performance Index
# Python Implimentation

import time
import os
import argparse

filename = "bull.shit"
version = "0.3-alpha"
max = 50000000

def main():
    setup_argparse()
    print_banner()

    if args.newline:
        bullshit_string = "bullshit\n"
    else:
        bullshit_string = "bullshit"
    
    f = open(filename, "w") 

    start_time = time.time()

    for i in range(0, 10):
        if args.verbose and not args.newline:
            one_tenth_print(f, bullshit_string)
        if args.verbose and args.newline:
            one_tenth_print_newline(f, bullshit_string)
        else:
            one_tenth_write(f, bullshit_string)

        print str((i+1) * 10) + "%"

    final_time = time.time() - start_time
    print(final_time)

    f.close()

    if not args.keep:
        os.remove(filename)

def setup_argparse():
    global parse
    global args

    parse = argparse.ArgumentParser(description="Measure your computer's performance with bullshit!")

    parse.add_argument("-k", "--keep", action="store_true", help="Keeps the \"{0}\" file for your use".format(filename))
    parse.add_argument("-v", "--verbose", action="store_true", help="Prints all of the bullshit to the console. Not recommended - very, very slow.")
    parse.add_argument("-n", "--newline", action="store_true", help="Uses a newline character after each word")
    
    args = parse.parse_args()
    
def one_tenth_write(file, bullshit):
    loop_size = max / 10
    for i in range(0, loop_size):
        file.write(bullshit)

def one_tenth_print(file, bullshit):
    loop_size = max / 10
    for i in range(0, loop_size):
        file.write(bullshit)
        print "bullshit",

def one_tenth_print_newline(file, bullshit):
    loop_size = max / 10
    for i in range(0, loop_size):
        file.write(bullshit)
        print "bullshit"
        
def print_banner():
    print("Bullshit Performance Standard Benchmarking Utility")
    print("Version " + version)

if __name__ == "__main__":
    main()
