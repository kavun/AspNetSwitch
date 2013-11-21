import sublime, sublime_plugin
import os.path

class SwitchAspxVbCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        name, real_ext = os.path.splitext(self.view.file_name())
        win = self.view.window()
        ext = real_ext.lower()
        if ext == ".aspx":
            win.open_file(name+ real_ext + ".vb")
        elif ext == ".ascx":
            win.open_file(name+ real_ext + ".vb")            
        elif ext == ".master":
            win.open_file(name+ real_ext + ".vb")
        elif ext == ".vb":
            name2, ext2 = os.path.splitext(name)
            if ext2 == ".designer":
                win.open_file(name2)
            else: 
                win.open_file(name)

class SwitchAspxDesignerVbCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        name, ext = os.path.splitext(self.view.file_name())
        win = self.view.window()
        if ext == ".aspx":
            win.open_file(name+".aspx.designer.vb")
        elif ext == ".vb":
            name2, ext2 = os.path.splitext(name)
            if ext2 == ".designer":
                win.open_file(name2)
            else: 
                win.open_file(name)
