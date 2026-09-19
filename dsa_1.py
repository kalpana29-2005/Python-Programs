#You are given two strings word1 and word2. Merge the strings by adding letters in alternating
#  order, starting with word1. If a string is longer than the other, append the additional letters 
# onto the end of the merged string.Return the merged string.
class Solution:
    def mergealternately(self,word1:str,word2:str)->str:
        result=""
        i,j=0,0

        while i<len(word1) and j<len(word2):
            result+=word1[i]
            result+=word2[j]
            i+=1
            j+=1
        result+=word1[i:]
        result+=word2[j:]
        return result
    
if __name__=="__main__":
    word1=input("Enter first string: ")

    word2=input("Enter second string: ")
    obj=Solution()
    print(obj.mergealternately(word1,word2))