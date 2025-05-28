import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Deque<String> q = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();

        for (int i=0;i<N;i++){
            String[] line = br.readLine().split(" ");
            String command = line[0];
            String x = "";
            if (line.length > 1) x = line[1];  
            
            switch (command) {
                case "push_front":
                    q.addFirst(x);
                    break;
                case "push_back":
                    q.addLast(x);
                    break;
                case "pop_front":
                    sb.append(q.isEmpty() ? -1:q.pollFirst()).append("\n");
                    break;
                case "pop_back":
                    sb.append(q.isEmpty() ? -1: q.pollLast()).append("\n");
                    break;
                case "size":
                    sb.append(q.size()).append("\n");
                    break;
                case "empty":
                    sb.append(q.isEmpty()?1:0).append("\n");
                    break;
                case "front":
                    sb.append(q.isEmpty() ? -1: q.peekFirst()).append("\n");
                    break;
                case "back":
                    sb.append(q.isEmpty() ? -1 : q.peekLast()).append("\n");
                    break;
            }
        }
        System.out.println(sb);
    }
}