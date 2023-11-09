class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = [0] * max(len(l1), len(l2))
        for i in range(min(len(l1), len(l2))):
            current = l1[i] + l2[i]
            if current < 10:
                result[i] += current
            else:
                result[i] += int(str(current)[1])
                result[i + 1] += 1

        if len(l1) > len(l2):
            for i in range(len(l2),len(l1)):
                result[i] += l1[i]

        elif len(l1) < len(l2):
            for i in range(len(l1),len(l2)):
                result[i] += l2[i]
        return result

print(Solution().addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4, 1, 1]))