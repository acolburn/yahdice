from ._anvil_designer import Form1Template
from anvil import *
import random
import time

blank_image = '_/theme/blank.png'

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.images=[]

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
    # time.sleep(0.2)
    # assign the image source to the randomly selected dice image, and make it visible
    image.source = image_number
    self.reset_dice_position(image)

  def reset_dice_position (self, image):
    if image == self.image_1:
      self.image_1_selected.visible = False
    if image == self.image_2:
      self.image_2_selected.visible = False
    if image == self.image_3:
      self.image_3_selected.visible = False
    if image == self.image_4:
      self.image_4_selected.visible = False
    if image == self.image_5:
      self.image_5_selected.visible = False
    image.visible = True

  def link_1_click(self, **event_args):
    self.image_click(self.image_1, self.image_1_selected)
    
  def link_2_click(self, **event_args):
    self.image_click(self.image_2, self.image_2_selected)

  def link_3_click(self, **event_args):
    self.image_click(self.image_3, self.image_3_selected)

  def link_4_click(self, **event_args):
    self.image_click(self.image_4, self.image_4_selected)

  def link_5_click(self, **event_args):
    self.image_click(self.image_5, self.image_5_selected)

  def image_click(self, image, image_selected):
    image_selected.source = image.source
    image_selected.visible = True
    self.images.append(image) 
    image.source ='_/theme/blank.png'
    self.button_roll.text="Roll Selected Dice"

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

  def button_new_click(self, **event_args):
    """This method is called when the button is clicked"""
    print('new game button clicked')
    scores=[self.text_box_1, self.text_box_2, self.text_box_3, self.text_box_4, self.text_box_5, self.text_box_6, self.text_box_bonus,
           self.text_box_3_kind, self.text_box_4_kind, self.text_box_full_house, self.text_box_sm_straight, self.text_box_lg_straight,
           self.text_box_chance, self.text_box_yahtzee]
    for score in scores:
      score.text=''
    self.label_score.text='0'

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.calculate_score_click()

  def text_box_2_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.calculate_score_click()

  def text_box_3_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.calculate_score_click()

  def text_box_4_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.calculate_score_click()

  def text_box_5_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.calculate_score_click()

  def text_box_6_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.calculate_score_click()

  def text_box_3_kind_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.calculate_score_click()

  def text_box_4_kind_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.calculate_score_click()

  def text_box_full_house_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.calculate_score_click()

  def text_box_sm_straight_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.calculate_score_click()

  def text_box_lg_straight_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.calculate_score_click()

  def text_box_chance_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.calculate_score_click()

  def text_box_yahtzee_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    self.calculate_score_click()




  


    
    


