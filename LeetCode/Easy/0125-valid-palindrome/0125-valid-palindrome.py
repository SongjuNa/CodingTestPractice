class Solution:
    def isPalindrome(self, s: str) -> bool:
        rmv_non_alphanum = "".join(char for char in s.lower() if char.isalnum())
        
        # 이제 깨끗해진 clean_s를 뒤집습니다.
        answer = rmv_non_alphanum[::-1]
        
        # clean_s와 뒤집은 answer를 비교합니다.
        if rmv_non_alphanum == answer:
            return True
        else:
            return False