# Student result module

def calculate_result(marks):
    if not marks:
        return 0, 0
    total = sum(marks)
    average = total / len(marks)
    return total, average
