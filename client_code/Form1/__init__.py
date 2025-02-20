from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random
import time



class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.player_1.role=None
    self.player_2.role=None
    self.images=[]
    
    
    


  def button_roll_click(self, **event_args):
    # self.images represents dice (images) to be rolled
    # If no dice selected, roll all the dice (images)
    if self.images==[]:
      self.images = [self.image_1,self.image_2,self.image_3,self.image_4,self.image_5]
    for image in self.images:
      self.roll_dice(image)
    self.images.clear()
    self.button_roll.text = "ROLL ALL DICE"

  
  def roll_dice(self, image):
    image.source = None
    dice = ['_/theme/1.png','_/theme/2.png','_/theme/3.png','_/theme/4.png','_/theme/5.png','_/theme/6.png']
    image_number = random.choice(dice)
    time.sleep(0.2)
    image.source = image_number
    image.visible = True


  def player_1_click(self, **event_args):
    self.item = app_tables.table_1.get(name="player1")
    self.player_1.role="selected"
    self.player_2.role=None
    

  def player_2_click(self, **event_args):
    self.item = app_tables.table_1.get(name="player2")
    self.player_1.role=None
    self.player_2.role="selected"

  def clear_scores(self):
    app_tables.table_1.delete_all_rows()
    app_tables.table_1.add_row(name="player1")
    app_tables.table_1.add_row(name="player2")

  def button_new_click(self, **event_args):
    """This method is called when the New Game button is clicked"""
    self.clear_scores()
    self.item = app_tables.table_1.get(name="player1")
    self.player_1.role="selected"
    self.player_2.role=None

  def link_1_click(self, **event_args):
   self.image_click(self.image_1)


  def link_2_click(self, **event_args):
    self.image_click(self.image_2)

  def link_3_click(self, **event_args):
    self.image_click(self.image_3)

  def link_4_click(self, **event_args):
    self.image_click(self.image_4)

  def link_5_click(self, **event_args):
    self.image_click(self.image_5)

  def image_click(self, image):
    image.visible = False
    self.images.append(image)
    self.button_roll.text="Roll Selected Dice"

  


    
    


