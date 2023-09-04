# EasyReflector
Easily manage textures in FreeCAD
## Credits
Based on this repo: https://github.com/Athanaze/Freecad-easy-reflections
I just made it into a feature python object that would be persistent between FreeCAD sessions and added the capability to specify custom texture files.
## Installation
Download the repository as a zip file and extract it into your Macro directory.  You should have the .FCMacro file and the .py file in your Macro folder and you should have a new folder in your Macro folder called easy_reflections, which will contain the .jpg files.

<pre>
Macro
  EasyReflector.FCMacro
  EasyReflector.py
  easy_reflections/white.jpg
  easy_reflections/studio.jpg
  ... etc.
</pre>

You only run the .FCMacro file.  The .py file is imported by the .FCMacro file and by FreeCAD when you reload a document containing one of the EasyReflector objects.


