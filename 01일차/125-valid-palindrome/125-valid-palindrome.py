class Solution:
    def isPalindrome(self, s: str) -> bool:
        correct_list = []
        
        for char in s:
            if char >= 'a' and char <= 'z':
                correct_list.append(char)
            if char >= 'A' and char <= 'Z':
                correct_list.append(char.lower()) # 대문자를 소문자로 바꿔주는 string.lower() 함수
            if char.isdigit():
                correct_list.append(char)
        
        # 리스트의 요소를 역순으로 바꿔서 반환하는 reversed 함수
        reverse_list = list(reversed(correct_list)) 
        
        correct_str = "".join(correct_list) # 리스트를 문자열로 바꿔주는 string.join() 함수
        reverse_str = "".join(reverse_list)
        
        if correct_str == reverse_str:
            return True
        return False