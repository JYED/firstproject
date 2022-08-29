seasons = ['봄','여름','가을','겨울']

for season in seasons:
    print(season)

ages = {'Tod':35, 'Jane':23, 'Paul':62}
for key in ages.keys():
    print(key)

for value in ages.values():
    print(value)

#for key in ages: 와 같은 의미이다.
for key in ages.keys():
    print('{}의 나이는 {}입니다.'.format(key,ages[key]))

# 두개의 value
for key,value in ages.items():
        print('{}의 나이는 {}입니다.'.format(key,value))

#dictionary에서는 list와 다르게 값의 순서를 지켜주진 않는다. ? 근데 순서대로 나오는데?