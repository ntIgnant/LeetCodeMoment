# s = "anagram"
# t = "nagaram"
#
# # Sort a string in alphabetical order (NOTE: it returns the value as a list)
# s = sorted(s)
# print(s)

anagram_list = ["eat","tea","tan","ate","nat","bat"]
sorted_anagrams = ["".join(sorted(word)) for word in anagram_list]
unique_anagrams = {hash(word) for word in sorted_anagrams}
print(anagram_list)
print(sorted_anagrams)
print(unique_anagrams)

word1 = "earth"
sorted_w1 = "".join(sorted(word1))
hash_sorted_w1 = hash(sorted_w1)

word2 = "heart"
sorted_w2 = "".join(sorted(word2))
hash_sorted_w2 = hash(sorted_w2)


print(word1, word2)
print(sorted_w1, sorted_w2)
print(hash_sorted_w1, hash_sorted_w2)