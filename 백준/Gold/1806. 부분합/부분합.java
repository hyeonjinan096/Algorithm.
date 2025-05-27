import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());

        int[] nums = new int[N+1];
        st = new StringTokenizer(br.readLine());
        
        for (int i=0;i<N;i++){
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int left = 0;
        int sum = 0;
        int answer = Integer.MAX_VALUE;

        for(int right=0;right < N;right++){
            sum += nums[right];
            while(sum >= S){
                answer = Math.min(answer, right - left + 1);
                sum -= nums[left];
                left++;
            }
        }
        
        System.out.println(answer == Integer.MAX_VALUE ? 0 : answer);
    }
}