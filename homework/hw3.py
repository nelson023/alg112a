def generate_permutations(n):
    result = []  

    def perm_next(p):
        i = len(p)
        if i == n:
            result.append(p.copy())  
            return
        for x in range(n):
            if x not in p:
                p.append(x)
                perm_next(p)
                p.pop()

    perm_next([])
    return result

print(generate_permutations(2))
print(generate_permutations(3))
print(generate_permutations(4))
print(generate_permutations(5))
