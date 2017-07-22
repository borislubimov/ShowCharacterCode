# -*- coding: utf-8 -*-
import sublime_plugin


class ShowCharCodeCommand(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        self.show_char_code(view)

    def on_activated(self, view):
        self.show_char_code(view)

    def show_char_code(self, view):
        selected = view.substr(view.sel()[0].a)
        view.set_status('charcode', "Char Code: {0} | {0:#x} | {0:b}".format(ord(selected)))