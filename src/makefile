BSPS-win32.zip : bullshit.py
	/cygdrive/c/python27/python.exe setup.py py2exe
	rm -r build
	mv dist ../win32
	cd .. && zip -r BSPS-win32.zip win32 src README.md LICENSE
	rm -r ../win32
