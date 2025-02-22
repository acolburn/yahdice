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
    # self.player_1.role=None
    # self.player_2.role=None
    self.player_1_click()
    self.images=[]

    
  def player_1_click(self, **event_args):
    """This method is called when the Player1 link in the navigation pain is clicked"""
    self.item = app_tables.table_1.get(name="player1")
    self.player_1.role="selected"
    self.player_2.role=None
    self.label_score.text = ''
    

  def player_2_click(self, **event_args):
    """This method is called when the Player2 link in the navigation pain is clicked"""
    self.item = app_tables.table_1.get(name="player2")
    self.player_1.role=None
    self.player_2.role="selected"
    self.label_score.text = ''

  def clear_scores(self):
    "This method clears all scores from the data table"
    app_tables.table_1.delete_all_rows()
    app_tables.table_1.add_row(name="player1")
    app_tables.table_1.add_row(name="player2")
    

  def button_new_click(self, **event_args):
    """This method is called when the New Game button is clicked"""
    # It clears the scores and then assigns Player1 to be the current player
    self.clear_scores()
    self.item = app_tables.table_1.get(name="player1")
    self.player_1.role="selected"
    self.player_2.role=None
    self.label_score.text=''  
    


  def button_roll_click(self, **event_args):
    # self.images represents dice (images) to be rolled
    # If no dice selected, at the beginning of a turn, roll all the dice (images)
    if self.images==[]:
      self.images = [self.image_1,self.image_2,self.image_3,self.image_4,self.image_5]
    # If one or more dice were selected, the selected dice (images) will be stores in self.images
    # It's kind of like the cup where players put the dice they want to roll
    for image in self.images:
      self.roll_dice(image)
    # At the end of the turn, clear the images list (analogous to the cup being empty), ready for the next player
    self.images.clear()
    self.button_roll.text = "ROLL ALL DICE"

  
  def roll_dice(self, image):
    image.source = None
    # dice is a list with image sources
    dice = ['_/theme/1.png','_/theme/2.png','_/theme/3.png','_/theme/4.png','_/theme/5.png','_/theme/6.png']
    # randomly select a dice image
    image_number = random.choice(dice)
    # wait a moment so player knows something happened
    time.sleep(0.2)
    # assign the image source to the randomly selected dice image, and make it visible
    image.source = image_number
    image.visible = True




  def dim(self,source):
    if source=='1.png':
      return '_/theme/1-dim.png'
    if source=='2.png':
      return '_/theme/2-dim.png'
    if source=='3.png':
      return '_/theme/3-dim.png'
    if source=='4.png':
      return '_/theme/4-dim.png'
    if source=='5.png':
      return '_/theme/5-dim.png'
    if source=='6.png':
      return '_/theme/6-dim.png'

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
    # image.visible = False
    self.images.append(image)
    self.button_roll.text="Roll Selected Dice"
    image.source=self.dim(image.source.name)

  def check_for_bonus(self):
    """Gives player bonus score if sum of ones through sixes is at least 63"""
    sum=0
    # scores=[self.item['ones'], self.item['twos'], self.item['threes'], self.item['fours'], self.item['fives'], self.item['sixes']]
    # Changed code because I assume it'll be faster if I use client-side values from text boxes 
    # rather than values stored server-side in the database
    scores=[self.text_box_1.text, self.text_box_2.text, self.text_box_3.text, self.text_box_4.text, self.text_box_5.text, self.text_box_6.text]
    for score in scores:
      if score is not None:
        sum+=int(score)
    if sum>=63:
      self.item['bonus']=50
      self.text_box_bonus.text=50
    else:
      self.item['bonus']=0
      self.text_box_bonus.text=0



  def calculate_score_click(self, **event_args):
    """This method is called when the Calculate Score button is clicked"""
    self.check_for_bonus()
    sum=0
    # scores=[self.item['ones'], self.item['twos'], self.item['threes'], self.item['fours'], self.item['fives'], self.item['sixes'], self.item['bonus'],
    #        self.item['3_kind'], self.item['4_kind'], self.item['full_house'], self.item['sm_straight'], self.item['lg_straight'], 
    #        self.item['chance'], self.item['yahtzee']]
    # Changed code because I assume it'll be faster if I use client-side values from text boxes 
    # rather than values stored server-side in the database
    scores=[self.text_box_1.text, self.text_box_2.text, self.text_box_3.text, self.text_box_4.text, self.text_box_5.text, self.text_box_6.text, self.text_box_bonus.text,
           self.text_box_3_kind.text, self.text_box_4_kind.text, self.text_box_full_house.text, self.text_box_sm_straight.text, self.text_box_lg_straight.text,
           self.text_box_chance.text, self.text_box_yahtzee.text]
    for score in scores:
      # if isinstance(score, int) : ... This works, too. A little confused, because textBox.text should be a string, right? So isinstance(aString, int) should
      # return False, shouldn't it? It even works ok if you enter a string of letters in the textBox!
      if score is not None:
        sum+=score
    self.label_score.text=str(sum)


  


    
    


