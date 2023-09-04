# EasyReflector
Easily manage textures in FreeCAD

<img src="screenshot01.png">

## Toolbar Icon
<img src="EasyReflectorIcon.svg">

## Credits
Based on this repo: https://github.com/Athanaze/Freecad-easy-reflections
I just made it into a feature python object that would be persistent between FreeCAD sessions and added the capability to specify custom texture files.

## Installation
Put the EasyReflector.FCMacro file into your macros folder.  It will create the easyreflector.py file for you and also it will download the image texture files and place them into your macros/easy_reflections folder.

## Usage

Select the object you wish to apply the texture to, and then run the EasyReflector.FCMacro macro.  (Do not run the EasyReflector.py file as it is imported by the .FCMacro file and by FreeCAD when you load a document containing one of the EasyReflector objects.)

The studio texture is applied to the selected object(s) by default, but you can change that by editing the Environment property of the EasyReflector object.

Note: FreeCAD does not save the texture information, so when you reload the file you need to refresh the EasyReflector object by toggling the Refresh property from False to True.  This triggers a refresh, reapplying your texture to your objects.  The Refresh property then toggles itself back to False, ready for the next usage.

You can also use your own image file for the texture instead of the files provided here.  To do this, choose the "image file" option for the Environment.  This makes visible the "Image File" property, which you can use to select your image file to apply.  The file can reside in any directory.

## ChangeLog
### 0.2023.09.04b -- added view provider and icons
Now can accept drag and drop
Untextures its LinkedObjects upon deletion
Dynamic icon change upon enabling/disabling
Enable/Disable via double click
### 0.2023.09.04 -- now creates .py file automatically, and also downloads images and puts them in macros/easy_reflections folder
adds ability to put new .jpg files into the easy_reflections folder, the Environment property automatically updates for new EasyReflector objects
### 0.2023.09.03 -- initial uploaded version

