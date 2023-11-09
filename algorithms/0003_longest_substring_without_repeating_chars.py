class Solution(object):  # working brute force solution
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        results = []

        for i in range(len(s)):
            counter = 1
            current = [s[i]]

            for j in range(i-1,-1,-1):
                if s[i] == s[j] or s[j] in current:
                    break
                else:
                    current.append(s[j])
                    counter += 1
            results.append(counter)
        return max(results)

print(Solution().lengthOfLongestSubstring('abcabcbb'))