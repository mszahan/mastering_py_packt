filter_modulo = lambda i, m: (i[j] for j in range(len(i)) if i[j] % m)

print(list(filter_modulo(range(10), 2)))

# this is beatiful which is better than prvious ugly code
def filter_modulo(items, modulo):
    for item in items:
        if item % modulo:
            yield item

print(list(filter_modulo(range(10), 2)))

