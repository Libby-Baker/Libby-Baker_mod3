'''
Libby Baker
Campus cafe

Pseudocode:
define menu - print items and prices
print menu
variables for menu item prices and tax
get variable for input - how many coffees
get variable for input - how many muffins
get variable for input - how many bagels
get tip percent from input for variable

function line total - return unit price*qty
get line prices for each item using line total function.
calculate subtotal using line totals
calculate real tax - subtotal*tax percent
calculate real tip - subtotal*tip
add total - real tax, real tip, subtotal

function format currency - print float with $ and two decimal spaces :.f
use format currency function on item line_totals. totals, subtotals, tax, and tip
make print receipt funfunction
print f {qty} x {each item} @ {unit price} = {line total} x3
print tax
print tip
print total
ty!
call print receipt



'''
def menu():
    print("==Campus Cafe==")
    print("Coffee - $2.25")
    print("Muffin - $2.75")
    print("Bagel - $2.50")

menu() #print menu
#Setting up variables for qty inputs and prices
coffee_qty = int(input("How many coffees? "))
coffee_price = 2.25

muffin_qty = int(input("How many muffins? "))
muffin_price = 2.75

bagel_qty = int(input("How many bagels? "))
bagel_price = 2.50

tip_percent = int(input("Enter tip percent "))
tax = 0.08875


def line_total(unit_price: float, qty: int): # calculate line totals. Unit price x amount
   return(float(unit_price*qty))


coffee_line = line_total(coffee_price, coffee_qty)
muffin_line = line_total(muffin_price, muffin_qty)
bagel_line = line_total(bagel_price, bagel_qty)

subtotal = (coffee_line+muffin_line+bagel_line)# add up line totals
real_tax = 0.08875*subtotal #actual tax amount. Tax percent x subtotal
real_tip = subtotal*tip_percent/100 #actual tip amount. Tip percent x subtotal

def compute_total(subtotal: float, tax: float, tip: float):
    return(float(subtotal+tax+tip))

total = compute_total(subtotal, real_tax, real_tip)

def format_currency(amount: float):
    return(f"${amount:.2f}") #format currency $_.__

#Reformat everything for print. There's a better way to do this, isn't there?
subtotal_form = format_currency(subtotal)
coffee_line_form = format_currency(coffee_line)
muffin_line_form = format_currency(muffin_line)
bagel_line_form = format_currency(bagel_line)
coffee_price_form = format_currency(coffee_price)
muffin_price_form = format_currency(muffin_price)
bagel_price_form = format_currency(bagel_price)
total_form = format_currency(total)
tip_form = format_currency(real_tip)
tax_form = format_currency(real_tax)


def receipt():
    print("==Receipt==")
    print(f"{coffee_qty} x Coffee @ {coffee_price_form} = {coffee_line_form}")
    print(f"{muffin_qty} x Muffin @ {muffin_price_form} = {muffin_line_form}")
    print(f"{bagel_qty} x Bagel @ {bagel_price_form} = {bagel_line_form}")
    print(f"Subtotal   {subtotal_form}")
    print(f"Tax    {tax_form}")
    print(f"Tip    {tip_form}")
    print(f"TOTAL  {total_form}")
    print("Thank You!")



receipt()











