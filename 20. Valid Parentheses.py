class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for char in s:
            if char in openToClose:
                topElement = stack.pop() if stack else "#"
                if openToClose[char] != topElement:
                    return False
            else:
                stack.append(char)
        if len(stack) > 0:
            return False
        return True
        