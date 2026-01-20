# https://leetcode.com/problems/valid-anagram/description/

s = "anagram"
t = "nagaram"

sorS = sorted(s)
sorS = "".join(sorS)

sorT = sorted(t)
sorT = "".join(sorT)

if sorS == sorT:
    print("True")
else:
    print("False")
