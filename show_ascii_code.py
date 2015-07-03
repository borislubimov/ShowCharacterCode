# -*- coding: utf-8 -*-
import sublime_plugin


class ShowAsciiCodeCommand(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        self.show_ascii_code(view)

    def on_activated(self, view):
        self.show_ascii_code(view)    

    def show_ascii_code(self, view):    
        selected = view.substr(view.sel()[0].a)
        view.set_status('asciicode', "ASCII {0}".format(ord(selected)))