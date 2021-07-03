package Programmers.level1;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Failure {
    public class Pair{
        public double failure = 0;
        public int index = 0;

        public Pair(double failure, int index){
            this.failure = failure;
            this.index = index;
        }

        public double getFailure() {
            return failure;
        }

        public int getIndex() {
            return index;
        }
    }

    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        int[] st = new int[N+2];
        for (int i=0; i<stages.length; i++){
            int index = stages[i];
            st[index]++;
        }

        int user = stages.length;
        List<Pair> fail = new ArrayList<Pair>();

        for (int i=0; i<N; i++){
            double failure = 0;
            if (user != 0) {
                failure = (double) st[i + 1] / (double) user;
            }
            user -= st[i+1];
            fail.add(new Pair(failure, i+1));
        }

        Collections.sort(fail, new Comparator<Pair>() {
            @Override
            public int compare(Pair o1, Pair o2) {
                if (o1.getFailure() > o2.getFailure())
                    return -1;
                else if (o1.getFailure() < o2.getFailure())
                    return 1;
                return 0;
            }
        });

        int i=0;
        for (Pair pair : fail) {
            answer[i++] = pair.getIndex();
        }

        return answer;
    }
}
