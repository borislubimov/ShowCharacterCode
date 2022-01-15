# -*- coding: utf-8 -*-
import sublime_plugin


class ShowCharCodeCommand(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        self.show_char_code(view)

    def on_activated(self, view):
        self.show_char_code(view)

    def show_char_code(self, view):
        selection = view.sel()
        if len(selection) == 0:
            view.erase_status('charcode')
            return
        selected = view.substr(selection[0].a)
        view.set_status('charcode',
                        "DEC {0}, HEX {0:#x}, BYTE {1}".format(ord(selected), selected.encode('unicode_escape')))
