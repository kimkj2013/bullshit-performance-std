../win32/bullshit.exe : bullshit.py
	/cygdrive/c/python27/python.exe setup.py py2exe
	rm -r build
	rsync -a dist/* ../win32
	rm -r dist
