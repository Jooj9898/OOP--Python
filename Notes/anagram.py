anagram = str(input("Please enter a word:"))
anagram_2 = str(input("Please enter another word:"))

anagram_sorted = sorted(anagram)
anagram_2_sorted = sorted(anagram_2)

if anagram_sorted == anagram_2_sorted:
    print("these two are anagrams")
else:
    print("they are not anagrams")