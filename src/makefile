dist/bs.exe : bs.py
	/cygdrive/c/python27/python.exe setup.py py2exe
	rm -r build
	rsync -a dist/* ../bin/WIN32
