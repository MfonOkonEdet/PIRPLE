# Home Work 10
"""
Pick any library that come with Python (https://docs.python.org/3/library/) that we haven't covered in the course already.
Learn how to use the library extensively, then prepare a code sample that showcases what you've learned.
This can take any form you wish.
You could create an application with the library, or just show examples of how to use its methods.
"""

# Using the pprint library
import pprint
#creating a variable list
stocks = ["goat", "cow", "ram", "sheep", "pig", "dog", "turkey"]
# setting the index of where you want the list to be placed in the print out
#             (index of the recursive level in which the list would be placed, nested list range of index)
stocks.insert(0, stocks[3:])
# stating the index of each recursive level
# adding width and compact
# width parameter controls the desired output width
# compact fits all items that could fit within the width on each output line if set to "True" but if set to "False" each item would be arranged on seperate lines. 
myP = pprint.PrettyPrinter(indent=1, width=39, compact=False)
myP.pprint(stocks)

#creating another variable and using the depth parameter
#depth controls the number of levels that would be printed
goods = ("drinks",("milk",("car",("meat",("game",("trip",))))))
myg = pprint.PrettyPrinter(depth=4)
myg.pprint(goods)