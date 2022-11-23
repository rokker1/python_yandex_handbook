N = int(input())
base = []
for i in range(N):
    line = input()
    base.append(line)
query = input()
for document in base:
    if document.lower().find(query.lower()) != -1:
        print(document)