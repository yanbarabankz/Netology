word = ('testing')
result = list(word)
if len(word)%2 == 0:
    print("Число букв чётное")
    print(word[(int((len(word)-1)/2))], word[(int((len(word)+1)/2))])
else:
    print("Число букв нечётное")
    print(word[int((len(word)-1)/2)])



