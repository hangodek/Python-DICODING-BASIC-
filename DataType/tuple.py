x = (1, "Dicoding", 1+3j)
print(type(x))

x = (5, 'program', 1+3j)
print(x[1])
print(x[0:3])

#x = (5, 'program', 1+3j) Won't work coz tuple is immutable
#x[1] = 'Dicoding'