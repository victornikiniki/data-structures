hey = (9, 3, 5)

# print(hey[0]) indexing with tuple

def area_perimeter_sq(side_length):
    area = side_length * side_length
    perimeter = side_length * 4
    return (area, perimeter) # tuple paranthesis optional

result = area_perimeter_sq(5) 

# print(f"Area: {result[0]} ") 
# print(f"Perimeter: {result[1]} ")

lst = [1, 2, 3]
new_list = []

for x in lst: 
    new_list.append((x, x*x))

print(new_list)
