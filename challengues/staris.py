field_size = int(input())

for number in range(field_size):
    character = "#"
    string = character * (number + 1)
    print(f"{string:>{field_size}}")

# f'Number {i}: {num:{field_size}.2f}'
# 'Number 3:   25.00'

