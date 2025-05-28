import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        Deque<int[]> numq = new ArrayDeque<>();
        
        for(int i=1;i<N+1;i++){
            int n = Integer.parseInt(st.nextToken());
            numq.add(new int[]{i,n});
        }

        StringBuilder answer = new StringBuilder();
        int[] target = numq.pollFirst();
        answer.append(target[0]).append(" ");
        
        while(numq.size() > 0){
            if (target[1] > 0){
                for (int i=0;i<target[1]-1;i++){
                    numq.addLast(numq.pollFirst());    
                }
                target = numq.pollFirst();
            }
            else {
                for(int i=0;i<Math.abs(target[1])-1;i++){
                    numq.addFirst(numq.pollLast());
                }
                target = numq.pollLast();
            }
            answer.append(target[0]).append(" ");
        }

        System.out.println(answer.toString().trim());
        
    }
}