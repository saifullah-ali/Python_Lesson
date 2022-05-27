class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        numRansome = len(ransomNote)
        for letter in magazine:
            for i in ransomNote:
                print(f'letter {letter} and i is {i}')
                if letter == i:
                    numRansome = numRansome - 1
                    ransomNote = ransomNote.replace(letter,"",1)
                    break
        print(numRansome)
        if numRansome == 0:
            return True
        else:
            return False

d = Solution()
print(d.canConstruct("aa","aab"))