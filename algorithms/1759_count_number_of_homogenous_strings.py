class Solution(object):
    def countHomogenous(self, s):
        result = 0
        counter = 0
        MOD = 10 ** 9 + 7
        for idx, l in enumerate(s):
            if idx == 0 or l == s[idx - 1]:
                counter += 1
            else:
                counter = 1

            result = (result + counter) % MOD

        return result