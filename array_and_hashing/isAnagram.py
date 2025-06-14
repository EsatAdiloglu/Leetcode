class Solution:
    def isAnagramMySolution(self, s: str, t: str) -> bool:
        '''
        I use a frequency table to keep track of which characters appear in s, and how many of a certain character has appeared
        At the end, I take the sum the frequency table to check if its 0.
        In the for loop for t, I have a if condition for if freq[idx] is 0. If it is, that means that the character in t did not
        appear in s, making both words not anagrams. This can be a bit efficient if the misplaced characters appears at the beginning of t
        Time Complexity: O(n + m + 1) => O(n + m), where n is the length of s and m is the length of t
        Because we have to loop through s and then loop through t. The '+1' is when sum(freq). Since we always know the size of freq,
        it is constant time
        Space Complexity: O(1) because freq always has 26 elements, so it is constant no matter the input
        
        I could definitely made this better by reducing the 2 for loops down into 1 for loop, but eh :P
        '''
        freq = [0] * 26
        for c in s:
            idx = ord(c) - ord('a')
            freq[idx] += 1
        for c in t:
            idx = ord(c) - ord('a')
            if freq[idx] == 0:
                return False
            freq[idx] -= 1
        return sum(freq) == 0

    def isAnagramSorting(self, s: str, t: str) -> bool:
        '''
        We sort both s and t, and then check if they're the same. This is because characters can be sorted with 'a' being first and 'z' being last.
        So Ex:
        s = "racecar"
        t = "carrace"
        sorted(s) = "aaccerr"
        sorted(t) = "aaccerr"
        Time Complexity: O(nlogn + mlogm) where n is the length of s and m is the length of t. We have to sort them, which is usually nlogn for quick sort
        Space Complexity: O(1) or O(n+m) because sorted is O(n). Idk what sorting algorithm is O(1) for strings so :P       
        '''
        if len(s) != len(t):
            return False
            
        return sorted(s) == sorted(t)
    
    def isAnagramHashMap(self, s: str, t: str) -> bool:
        '''
        We create a hashmap for both s and t. Then we loop through s, adding the characters of s and t to their respective hashmaps. Then we check if they're the same
        We use hashmaps because unlike list, hashmap has constant lookup time because it hashes the key
        Time Complexity: O(n + m) becaue we have to loop through s
        Space Complexity: O(1) because countS and countT will have at most 26 key-value pairs since there are 26 different characters
        in the english alphabet
        '''
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    
    def isAnagramHashTable(self, s: str, t: str) -> bool:
        '''
        We create count, which is a frequency table, with 26 elements. This is similar to my approach
        Then we loop through s, adding 1 with s's characters and removing 1 with t's characters
        After looping through s, we then check if each value is not equal to 0. If a value isn't
        equal to 0, that means that s and t aren't anagrams since either a character in s isn't in t or vice versa, and then we return False
        Time Complexity: O(n + m) because we have to loop through s.
        Space Complexity: O(1) because count is initialize to always have 26 elements
        '''
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True