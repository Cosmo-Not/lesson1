all_scores = [
    {'school_class': '4a', 'scores':[3,4,4,5,2]},
    {'school_class': '4b', 'scores':[5,5,3,4,1]},
    {'school_class': '4v', 'scores':[1,2,5,5,4]}
]

scores_sum_a=0
scores_sum_b=0
scores_sum_v=0

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
