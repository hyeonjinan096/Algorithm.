import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        List<List<int[]>> graph = new ArrayList<>();
        for(int i=0;i<N+1;i++){
            graph.add(new ArrayList<>());
        }
        
        for (int i=0;i<M;i++){
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int C = Integer.parseInt(st.nextToken());
            graph.get(A).add(new int[]{B,C});
            graph.get(B).add(new int[]{A,C});
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(x->x[1]));
        pq.offer(new int[]{1,0});

        int[] dp = new int[N+1];
        Arrays.fill(dp,Integer.MAX_VALUE);

        while(!pq.isEmpty()){
            int[] cur = pq.poll();

            int x = cur[0];
            int cost = cur[1];

            if (x == N) break;
            if (cost > dp[x]) continue;

            for(int[] next : graph.get(x)){
                int next_x = next[0];
                int next_cost = cost + next[1];
                
                if (dp[next_x] <= next_cost) continue;

                dp[next_x] = next_cost;
                pq.offer(new int[]{next_x,next_cost});
            }
        }

        System.out.println(dp[N]);

        
        
    }
}