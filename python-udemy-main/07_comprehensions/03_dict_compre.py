tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

tea_prices_usd = {tea:price / 80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)

#Practise code
student_marks = {
    "Aman": 9.5,
    "Hitesh": 8.0,
    "Jia": 9.5,
}

student_marks_Percentage = {student:percentage * 10 for student, percentage in student_marks.items()}

print(student_marks_Percentage)