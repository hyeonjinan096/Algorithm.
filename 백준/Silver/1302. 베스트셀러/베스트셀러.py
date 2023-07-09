n = int(input())
 
books = {}
 
for _ in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1
      
M = max(books.values())
arr = []
 
for book, n in books.items():
    if M==n:
        arr.append(book)
arr.sort()

print(arr[0])