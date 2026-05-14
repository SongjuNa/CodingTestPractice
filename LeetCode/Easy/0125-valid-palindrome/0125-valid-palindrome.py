class Solution:
    def isPalindrome(self, s: str) -> bool:
        rmv_non_alphanum = "".join(char for char in s.lower() if char.isalnum())
        
        answer = rmv_non_alphanum[::-1]
        
        if rmv_non_alphanum == answer:
            return True
        else:
            return False