# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:44:30 2018

@author: Asako
"""

from numpy import *
from functions import call_desired,create_weekShift



if __name__ == "__main__":

    MShift = call_desired()
    Feedback = array([1,1,1,1,1,1,1,1,1,1])
    weekcount = 0
    while weekcount<4:
        desiredShift = MShift[weekcount]
        Feedback ,lastfeed = create_weekShift(desiredShift,Feedback)
        if input("Do you reject this?[y/]") == "y":
            Feedback,lastfeed = create_weekShift(desiredShift,Feedback)
    
        else:
            #ここで次の週のDesired受け取って、（desiredShift)
            Feedback = lastfeed
            weekcount +=1