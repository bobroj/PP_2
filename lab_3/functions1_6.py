def reverse_sentence(sentence):
    # разделяем слова в предложении и каждое слово становится элементом кортежа
    words = sentence.split()

    n=len(words)

    for i in range(n-1, -1, -1):
        print(words[i])


my_sentence = input("Enter a sentence: ")


print("Reversed sentence: ")
reverse_sentence(my_sentence)
