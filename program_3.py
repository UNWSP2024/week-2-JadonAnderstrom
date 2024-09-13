def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    print('Hello, and welcome to the Anderstrom Bakery. This is a self automated checkout. Please enter the price of your items below.\n')
 
    item1 = float(input('Insert dollar amount of item 1: $'))
    item2 = float(input('Insert dollar amount of item 2: $'))
    item3 = float(input('Insert dollar amount of item 3: $'))
    item4 = float(input('Insert dollar amount of item 4: $'))
    item5 = float(input('Insert dollar amount of item 5: $'))
    
    # then displays the subtotal of the sale, 
    pt1 = (item1 + item2 + item3 + item4 + item5)
    print('Subtotal: $','${:,.2f}'.format(pt1))
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.
    print('Sales tax: 7%')
    pt2 = (pt1 * 1.07)
    print('Total: $','${:,.2f}'.format(pt2))
    print('\n')
    print('Thank you for shopping at the Anderstrom Bakery, see you next time!')

calculate_total_purchase()

    #Jadon Anderstrom, 9/12/24, "Calculate Total".
