pers = [1, 2, 3]
secun = ["mark", "alice", "john"]

# One-liner to create a list of tuples
result = [(pers[i], secun[i]) for i in range(len(pers))]

print(result)
