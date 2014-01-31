BSPS-win64.zip : bullshit.py
	/cygdrive/c/python33/python.exe setup.py build
	mv build/* ../win64
	rm -r build/ __pycache__/
	cd .. && zip -r BSPS-win64.zip win64 src README.md LICENSE
	rm -r ../win64
