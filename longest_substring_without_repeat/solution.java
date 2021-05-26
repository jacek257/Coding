class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> seen = new HashSet<>();
        int start = 0;
        int longest = 0, tmp = 0;

        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if(seen.add(c)){
                tmp++;
            }
            else {
                if(tmp > longest){
                    longest = tmp;
                }
                int pos = s.indexOf(c, start);
                if(pos < i) {
                    tmp -= pos-start;
                    start = pos+1;
                }
                else{
                    tmp++;
                }
            }
        }

        if(tmp > longest){
            longest = tmp;
        }
        return longest;
    }
}
