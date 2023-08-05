import math

print("\n**** Heat-Index calculator ****\n")

temp = float(input('Temperature(*C): '))
hum = float(input('Humidity(%): '))
# Convert celius to fahrenheit
fahrenheit = ((temp * 9/5) + 32)

# Creating multiples of 'fahrenheit' & 'hum' values for the coefficients
T2 = pow(fahrenheit, 2)
T3 = pow(fahrenheit, 3)
H2 = pow(hum, 2)
H3 = pow(hum, 3)

# Coefficients for the calculations
C1 = [ -42.379, 2.04901523, 10.14333127, -0.22475541, -6.83783e-03, -5.481717e-02, 1.22874e-03, 8.5282e-04, -1.99e-06]
heatindex = round(C1[0] + (C1[1] * fahrenheit) + (C1[2] * hum) + (C1[3] * fahrenheit * hum) + (C1[4] * T2) + (C1[5] * H2) + (C1[6] * T2 * hum) + (C1[7] * fahrenheit * H2) + (C1[8] * T2 * H2))

if (fahrenheit > 80 and fahrenheit < 112) and hum < 13:
    adj1 = ((13-hum)/4)*math.sqrt((17 - abs(fahrenheit - 95))/17) # if RH < 13 and AT (80, 112) *F
elif (fahrenheit > 80 and fahrenheit < 87) and hum > 85:
    adj2 = ((hum-85)/10) * ((87-fahrenheit)/5)
elif fahrenheit < 80:
    heatI = (((0.5 * (fahrenheit + 61.0 + ((fahrenheit-68.0)*1.2) + (hum*0.094))) - 32)*5)/9 # < 80


print("\nThe Heat index is:")
if fahrenheit < 80:
    print(heatI)
elif (fahrenheit > 80 and fahrenheit < 87) and hum > 85:
    print(((heatindex + adj2 - 32)*5)/9)
elif (fahrenheit > 80 and fahrenheit < 112) and hum< 13:
    print(((heatindex - adj1 - 32)*5)/9)
else:
    print(heatI)
    
# print("Heatindex:", (round(((heatindex - 32) * 5/9), 0),"*C"))
