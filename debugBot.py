#chatBot lib
import nltk
import numpy as np 
import random
import time

def bot(user_input):
    user_input = user_input.lower()

    if(user_input=='thanks' or user_input=='thank you'):
        return "You are welcome"

    
    return "Didnt get anything. Sorry I didnt understand..."




