class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = s.replace(" ", "")
        clean_text = "".join(char for char in clean_text if char.isalnum())
        if clean_text.lower() == clean_text[::-1].lower():
            return True
        return False


        