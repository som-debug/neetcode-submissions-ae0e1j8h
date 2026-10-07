class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s) - 1
        i = 0
        while i<n:
            while not (re.fullmatch(r"[A-Za-z0-9]+", s[i])):
                i += 1 
                if i>=n:
                    break
            
            while not ( re.fullmatch(r"[A-Za-z0-9]",s[n])):
                n -= 1
                if n <= i:
                    break
            print(s[i],i,s[n], n)    
            if i<=n and (s[i].casefold() == s[n].casefold()) :
                i += 1
                n -= 1
            elif re.fullmatch(r"[A-Za-z0-9]",s[n]) and re.fullmatch(r"[A-Za-z0-9]",s[i]) and (s[i].casefold() != s[n].casefold()):
                # print(s[i],i,s[n], n)
                return False
        
        return True
        