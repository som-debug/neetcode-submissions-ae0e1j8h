class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        initPrefix = strs[0]
        j = 1 ;
        while j < len(strs):
            currentString = strs[j]
            res = ""
            if(len(currentString) == 0):
                return res
            for i in range(min(len(initPrefix),len(currentString))):
                if initPrefix[i] == currentString[i]:
                    res = res + currentString[i]
                elif len(res) == 0:
                    return res
                else:
                    initPrefix = res
                    break
            initPrefix = res
    
            j += 1


        return initPrefix
                    
                
        