"""Sort the following dictionary’s keys based on the value from highest to lowest. Assign the resulting value to the variable sorted_values."""

dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
d=dictionary.keys()
sorted_values=sorted(d, key=lambda x: dictionary[x], reverse=True)
print(sorted_values)
