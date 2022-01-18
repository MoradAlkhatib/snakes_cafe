print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type 'quit' **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
""")


allOrder = {"wings": 0, "cookies": 0, "spring rolls": 0, "salmon": 0, "steak": 0, "meat tornado": 0,
            "a literal garden": 0, "ice cream": 0, "cake": 0, "pie": 0, "coffee": 0, "tea": 0, "unicorn tears": 0, }
count = 0


order = input(""" 
***********************************
Please check you use Lower case 
** What would you like to order? **
***********************************
>""").lower()

while order != "quit":
    if(order in allOrder):
        allOrder[order] = allOrder[order]+1
        for i in allOrder:
            if(allOrder[i] > 0):

                print("{} order of {} have been added to your meal".format(
                    allOrder[i], i))

    else:
        allOrder[order]=1
        print('the item you ordered is not on the menu but we will get it for you')
        print(f' {allOrder[order]} order of {order} have been added to your meal ')

    order = input(""" 
***********************************
Please check you use Lower case 
** What would you like to order? **
***********************************
>""").lower()
