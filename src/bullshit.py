# The Bullshit Performance Index
# Python Implimentation

import time
import os
import argparse

filename = "bull.shit"
version = "0.4.0"
max = 50000000

def main():
    global write_file
    global f

    setup_argparse()
    if not args.verbose:
        print_banner()

    if args.newline:
        bullshit_string = "bullshit\n"
    else:
        bullshit_string = "bullshit"
    
    write_file = (not args.verbose) or (args.keep or args.force)

    if write_file: 
        f = open(filename, "w") 

    start_time = time.time()

    for i in range(0, 10):
        if args.verbose and not args.newline:
            one_tenth_print(bullshit_string)
        elif args.verbose and args.newline:
            one_tenth_print_newline(bullshit_string)
        else:
            one_tenth_write(f, bullshit_string)

        if not args.terse:
            print str((i+1) * 10) + "%"

    if write_file:
        final_time = time.time() - start_time
        print(final_time)

    if write_file:
        f.close()

    if not args.keep and write_file:
        os.remove(filename)

def setup_argparse():
    global parse
    global args

    parse = argparse.ArgumentParser(description="Measure your computer's performance with bullshit!")

    verbosity = parse.add_mutually_exclusive_group()

    verbosity.add_argument("-v", "--verbose", action="store_true", help="Prints all of the bullshit to the console. Not recommended - very, very slow.")
    verbosity.add_argument("-t", "--terse", action="store_true", help="Allow only the score to be written to the console")

    parse.add_argument("-k", "--keep", action="store_true", help="Keeps the \"{0}\" file for your use".format(filename))
    parse.add_argument("-n", "--newline", action="store_true", help="Uses a newline character after each word")
    parse.add_argument("-f", "--force", action="store_true", help="Forces the program to write the \"{0}\" file. Use this with verbose flag.".format(filename))
    
    args = parse.parse_args()
    
def one_tenth_write(file, bullshit):
    loop_size = max / 10
    for i in range(0, loop_size):
        file.write(bullshit)

def one_tenth_print(bullshit):
    if write_file:
        one_tenth_write(f, bullshit)

    loop_size = max / 10
    for i in range(0, loop_size):
        print "bullshit",

def one_tenth_print_newline(bullshit):
    if write_file:
        one_tenth_write(f, bullshit)

    loop_size = max / 10
    for i in range(0, loop_size):
        print "bullshit"
        
def print_banner():
    if not args.terse or not args.verbose:
        print("Bullshit Performance Standard Benchmarking Utility")
        print("Version " + version)

if __name__ == "__main__":
    main()
