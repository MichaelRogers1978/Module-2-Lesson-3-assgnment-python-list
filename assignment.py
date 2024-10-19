#task 1


grade = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grade.sort()


print(f"sorted grade: {grade}") 
print(f"average {sum(grade)//len(grade)}")


# task 2

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if "Alice" in submitted and "Alice" in attended:
    print("Alice was in class and turned in her assignments.")
else:
    print("Poor Alice doesn't get to have ice cream.")


# task 3

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week_temperatures_index = temperatures[7:14]
temperatures_over_one_hundred_index = temperatures[24:30]

print(f"second_week_temperatures: {second_week_temperatures_index}")
print(f"temperatures_over_one_hundred: {temperatures_over_one_hundred_index}")
