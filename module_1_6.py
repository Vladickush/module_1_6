# Словарь

my_dict = {'Vlad' : 1959,
           'Alla' : 1961,
           'Olga' : 1987,
           'Igor' : 1989}
print (my_dict)
print('Vlad ', my_dict['Vlad'])
my_dict['Natasha'] = 2001
print('Natasha ', my_dict['Natasha'])
my_dict['Michal'] = 2019
my_dict['Vera'] = 2021
del my_dict['Vlad']
print (my_dict)

# Множество

my_set = {1,1,2,3,4,4,6,6,8,9,9,'Nick','Pit','Pit'}
print()
print(my_set )
my_set.add('Me')
my_set.add((11,12,13))
my_set.discard('Pit')
print(my_set )
