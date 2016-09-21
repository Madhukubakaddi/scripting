#!/tools/bin/python
#Program for converting celsius to Frahnheit temperature (Tf = Tc * 9.0 / 5.0 + 32)

Tc = raw_input("Enter temperature in celsius:")
Tf = float(Tc) * 9.0 / 5.0 + 32
print "Temperature in Frahnheit is:", Tf
