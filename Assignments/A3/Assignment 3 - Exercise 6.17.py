# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:01:07 2020

@author: skhan
"""
"""
6.17 (PROJECT: COOKING WITH HEALTHIER INGREDIENTS) In the “Strings: A Deeper
 Look” chapter’s exercises, you’ll write a script that enables its user to 
 enter ingredients from a cooking recipe, then recommends healthier 
 replacements. In preparation for that exercise, create a dictionary that 
 maps ingredients to lists of potential replacements. Some ingredient 
 replacements are shown below:



Your dictionary should take into consideration that replacements are not 
always one-for-one. For example, if a cake recipe calls for three eggs, 
it might reasonably use six egg whites instead. Research conversion data
 for measurements and ingredient substitutes online. Your dictionary should
 map the ingredients to lists of potential substitutes.
"""

subdict = {"sour cream": ["yogurt",],
           "milk": ["evaporated milk", "water"],
           "lemon juice": ["vinegar",],
           "sugar": ["honey", "molasses", "agave nectar"],
           "butter": ["margarine","yogurt"],
           "flour": ["rye flour", "rice flour"],
           "mayonnaise": ["cottage cheese", "mayonnaise", "yogurt"],
           "egg": ["cornstarch", "arrowroot flour", "potato starch", 
                   "egg whites","large banana (mashed)"],
           "milk": ["soy milk"],
           "oil": ["applesauce"]}

print(subdict)