class Solution:
    def isValid(self, s: str) -> bool:
        pattern = {")": "(", "}": "{", "]": "["}
        stack = []
        for i in s:
            if i not in pattern:
                stack.append(i)
            else:
                if stack and pattern[i] == stack.pop():
                    continue
                else:
                    return False

        return not len(stack)