# set difference calculation

def calculate_set_differences(set1: set, set2: set) -> tuple[set, set]:
 one = set1 - set2
 two = set2 - set1
 return one, two

set1 = {'a', 'b', 'c'}
set2 = {'b', 'c', 'd'}
print(calculate_set_differences(set1, set2))