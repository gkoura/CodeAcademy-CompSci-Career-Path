weight = 41.5

#Ground Shipping
flat_charge = 20 
ground_cost = None
if weight <= 2:
    ground_cost = 1.5*weight+flat_charge
elif weight  > 2 and weight <= 6:
    ground_cost = 3*weight+flat_charge
elif weight  > 6 and weight <= 10:
    ground_cost = 4*weight+flat_charge
else:
    ground_cost = 4.75*weight+flat_charge

print (f"Ground Shipping: {ground_cost:.2f}")

#premium ground shipping
prem_flat_charge = 125 
print (f"Ground Shipping Premium: {prem_flat_charge:.2f} ")

#drone shipping 
drone_cost = None
if weight <= 2:
    drone_cost = 4.5*weight
elif weight  > 2 and weight <= 6:
    drone_cost = 9*weight
elif weight  > 6 and weight <= 10:
    drone_cost = 12*weight
else:
    drone_cost = 14.25*weight

print (f"Drone Shipping: {drone_cost:.2f}")