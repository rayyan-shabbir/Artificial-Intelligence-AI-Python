# y = 10

# # x = y += 2

# print(y)

txt = 'but soft what light in yonder window breaks'

words = txt.split()

lst = list()

for word in words:
    lst.append((len(word), word))

lst.sort(reverse=True)
print(lst)

res = list()
for key, val in lst:
    res.append(val)

print(res)
