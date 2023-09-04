from pivy import coin
import FreeCAD

PATH = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macro").GetString("MacroPath")+"/easy_reflections/"

class EasyReflector:
    def __init__(self, obj):
        obj.addProperty("App::PropertyEnumeration", "Environment","EasyReflector","Select Environment (white = None)")
        obj.addProperty("App::PropertyBool","Refresh","EasyReflector","Set to True to refresh textures after reloading file.\n(Resets self back to False.)").Refresh=False
        obj.Environment = ["image file","none","interior","industrial","mesh2","outside","studio","workshop"]
        obj.Environment = "studio"
        obj.addProperty("App::PropertyLinkList","LinkedObjects","EasyReflector","Objects to apply textures to")
        obj.addProperty("App::PropertyFile","ImageFile","EasyReflector","Image file to use for environment")
        obj.setEditorMode("ImageFile", 2) #hide by default
        obj.Proxy = self

    def execute(self,fp):
        if not fp.LinkedObjects:
            return
        self.setEnvironment(fp, fp.Environment)

    def onChanged(self,fp,prop):
        if not fp:
            return
        if prop == "Refresh" and fp.Refresh == True:
            fp.Refresh = False
        elif prop == "Environment":
            if fp.Environment == "image file":
                fp.setEditorMode("ImageFile", 0) #normal mode
            else:
                fp.setEditorMode("ImageFile", 2) #hide
        
    def setEnvironment(self, fp, env):
        tex = coin.SoTexture2()
        if env == "image file":
            tex.filename = fp.ImageFile
        else:
            if fp.Environment == "none":
                tex.filename = PATH + "white.jpg"
            else:
                tex.filename = PATH + fp.Environment + ".jpg"
        tc = coin.SoTextureCoordinateEnvironment()
        linked = fp.LinkedObjects
        if not linked:
            return
        for link in linked:
            rootnode = link.ViewObject.RootNode
            child1 = rootnode.getChild(1)
            child2 = rootnode.getChild(2)
            already_done = "SoTexture2" in str(type(child1)) and "SoTextureCoordinateEnvironment" in str(type(child2))
            if already_done:
                rootnode.replaceChild(1, tex)
                rootnode.replaceChild(2, tc)
            else:
                rootnode.insertChild(tex,1) 
                rootnode.insertChild(tc,2)




