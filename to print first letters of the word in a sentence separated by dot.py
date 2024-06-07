def Anagrams(li ):
    dictionary = {}
    for word in li:
        sortedWord = ''.join(sorted(word))
        print(sortedWord)
        if sortedWord not in dictionary:
            dictionary[sortedWord] = [word]
        else:
            dictionary[sortedWord] += [word]
    return [dictionary[i] for i in dictionary]

li = ['pop','bat','tab','opp','cat']
print(Anagrams(li))

20. Program to print first letters of the word in a sentence separated by dot.

Sample input: "The cat on the wall"
Sample output: T.C.O.T.W.

string="The cat on the wall"
l1=list(string.split())
print(l1)

for i in range(len(l1)):
    print(l1[i][0].upper(),end=".")
    continue
