import math
marks_data = {
    'Березька': [6, 12, 11, 6, 5, 10, 8, 9, 9, 7, 5, 11],
    'Баймухаметов': [11, 4, 9, 5, 9, 8, 12, 9, 4, 10, 4, 11],
    'Маєвський': [11, 11, 11, 11, 11, 10, 11, 10, 11, 10, 11, 10],
    'Гатілов': [4, 9, 5, 4, 7, 5, 5, 6, 5, 8, 9, 5],
    'Дурідівка': [4, 7, 5, 4, 9, 5, 5, 4, 5, 4, 11, 5],
    'Козаченко': [10, 6, 10, 4, 7, 5, 10, 9, 5, 4, 10, 10],
    'Воробканич': [5, 5, 5, 5, 6, 5, 5, 4, 5, 6, 8, 9],
    'Губченков': [4, 9, 5, 5, 8, 5, 8, 7, 7, 7, 6, 4],
    'Лакаров': [4, 4, 6, 4, 7, 5, 9, 10, 5, 9, 11, 6],
    'Лоза': [4, 5, 5, 4, 10, 8, 5, 6, 9, 10, 8, 7],
}

#середні оцінки

class_average = sum(sum(marks) for marks in marks_data.values()) / sum(len(marks) for marks in marks_data.values())

print("Середня оцінка в класі: ", round(class_average, 2))

#оцінки вище середніх

print("Оцінки учнів:")

for student, marks in marks_data.items():
    student_average = sum(marks) / len(marks) if len(marks) > 0 else 0
    if student_average > class_average:
        print(f"Учень {student} має оцінку вище середньої ({round(student_average, 2)})")
    else:
        print(student, "середня оцінка: ", round(student_average, 2))    

