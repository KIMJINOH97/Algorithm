package Programmers.level1;

class Solution {
    public static void main(String[] args) {
        System.out.println(solution("z-+.^."));
    }

    public static String solution(String new_id) {
        new_id = new_id.toLowerCase();
        StringBuilder st = new StringBuilder();
        for(int i=0; i<new_id.length(); i++){
            char s = new_id.charAt(i);
            if (Character.isDigit(s) || Character.isAlphabetic(s) || s == '.' || s == '_' || s == '-'){
                st.append(s);
            }
        }
        new_id = String.valueOf(st);
        new_id = new_id.replaceAll("\\.+", ".");

        int id_len = new_id.length();
        char first = new_id.charAt(0);
        char last = new_id.charAt(id_len-1);

        if (first == '.'){
            new_id = new_id.substring(1);
        }

        if (last == '.'){
            new_id = new_id.substring(0, id_len-1);
        }

        if (new_id.length() == 0){
            new_id = "a";
        }

        if (new_id.length() >= 16){
            new_id = new_id.substring(0, 15);
        }

        int index = 0;
        for (int i = new_id.length()-1; i >= 0; i--){
            char s = new_id.charAt(i);
            if (s != '.'){
                index = i;
                break;
            }
        }

        new_id = new_id.substring(0, index+1);
        id_len = new_id.length();
        if (id_len < 3){
            last = new_id.charAt(id_len-1);
            for(int i=0; i<3-id_len; i++){
                new_id += last;
            }
        }

        return new_id;
    }
}