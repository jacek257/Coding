class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        start, end = 0, 0
        cur_len = 0
        self.words = words

        while end < len(words):
            cur_len += len(words[end])
            if cur_len >= maxWidth:
                if cur_len > maxWidth:
					# Remove the last word and the space before it
                    cur_len -= (len(words[end])+1)
                    end -= 1
				# If its the last line, extra space added is 0
                ans.append(self.get_line(start, end, 0 if e == len(words)-1 else (maxWidth - cur_len)))
                cur_len = 0
                start, end = end+1, end+1
            elif cur_len < maxWidth:
                # For 1 space
                cur_len += 1
                end += 1
        if cur_len > 0:
            ans.append(self.get_line(start, end-1, 0))
            last = ans[-1]
            extra = maxWidth - len(last)
            ans[-1] = last + ' '*extra
        return ans


    def get_line(self, start, end, spaces):
        line = ''
        if start == end:
            line = self.words[end] + (' '*spaces)
            return line
        word_count = end-start
        dist_space, extra = 1+ spaces//word_count, spaces%word_count
        while start <= end:
            line += self.words[start]
            if start < end:
                line += (' '* dist_space)
            if extra > 0:
                line += ' '
                extra -= 1
            start += 1
        return line
