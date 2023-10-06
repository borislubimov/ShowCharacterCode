# -*- coding: utf-8 -*-
import sublime
import sublime_plugin


SETTINGS_FILE = 'ShowCharacterCode.sublime-settings'
SETT_MODE = 'mode'
STATUS_CHARCODE = 'charcode'

SHOW_OFF = 0
SHOW_HEX_ONLY = 1
SHOW_HEX_AND_DEC = 2

_settings = None


def show_character_code(view):
    global _settings
    if _settings is None:
        _settings = sublime.load_settings(SETTINGS_FILE)
    if not _settings.has(SETT_MODE):
        _settings.set(SETT_MODE, SHOW_HEX_AND_DEC)
    # sublime.status_message('char_code_mode : %s' % str(_settings.get(SETT_MODE)))
    if _settings.get(SETT_MODE) == SHOW_OFF:
        return
    selection = view.sel()
    if len(selection) == 0:
        view.erase_status(STATUS_CHARCODE)
        return
    selected = view.substr(selection[0].a)
    char_code = ord(selected)
    if _settings.get(SETT_MODE) == SHOW_HEX_ONLY:
        fmt_str = '0x{0:02X}' if char_code <= 0xFF else '0x{0:04X}' if char_code <= 0xFFFF else '0x{0:06X}'
        view.set_status(STATUS_CHARCODE, fmt_str.format(char_code))
    else:
        view.set_status(STATUS_CHARCODE,
                        "DEC {0}, HEX {0:#x}, BYTE {1}".format(char_code, selected.encode('unicode_escape')))


class ShowCharCodeListener(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        self.show_char_code(view)

    def on_activated(self, view):
        self.show_char_code(view)

    def show_char_code(self, view):
        show_character_code(view)


class ShowCharacterCodeCommand(sublime_plugin.WindowCommand):
    def run(self, mode=SHOW_OFF):
        global _settings
        if _settings is None:
            _settings = sublime.load_settings(SETTINGS_FILE)
        _settings.set(SETT_MODE, mode)
        sublime.save_settings(SETTINGS_FILE)
        if mode == SHOW_OFF:
            self.window.active_view().erase_status(STATUS_CHARCODE)
        else:
            show_character_code(self.window.active_view())
