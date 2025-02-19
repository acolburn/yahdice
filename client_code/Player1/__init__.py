from ._anvil_designer import Player1Template
from anvil import *


class Player1(Player1Template):
  def __init__(self, **properties):
    self.item = {
      'ones': 0,
      'twos': 0,
      'threes': 0,
      'fours': 0,
      'fives': 0,
      'sixes': 0,
    }
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    


  

