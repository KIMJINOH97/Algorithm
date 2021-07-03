<h1 align="center">Algorithm :turtle:</h1>
<p>
</p>

JAVA 자료구조 별 Method 요약

<h2>String 클래스 관련</h2>
<table>
    <th>Method</th>
    <th>Return</th>
    <th>Ex</th>
    <tr>
        <td><b>str.split("")</b></td>
        <td>문자열을 기준에 다라 나눠 String[] 반환</td>
        <td>
            String str = "I am jinoh" <br>
            str.split(" ") -> ['I', 'am', 'jinoh']<br>
        </td>
    </tr>
    <tr>
        <td><b>str.toLowerCase()</b></td>
        <td>문자열의 소문자로 바꾸어 반환</td>
        <td>
            String str = "AbCDe" <br>
            str.toLowerCase() -> "abcde"<br>
        </td>
    </tr>
    <tr>
        <td><b>str.replaceAll("regex", "바꿀문자")</b></td>
        <td>정규표현식에 해당하는 문자열을 바꿀문자로 바꾼뒤 String으로 반환</td>
        <td>
            String str = "ABCAB" <br>
            str.replaceAll("A", "B") -> "BBCBB" <br>
        </td>
    </tr>
    <tr>
        <td><b>str.charAt(index)</b></td>
        <td>문자열의 해당하는 index를 char로 뽑아냄</td>
        <td>
            String str = "abcde" <br>
            str.charAt(1) -> 'b'<br>
        </td>
    </tr>
    <tr>
        <td><b>str.subString(start, end)</b></td>
        <td>문자열의 index의 start ~ end-1까지 추출해 String 반환</td>
        <td>
            String str = "abcde" <br>
            str.charAt(1) -> 'b'<br>
        </td>
    </tr>
</table>

<h2>Sort </h2>

```
    // ArrayList를 Sort 하고 싶다면, interface인 Comparable 과 Comparator 구현 하여여 함,.
    
    // 기본 array sort
    int[] arr = {2, 1, 3, 4, 2, 5};
    Arrays.sort(arr);
    >> 결과: [1, 2, 2, 3, 4, 5]
    
    // Collection의 List<T>정렬하기 (예시는 내림차순)
    List<Pair> pair = new ArrayList<Pair>();
    for (int i=0; i<10; i++){
        pair.add(new Pair(i, 0));
    }
    
    Collections.sort(pair, new Comparator<Pair>() {
            @Override
            public int compare(Pair o1, Pair o2) {
                if (o1.index > o2.index)
                    return -1;
                else if (o1.index < o2.index)
                    return 1;
                return 0;
            }
        });
    
    >> 결과 : [9, 8, 7, 6, ..... 0]
    
    public class Pair{
        public int index = 0;
        public int num = 0;

        public Pair(double failure, int index){
            this.failure = failure;
            this.index = index;
        }
    }

```