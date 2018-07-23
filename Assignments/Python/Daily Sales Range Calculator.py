"""This is the List of Sales provided by the user"""
SalesList = [4, 2, 10, 7]
"""Setting HighSale and LowSale equal to the first item on the list
ensures that no values will be missed, as it ensures all other items on the
list will be equated to other items on the list."""
HighSale = SalesList[0]
LowSale = SalesList[0]
SaleRange = 0

"""This function evaluates each item in the list, and checks it against the
current values held within HighSale and LowSale."""
for sale in SalesList:
    """This part of the function calculates the highest value"""
    if sale > HighSale:
        HighSale = sale
       
    else:
        """This part of the function calculates the lowest value"""
        if sale < LowSale:
            LowSale = sale
           

"""This is a simple calculation to calculate the range"""
SaleRange = HighSale - LowSale
"""This prints the value of the range"""
print(SaleRange)
