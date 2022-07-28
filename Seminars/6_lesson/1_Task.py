listt = [1, 1, 2]
# res = list(filter(lambda x: listt.count(x) == 1, listt))
my_list = [x for x in listt if listt.count(x) == 1]
print(my_list)
