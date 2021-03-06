# The Bullshit Performance Standard (BSPS)#
#### Original Code and Concept by Nate Mara and Daltin Loomis ####
##### Honorable Mention goes to John Shaver #####

## Our Mission ##

We realize that there are many ways for current computer users to measure their
computer's performance. These include, but are not limited to:

- The Windows Performance Index
- Their processor's clock speed
- How fast Facebook loads
- How good their games look
- Prime95
- Etc.

You get the idea. We saw all of this and realized something: it's all bullshit!
We thought that we should just cut the shit and get straight to the point: for
all but the most intensive users, performance benchmarks are __bullshit__. So
we created _The Bullshit Performance Standard_ to fit nicely in with the
others.

## How Does it Work? ##

_The Bullshit Performance Standard_ uses a very advanced method of quantifying
your machine's performance. The method is described in detail below.

1. When the program begins, a new file is created ("bull.shit")
2. The program writes 50,000,000 copies of the string "bullshit" to this file
3. The time that this operation takes is printed to the console
4. The file is deleted

The time that is given to the user at the end of the benchmark's execution is
your machine's BSPS score, or BSPSS.

## Useage ##

To get this ~~fantastic~~ ~~astounding~~ ~~majestic~~ ~~bullshit~~ fantastic
benchmarking suite onto your machine and start testing, follow these steps:

### Windows users (without Python installed)
1. Grab a zip of the latest windows binaries from the releases tab
2. Run the BSPS
1. `cd BSPS-win32`
2. `cd win32`
3. `bullshit`
3. Brag about your score on the internet!

### \*Nix/Mac OSX/Windows users (with Python) ###
1. Download this repo
1. If you have Git installed: `git clone
   https://github.com/natemara/bullshit-performance-std`
	2. If you don't have Git installed, just download [the latest zip](https://github.com/natemara/bullshit-performance-std/zipball/master)
	   and extract it to a directory of your choosing.
2. Run the BSPS
	1. `cd bullshit-performance-std`
	2. `cd src`
	3. `python3 bullshit.py`
3. Brag about your score on the internet!

### Command Line flags ###

`-k` / `--keep` by default, upon completion, this program deletes the created
`bull.shit` file. Enabling this option will prevent this from happening so that
you are free to use the bullshit for your own nefarious purposes.

`-v` / `--verbose` this will print all 50 million strings of bullshit directly
to your console for your viewing pleasure. This is not recommended, as it will
take for fucking ever. Seriously, don't do this. If you really want to look at
all that bullshit, either watch the news or use the `-k` flag and view the
bullshit with Vim/less/more/cat. This is incompatible with the `--terse`
argument, as the options are inherently mutually exclusive. This will also
prevent the program from writing to the file, showing the banner, and
calculating the time. See the `--force` flag below for details.

`-f` / `--force` by default, when the `--verbose` flag is used, the output is
restricted to just bullshit. While there is not inherently anything wrong with,
this you may still want the `bull.shit` file to be created, and you may be
curious about the time that it takes. This flag will cause the normal behavior
of file writing and time printing to take place.

`-n` / `--newline` by default, this program will write the bullshit to the file
with no other characters, 100% pure, uncut bullshit. If you'd like your
bullshit to look a little nicer, use this flag, and a newline character will be
appended to each bullshit word, and you'll have one bullshit on each line.

`-t` / `--terse` this will restrict all output of the program to just the
BSPSS, excluding the banner, the version, and the percentage. This is useful
for scripts, for example you could write just the score to a file, along with
the date, so that you can accurately track your machine's bullshit
generation over time. This is incompatible with the `--verbose` argument,
as the options are inherently mutually exclusive.

## How is the BSPS licensed? ##

The licensing technique employed by the BSPS is somewhat different from
that which you may have seen before. The project is licensed under the
[Bullshit Foundation Document (BFD)](LICENSE).  Basically, this document
says that anyone is free to use, distribute, change, and distribute those
changes to anyone you wish. The output of the program however, must be
attributed back to this project, and it cannot be used for commercial gain
without express written consent of the original authors.
