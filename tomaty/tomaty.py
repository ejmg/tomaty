"""
tomaty.py
~~~~~~~~

stub code for tomaty.py


TODO: everything

:copyright: @ 2018
:author: elias julian marko garcia
:license: MIT, see LICENSE
"""
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, GLib


def tomaty():
    t = Timer()
    t.connect('delete-event', Gtk.main_quit)
    t.show_all()
    Gtk.main()
