def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3))

# print(hitung_total(1, 2, 3, 4, 5, 6, 7, 8)) Will work too