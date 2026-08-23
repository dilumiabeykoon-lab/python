customer_n=input("Enter Customer Name:")
pre_meter_reading=int(input("Enter previous meter reading:"))
c_meter_reading=int(input("Enter current meter reading:"))
s_charge=500
env_levy=float(1000)
print("------------  Electricity Bill------------")
print("Customer Name:",customer_n)

if pre_meter_reading>=0 and c_meter_reading>=0 and c_meter_reading>=pre_meter_reading:
    #calculate the no of units.
    units_consumed=c_meter_reading-pre_meter_reading
    print("Units Consumed:",units_consumed)
    if units_consumed<=60:
        e_charge=units_consumed*25
    elif units_consumed>60 and units_consumed<=120:
        charge1=60*25
        remaining=units_consumed-60
        charge2=remaining*35
        e_charge=charge1+charge2
    elif units_consumed>120:
        charge1=60*25
        charge2=60*35
        remaining=units_consumed-120
        charge3=remaining*50
        e_charge=charge1+charge2+charge3

print("Electricity Charge:Rs.",e_charge)
print("Service Charge:Rs.",s_charge)

if units_consumed>150:
    final_bill=e_charge+env_levy+s_charge
    print("Environmental Levy:Rs.",env_levy)
else:
    final_bill=e_charge+s_charge
    print("Environmental Levy:Rs.0.00")

print("Final Bill:Rs.",final_bill)
print()
if units_consumed<30:
    print("Reward:Energy Saver Reward")
else:
    print("Reward:None")
