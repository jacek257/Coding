class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        int start=0, end=0;
        int curLen = 0;
        List<String> ans = new ArrayList<>();

        while(end < words.length) {
            curLen += words[end].length();
            if (curLen >= maxWidth) {
                if(curLen > maxWidth) {
                    curLen -= words[end].length()+1;
                    end -= 1;
                }

                ans.add(getLine(words, start, end, end==words.length-1 ? 0 : maxWidth-curLen));
                curLen = 0;
                start = ++end;
            }
            else if (curLen < maxWidth) {
                curLen++;
                end++;
            }
        }
        if(curLen > 0) {
            ans.add(getLine(words, start, end-1, 0));
            String last = ans.get(ans.size()-1);
            int extra = maxWidth - last.length();
            ans.set(ans.size()-1, last + " ".repeat(extra));
        }

        return ans;
    }

    private String getLine(String[] words, int start, int end, int spaces) {
        String line = "";
        if(start == end) {
            line = words[end] + " ".repeat(spaces);
            return line;
        }
        int wordCount = end-start;
        int distSpace = (spaces/wordCount)+1;
        int extra = spaces%wordCount;

        while(start <= end) {
            line = line + words[start];
            if(start < end) {
                line = line + " ".repeat(distSpace);
            }
            if(extra > 0) {
                line = line + " ";
                extra--;
            }
            start++;

        }

        return line;
    }
}
