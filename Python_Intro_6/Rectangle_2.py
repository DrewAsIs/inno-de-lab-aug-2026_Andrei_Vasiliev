length_text = input("Enter length: ")
width_text = input("Enter width: ")
#a floating point type would fit here better, but int is directly mentioned in the task, so it is what it is
length = int(length_text)
width = int(width_text)
area = length * width
print(f'Area is: {area}')