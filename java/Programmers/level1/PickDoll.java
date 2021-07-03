package Programmers.level1;

import java.util.*;

class PickDoll {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();

        for(int i=0; i<moves.length; i++){
            int index = moves[i]-1;
            int doll = -1;
            for (int j=0; j<board.length; j++){
                int b = board[j][index];
                if (b != 0){
                    doll = b;
                    board[j][index] = 0;
                    break;
                }
            }
            if (doll == -1) continue;

            if (stack.size() > 0 && stack.peek() == doll){
                stack.pop();
                answer += 2;
                continue;
            }

            stack.push(doll);

        }

        return answer;
    }
}
