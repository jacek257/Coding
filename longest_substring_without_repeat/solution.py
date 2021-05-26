class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0;
        tmp = 0;
        seen = set();
        start = 0
        for i, char in enumerate(s):
            if char not in seen:
                seen.add(char)
                tmp += 1

            else:
                if tmp > longest:
                    longest = tmp
                pos = s[start:i].find(char)
                tmp -= pos
                start += pos+1

        if tmp > longest:
            longest = tmp

        return longest
            
