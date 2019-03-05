import VT4002
vt4002 = VT4002.Connection(port='/dev/ttyS4')

output = vt4002.get_actual_values()

print(output.temp2_actual())
print(output.temp1_actual())
