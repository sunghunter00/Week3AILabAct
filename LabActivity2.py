def check_fast_lane(minutes_left, items, teacher_pass):
    # Override rule: teacher pass allows fast lane
    if teacher_pass:
        return "Fast lane approved"

    # Normal fast lane rules
    if minutes_left >= 15 and items <= 10:
        return "Fast lane approved"
    else:
        return "Use regular line"


students_in_line = [
    {"name": "Ella", "minutes_left": 20, "items": 5, "teacher_pass": True},
    {"name": "John", "minutes_left": 10, "items": 3, "teacher_pass": False},
    {"name": "Maria", "minutes_left": 18, "items": 8, "teacher_pass": False},
    {"name": "Kevin", "minutes_left": 5, "items": 12, "teacher_pass": False}
]

fast_lane_count = 0

for student in students_in_line:
    result = check_fast_lane(
        student["minutes_left"],
        student["items"],
        student["teacher_pass"]
    )

    print(student["name"], "-", result)

    if result == "Fast lane approved":
        fast_lane_count += 1

print("Total students approved for fast lane:", fast_lane_count)