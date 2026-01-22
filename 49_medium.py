# https://leetcode.com/problems/group-anagrams/description/

anagrams_list = ["eat","tea","tan","ate","nat","bat"]
print(anagrams_list)

sorted_anagrams = ["".join(sorted(word)) for word in anagrams_list]
print(sorted_anagrams)
unique_anagrams = {}
for anagram in anagrams_list:
    tmp_sorted = "".join(sorted(anagram))
    tmp_hashed = hash(tmp_sorted)

    if tmp_hashed in unique_anagrams:
        unique_anagrams[tmp_hashed].append(anagram)
    else:
        unique_anagrams[tmp_hashed] = [anagram]


print(list(unique_anagrams.values()))