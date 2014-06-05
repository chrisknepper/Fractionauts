from gettext import gettext as _

import sys
from gi.repository import Gtk
import pygame

import sugar3.activity.activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.graphics.toolbutton import ToolButton
from sugar3.activity.widgets import StopButton

import sugargame
import sugargame.canvas
import Main


class FractionautsActivity(sugar3.activity.activity.Activity):
	def __init__(self, handle):
		sugar3.activity.activity.Activity.__init__(self, handle)
		self.activity = Main.Main()
		self.activity.run()
		# The execution of this class pauses until the game is exited from game main menu
		# Exit completely, skipping save for now
		self.close()
	
	def can_close(self):
		pygame.quit()
		return True