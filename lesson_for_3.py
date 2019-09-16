all_scores = [
    {'school_class': '4a', 'scores':[3,4,4,5,2]},
    {'school_class': '4b', 'scores':[5,5,3,4,1]},
    {'school_class': '4v', 'scores':[1,2,5,5,4]}
]

key_school_class = 0
sum_avg_class_score = 0

for class_score in all_scores:
    sum_class_score = 0
    class_score = all_scores[key_school_class]["scores"]
    sum_class_score = sum(class_score)
    avg_class_score = sum_class_score / len(class_score)
    sum_avg_class_score = sum_avg_class_score + avg_class_score
    print(f'Средний балл по классу {all_scores[key_school_class]["school_class"]}: {avg_class_score}')
    key_school_class = key_school_class + 1

avg_school_score = sum_avg_class_score / len(all_scores)
<<<<<<< HEAD
print (f'Средний балл по школе: {avg_school_score}')
=======
print (f'Средний балл по школе: {avg_school_score}')
>>>>>>> 5627e4b680dc12a4179ba9614931c5cf0ad6dd9a
