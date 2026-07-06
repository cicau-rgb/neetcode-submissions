class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "[" : "]",
            "(" : ")",
            "{" : "}"
        }

        stack = []

        for c in s:
            if c in pairs.keys():
                stack.append(c)
            elif len(stack) > 0 and pairs[stack.pop()] == c:
                continue
            else:
                return False
        
        return len(stack) == 0
        