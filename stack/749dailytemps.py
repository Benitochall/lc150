class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        answers = [0] * len(temperatures)
        for i, num in enumerate(temperatures):
            while stack and num > stack[-1][0]:
                # pop value from stack and place it where it should go
                val, pos = stack.pop()
                answers[pos] = i - pos
            stack.append((num,i))
        return answers