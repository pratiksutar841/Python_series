'''
If cost price and selling price of an item is input through the keyJoard, write a program to determine
whether the seller has made profit or incurred loss or no profit no loss. Also determine how much 
profit he
made or loss he incurred.'''

# Taking cost price and selling price input from the user
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))
 
# Calculating profit/loss
profit = selling_price - cost_price
profit_percentage = (profit / cost_price) * 100
 
# Checking profit/loss and providing output
if profit > 0:
    print("\nThe seller has made a profit of", profit, "units.")
    print("Profit percentage:", profit_percentage, "%")
elif profit < 0: 
    print("\nThe seller has incurred a loss of", abs(profit), "units.")
    print("Loss percentage:", abs(profit_percentage), "%")
else:
    print("\nIt's neither loss nor profit")