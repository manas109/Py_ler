# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 18:42:41 2021

@author: Manaswini Raghavan
"""
#QR Code generter using python 

import qrcode
img = qrcode.make("https://www.youtube.com/")
img.save("youtubeQR.jpg")
