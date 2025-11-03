class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int ans = 0;
        for (int i = 0;i<stones.length();i++){
            char ch = stones.charAt(i);
            boolean found = false;
            for (int j = 0; j< jewels.length();j++){
                char die = jewels.charAt(j);
                if(ch == die){
                    found = true;
                    break;
                }
            }
            if (found == true){
                ans += 1;
            }
        }
        return ans;        
    }
}