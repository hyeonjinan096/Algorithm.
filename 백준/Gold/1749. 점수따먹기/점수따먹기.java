import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[][] board;
    static int[][] prefix;

    public static void main(String[] args) throws IOException {
        // 입력 처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        board = new int[N + 1][M + 1];
        prefix = new int[N + 1][M + 1];

        // 점수 입력
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 누적합 배열 만들기
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= M; j++) {
                prefix[i][j] = board[i][j]
                        + prefix[i - 1][j]
                        + prefix[i][j - 1]
                        - prefix[i - 1][j - 1];
            }
        }

        int max = Integer.MIN_VALUE;

        // 모든 직사각형 구간 탐색
        for (int y1 = 1; y1 <= N; y1++) {
            for (int x1 = 1; x1 <= M; x1++) {
                for (int y2 = y1; y2 <= N; y2++) {
                    for (int x2 = x1; x2 <= M; x2++) {
                        int total = prefix[y2][x2]
                                - prefix[y1 - 1][x2]
                                - prefix[y2][x1 - 1]
                                + prefix[y1 - 1][x1 - 1];
                        max = Math.max(max, total);
                    }
                }
            }
        }

        System.out.println(max);
    }
}
