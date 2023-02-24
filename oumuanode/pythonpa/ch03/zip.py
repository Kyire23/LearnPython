evens = [0, 2, 4, 6, 8]
odds = [1, 3, 5, 7, 9]
for e, o in zip(evens, odds):
    print("{0}*{1}={2}".format(e, o, e*o))

