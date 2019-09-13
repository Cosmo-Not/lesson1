all_scores = [
    {'school_class': '4a', 'scores':[3,4,4,5,2]},
    {'school_class': '4b', 'scores':[5,5,3,4,1]},
    {'school_class': '4v', 'scores':[1,2,5,5,4]}
]

scores_sum_a=0
scores_sum_b=0
scores_sum_v=0
key_school_class = 0
sum_school_score = 0
avg_school_score = 0

for class_score in all_scores:
    sum_class_score = 0
    avg_class_score = 0
    class_score = all_scores[key_school_class]["scores"]
    sum_class_score = sum(class_score)
    avg_class_score = sum_class_score / len(class_score)
    print(f'Средний балл по классу {all_scores[key_school_class]["school_class"]}: {avg_class_score}')
    key_school_class = key_school_class + 1

for score in all_scores[0]["scores"]:
    scores_sum_a += score
a = scores_sum_a / len(all_scores[0]["scores"])
print(f'Средний балл по классу {all_scores[0]["school_class"]}: {a}')

for score in all_scores[1]["scores"]:
    scores_sum_b += score
b = scores_sum_b / len(all_scores[1]["scores"])
print(f'Средний балл по классу {all_scores[1]["school_class"]}: {b}')

for score in all_scores[2]["scores"]:
    scores_sum_v += score
v = scores_sum_v / len(all_scores[2]["scores"])
print(f'Средний балл по классу {all_scores[2]["school_class"]}: {v}')

all = (a + b + v)/3
print(f'Средний балл по школе: {all}')
