print("-------bill calc------")
bill=float(input("what was the bill..?"))
tip=int(input("how much per. for tip ?"))
people=int(input("how many number of people..."))
tip_as_percent=tip/100
total_tip_amount=bill*tip_as_percent
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
print(final_amount)

