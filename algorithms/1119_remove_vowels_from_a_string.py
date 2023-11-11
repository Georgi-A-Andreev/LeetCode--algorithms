class Solution(object):
    def removeVowels(self, s):
        result = ''
        for c in s:
            if c not in ('a', 'e', 'i', 'o', 'u'):
                result += c

        return result