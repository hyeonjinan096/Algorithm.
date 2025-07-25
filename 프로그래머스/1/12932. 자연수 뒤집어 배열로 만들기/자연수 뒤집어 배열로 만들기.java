class Solution {
    public int[] solution(long n) {
        String st = n + "";
        int[] answer = new int[st.length()];
        
        int cnt = 0;
        while(n > 0){
            answer[cnt] = (int)(n % 10);
            n /= 10;
            cnt += 1;
        }
        
        return answer;
    }
}