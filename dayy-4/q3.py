string = "hello"
visited = []

for i in range(len(string)):
    if string[i] not in visited:
        count = 0
        for j in range(len(string)):
            if string[i] == string[j]:
                count = count + 1
        print(string[i], "→", count)
        visited.append(string[i])
