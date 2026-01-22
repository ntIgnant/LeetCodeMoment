# https://leetcode.com/problems/group-anagrams/description/

anagrams_list = ["eat","tea","tan","ate","nat","bat"]
print(anagrams_list)

sorted_anagrams = ["".join(sorted(word)) for word in anagrams_list]
print(sorted_anagrams)
unique_anagrams = {hash(word) for word in sorted_anagrams}
print(unique_anagrams)
for anagram in anagrams_list:
    tmp_sorted = "".join(sorted(anagram))
    tmp_hashed = hash(tmp_sorted)

    for key in unique_anagrams:
        if tmp_hashed == key:
            unique_anagrams.update(key, anagram)