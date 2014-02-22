#! /usr/bin/env python3

"""
The Bullshit Performance Index
Python Implimentation
Copyright 2014 Nathan Mara

This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see http://www.gnu.org/licenses/gpl.txt

All outputted bullshit licensed under
Creative Commons Attribution-NonCommercial license
http://creativecommons.org/licenses/by-nc/4.0/
"""

import time
import os
import argparse

filename = "bull.shit"

version_major = 0
version_minor = 6
version_patch = 0

version = str(version_major) + "."
version += str(version_minor)
version += "." + str(version_patch)

license_info = """
Copyright 2014 Nathan Mara
This program licensed under GNU GPLv3
All outputted bullshit licensed under CC BY-NC
"""

max = 50000000


def main():
	"""

	"""

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
		f = open(filename, "w", encoding="ascii")

	start_time = time.time()

	for i in range(0, 10):
		if args.verbose and not args.newline:
			one_tenth_print(bullshit_string)
		elif args.verbose and args.newline:
			one_tenth_print_newline(bullshit_string)
		else:
			one_tenth_write(f, bullshit_string)

		if not args.terse:
			print(str((i + 1) * 10) + "%")

	if write_file:
		final_time = time.time() - start_time
		print(final_time)

	if write_file:
		f.close()

	if not args.keep and write_file:
		os.remove(filename)


def setup_argparse():
	"""
	sets up the objects necessary for argparse to parse the command line arguments
	"""

	global parse
	global args

	parser_description = "Measure your computer's performance with bullshit!"

	help_verbose = "Prints all of the bullshit to the console."
	help_verbose += " Not recommended - very, very slow."
	help_terse = "Allow only the score to be written to the console"
	help_keep = "Keeps the \"%s\" file for your use" % filename
	help_newline = "Uses a newline character after each word"
	help_force = "Forces the program to write the \"%s\" file."
	help_force += " Use this with verbose flag." % filename

	parse = argparse.ArgumentParser(description=parser_description)

	verbosity = parse.add_mutually_exclusive_group()

	verbosity.add_argument("-v", "--verbose", action="store_true", help=help_verbose)
	verbosity.add_argument("-t", "--terse", action="store_true", help=help_terse)

	parse.add_argument("-k", "--keep", action="store_true", help=help_keep)
	parse.add_argument("-n", "--newline", action="store_true", help=help_newline)
	parse.add_argument("-f", "--force", action="store_true", help=help_force)

	args = parse.parse_args()


def one_tenth_write(file, bullshit):
	"""
	writes one-tenth of the specified bullshit to the file
	"""
	loop_size = int(max / 10)
	for i in range(0, loop_size):
		file.write(ascii(bullshit))


def one_tenth_print(bullshit):
	"""
	Prints one-tenth of the specified bullshit to the screen. If the file is to
	be written, specified by the command line arguments, then it is.
	"""
	if write_file:
		one_tenth_write(f, bullshit)

	loop_size = int(max / 10)
	for i in range(0, loop_size):
		print("bullshit",)


def one_tenth_print_newline(bullshit):
	"""
	Prints one-tenth of the specified bullshit to the screen with newline
	characters. If the file is to be written, specified by the command line
	arguments, then it is.
	"""
	if write_file:
		one_tenth_write(f, bullshit)

	loop_size = max / 10
	for i in range(0, loop_size):
		print("bullshit")


def print_banner():
	"""
	prints the banner at the beginning of the program's execution
	"""
	if not args.terse or not args.verbose:
		print("Bullshit Performance Standard Benchmarking Utility")
		print("Version " + version)
		print(license_info)

if __name__ == "__main__":
	main()
