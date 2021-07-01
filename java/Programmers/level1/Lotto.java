package Programmers.level1;

import java.util.*;

public class Lotto {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = {0, 0};
        int max_count = 0;
        int min_count = 0;

        for (int i =0; i<lottos.length; i++){
            if(lottos[i] == 0){
                max_count++;
                continue;
            }

            for(int j=0; j<win_nums.length; j++){
                if(win_nums[j] == lottos[i]){
                    max_count++;
                    min_count++;
                }
            }
        }

        Map<Integer, Integer> score = new HashMap<>();
        for(int i=1; i<7; i++){
            score.put(7-i, i);
        }
        score.put(0, 6);

        answer[0] = score.get(max_count);
        answer[1] = score.get(min_count);

        return answer;
    }
}