import numpy as np

PASS_MARK = 40


def get_marks():
    text = input("Enter marks separated by spaces: ")
    values = text.split()

    if not values:
        print("Enter at least one mark.")
        return None

    try:
        marks = [float(value) for value in values]
    except ValueError:
        print("Invalid marks. Enter numbers only.")
        return None

    for mark in marks:
        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100.")
            return None

    return np.array(marks)


def analyze_marks(marks):
    mean = np.mean(marks)
    median = np.median(marks)
    highest = np.max(marks)
    lowest = np.min(marks)
    std_dev = np.std(marks)  # Population standard deviation (NumPy default)

    passed = np.sum(marks >= PASS_MARK)
    failed = len(marks) - passed
    pass_percentage = passed / len(marks) * 100
    above_average = np.sum(marks > mean)

    print("\nClass Marks Analysis")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Max: {highest:g}")
    print(f"Min: {lowest:g}")
    print(f"Std Dev: {std_dev:.2f}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Pass percentage: {pass_percentage:.2f}%")
    print(f"Above average: {above_average} student(s)")


def main():
    marks = get_marks()
    if marks is not None:
        analyze_marks(marks)


if __name__ == "__main__":
    main()
