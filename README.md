<h1 align="center">Algorithm study👋</h1>
<p>
</p>

> 알고리즘 python method 요약

## String
<table>
    <th>Method</th>
    <th>Return</th>
    <th>ex</th>
    <tr>
        <td><b>str.find()</b></td>
        <td>매개변수로 입력한 문자열의 index 반환 없으면 -1</td>
        <td>
            str = 'abba' <br>
            str.find('a') -> 1 반환<br>
            str.find('a', 2) -> 3반환<br>
            </td>
    </tr>
    <tr>
        <td><b>str.startswith()</b></td>
        <td>문자열의 앞에서 부터 찾아 index 반환 없으면 -1</td>
        <td>
        str = 'I am jinoh' <br>
        str.startswith('I') -> True <br>
        str.startswith('I am') -> True
    </td>
    </tr>
    <tr>
        <td><b>str.endswith()</b></td>
        <td>매개변수로 문자열이 끝나면 True, 그렇지 않으면 False</td>
        <td>
            str = 'I am jinoh' <br>
            str.endswith('jinoh') -> True <br>
            str.endswith('joh') -> false <br>
        </td>
    </tr>
    <tr>
        <td><b>str.count()</b></td>
        <td>매개변수의 문자열이 몇개 있는지 반환(대 소문자 구분)</td>
        <td>
            str('문자열', 시작위치, 끝위치) 가능
            str = 'I am jinoh' <br>
            str.count('i') -> 1반환<br>
            str.count('o', 7, len(str)) -> 1반환 <br>
    </td>
    </tr>
    <tr>
        <td><b>str.index()</b></td>
        <td>find와 동일하나 없으면 ValueError</td>
        <td>
            str = 'I am jinoh' <br>
            str.index('a') -> 3반환<br>
            str.index('k') -> ValueError
        </td>
    </tr>
    <tr>
        <td><b>str.isalpha()</b></td>
        <td>문자열이 영어,한글로만 이루어졌으면 True 아니면 False</td>
        <td>
            str1 = 'I am jinoh' <br>
            str2 = '123 I am'<br>
            str1.isalpha() -> True<br>
            str2.isalpha() -> False
        </td>
    </tr>
</table>


## list


## dictionary


## 정규표현식


Give a ⭐️ if this project helped you!

***

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
