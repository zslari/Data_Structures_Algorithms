""" Test Driver File for pascal_triangle.py """

from pascal_triangle import pascaltriangle


def test_run():
    print("Test run for Lines 0-6 of Pascal's Triangle")
    for i in range(0, 7):
        print(f" Row {i}: {pascaltriangle(i)}")
    your_last_name = input("What is your last name? \n")
    print(f"Test Case of Pascal's Triangle for Length of {your_last_name}")
    print(f"Row {len(your_last_name)}: "
          f"Results in {pascaltriangle(len(your_last_name))}")


if __name__ == "__main__":
    test_run()


"""
SAMPLE RUN OUTPUT:

Test run for Lines 0-6 of Pascal's Triangle
 Row 0: [1]
 Row 1: [1, 1]
 Row 2: [1, 2, 1]
 Row 3: [1, 3, 3, 1]
 Row 4: [1, 4, 6, 4, 1]
 Row 5: [1, 5, 10, 10, 5, 1]
 Row 6: [1, 6, 15, 20, 15, 6, 1]
What is your last name? 
Foothill
Test Case of Pascal's Triangle for Length of Foothill
Row 8: Results in [1, 8, 28, 56, 70, 56, 28, 8, 1]

"""
