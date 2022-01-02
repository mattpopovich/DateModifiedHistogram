# DateModifiedHistogram
Displays a 24hr histogram based on when the files in the folder selected were modified. Made this for my dad so that he can analyze when there is activity on his trailcam 😂

# Create an executable to be used on Windows: 
My dad doesn't know anyting about Python, let alone computers. Let's make an executable for him to easily use. 

First, install pyinstaller -  `pip install pyinstaller`, then run
```
$ cd DateModifiedHistogram
$ pyinstaller DateModifiedHistogram.py --onefile
```
This will generate `DateModifiedHistogram.exe` in the `dist` folder that gets created (if ran in Windows, not sure what happens if you run `pyinstaller` on Linux/Mac). 

