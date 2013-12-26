# The Bullshit Performance Standard (BSPS)#
#### Original Code and Concept by Nate Mara and Daltin Loomis ####
##### Honorable Mention goes to John Shaver #####

## Our Mission ##
We realize that there are many ways for current computer users to measure their computer's performance. These include, but are not limited to:
- The Windows Performance Index
- Their processor's clock speed
- How fast Facebook loads
- How good their games look
- Etc.

You get the idea. We saw all of this and realized something: it's all bullshit! We thought that we should just cut the shit and get straight to the point: for all but the most intensive users, performance benchmarks are __bullshit__. So we created _The Bullshit Performance Standard_ to fit nicely in with the others.

##How Does it Work?##
_The Bullshit Performance Standard_ uses a very advanced method of calculating performance for your machine. The method is described in detail below.

1. When the program begins, a new file is created ("bull.shit")
2. The program writes 50,000,000 copies of the string "bullshit" to this file
3. The time that this operation takes is printed to the console
4. The file is deleted

The time that is given to the user at the end of the benchmark's execution is your machine's BSPS score, or BSPSS.

##How to use?##
To get this fantastic benchmarking suite onto your machine and start testing, follow these steps: 

### Windows users (without Python installed)
1. Grab a zip of the latest windows binaries from the releases tab
2. Run the BSPI
	1. `cd BSPS-win32`
	2. `cd win32`
	3. `bullshit`
3. Brag about your score on the internet!

### \*Nix/Mac OSX/Windows users (with Python) ###
1. Clone the repo: `git clone https://github.com/natemara/bullshit-performance-std.git` 
2. Run the BSPI
	1. `cd bullshit-performance-std`
	2. `cd src`
	3. `python bullshit.py`
3. Brag about your score on the internet!

### Command Line flags ###
`-k` `--keep` this will prevent the program from deleting the created `bull.shit` file, so that you are free to use it for your own nefarious purposes.

`-v` `--verbose` this will print all 50 million strings of bullshit directly to your console for your viewing pleasure. This is not recommended, as it will take for fucking ever. Seriously, don't do this. If you really want to look at all that bullshit, either watch the news or use the `-k` flag and view the bullshit with Vim/less/more/cat

`-n` `--newline` by default, this program will write the bullshit to the file with no other characters, 100% pure, uncut bullshit. If you'd like your bullshit to look a little nicer, use this flag, and a newline character will be appended to each bullshit word, and you'll have one bullshit on each line.

## What if I just need a bunch of bullshit? ##
We understand that there are circumstances in which you just need a lot of bullshit for what you're doing. The right job calls for the right tools. Say you are:
* Working on a last minute term paper
* Trying to come up with an excuse
* Writing a politician's campaign speech
* Or just in doubt that this program actually generates 50 million lines of pure bullshit

_The Bullshit Performance Standard_ is perfectly equipped to meet your needs. When you are running the benchmarking utility, simply pass the command line flag `-k` for "keep." This will cause the program to go through the regular sequence of benchmarking your machine, but with the added side effect of not deleting those 50 million lines of bullshit. Once the program is done, you will find a file, `bull.shit` in the same directory as the program. You are free to do with this as you wish, simply attribute the bullshit to this project.
