import java.util.Arrays;
import java.util.Collections;

class Solution {
    public String solution(String s) {
        String answer = "";
        //s를 배열로 만든다. 
        String[] str = s.split("");
        
        //Arrays.sort를 사용한다. 
        Arrays.sort(str, Collections.reverseOrder())
;
        // 배열을 다시 String으로 만든다.
        for(String a:str)
            answer += a;
        
        return answer;
        
    }
}