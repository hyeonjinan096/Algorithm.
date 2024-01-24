from sys import stdin

num_test_cases = int(stdin.readline())

for _ in range(num_test_cases):
    num_words = int(stdin.readline())
    word_list = [None] * num_words
    palindrome = False

    for word_idx in range(num_words):
        word_list[word_idx] = stdin.readline().rstrip()

    for i in range(0, num_words-1):
        for j in range(i+1, num_words):
            word_set1 = word_list[i] + word_list[j]
            word_set2 = word_list[j] + word_list[i]

            if word_set1 == word_set1[::-1]:
                print(word_set1)
                palindrome = True
                break
            elif word_set2 == word_set2[::-1]:
                print(word_set2)
                palindrome = True
                break

        if palindrome:
            break

    if not palindrome:
        print(0)
