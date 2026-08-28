students = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 78},
        {"name": "David", "score": 95}
    ]


total = sum(student["score"] for student in students)
people = len(students)
result = total / people

print(result)