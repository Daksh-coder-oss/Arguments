def total_amount(bill,tip_perc):
    total_bill=bill+(tip_perc*0.01*bill)
    print("The total bill is",total_bill)
bill=int(input("Please enter your bill value"))
tip_perc=int(input("Please ener the tip percentage"))
total_amount(bill,tip_perc)