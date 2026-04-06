class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = { ")": "(",
                    "]": "[",
                    "}": "{" }

        for p in s:
            if p in matches:
                if stack and stack[-1] == matches[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
                
        return len(stack) == 0