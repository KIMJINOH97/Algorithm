<h1 align="center">Algorithm :turtle:</h1>
<p>
</p>

> 알고리즘 python method 요약

## Str 관련 Method
<table>
    <th>Method</th>
    <th>Return</th>
    <th>Ex</th>
    <tr>
        <td><b>str.split()</b></td>
        <td>문자열을 기준에 다라 나눠 list로 반환</td>
        <td>
            str = 'I am jinoh' <br>
            str.split() -> ['I', 'am', 'jinoh']<br>
        </td>
    </tr>
    <tr>
        <td><b>'string'.join()</b></td>
        <td>문자열의 원하는 부분을 바꿔줌</td>
        <td>
            li = ['I', 'am', 'jinoh']
            ' 'join(li) -> 'I am jinoh'<br>
        </td>
    </tr>
    <tr>
        <td><b>str.replace()</b></td>
        <td>문자열의 원하는 부분을 바꿔줌</td>
        <td>
            str = 'I am jinoh' <br>
            str.replace('jinoh', 'python') -> 'I am python'<br>
        </td>
    </tr>
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
            str.count('o', 7, len(str)) -> 1반환
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
    <tr>
        <td><b>str.isdigit()</b></td>
        <td>문자열이 숫자로만 이루어졌으면 True 아니면 False</td>
        <td>
            str1 = 'I am jin5' <br>
            str2 = '123124'<br>
            str1.isdigit() -> False<br>
            str2.isdigit() -> True
        </td>
    </tr>
    <tr>
        <td><b>str.islower()</b></td>
        <td>문자열이 모두 소문자로만 되어졌으면 True 아니면 False</td>
        <td>
            str1 = 'I am jinoh'<br>
            str2 = 'I AM JINOH'<br>
            str1.isalpha() -> True<br>
            str2.isalpha() -> False
        </td>
    </tr>
    <tr>
        <td><b>str.isupper()</b></td>
        <td>문자열이 모두 대문자로만 되어졌으면 True 아니면 False</td>
        <td>
            str1 = 'I am jinoh'<br>
            str2 = 'I AM JINOH'<br>
            str1.isupper() -> False<br>
            str2.isupper() -> True
        </td>
    </tr>
    <tr>
        <td><b>str.lower()</b></td>
        <td>문자열을 모두 소문자로 변환</td>
        <td>
            str1 = 'I Am jinoh'<br>
            str1.lower() -> 'i am jinoh' 반환
        </td>
    </tr>
    <tr>
        <td><b>str.upper()</b></td>
        <td>문자열을 모두 대문자로 변환</td>
        <td>
            str1 = 'I am jinoh'<br>
            str1.upper() -> 'I AM JINOH' 반환
        </td>
    </tr>
</table>


## list 관련 Method

<table>
    <th>Method</th>
    <th>Return</th>
    <th>Ex</th>
    <tr>
        <td><b>list.append()</b></td>
        <td>해당 리스트에 매개변수를 맨 뒤에 추가 반환값 X</td>
        <td>
            li = ['I', 'am'] <br>
            li.append('jinoh') -> ['I', 'am', 'jinoh'] <br>
        </td>
    </tr>
    <tr>
        <td><b>list.pop()</b></td>
        <td>해당 리스트에 지정 인덱스를 제거 후 그 수를 반환</td>
        <td>
            li = ['I', 'am', 'kim', 'jinoh']<br>
            li.pop() -> ['I', 'am', 'kim'] default -1번째<br>
            li.pop(1) -> li = ['I', 'kim'] return 'jinoh'
        </td>
    </tr>
    <tr>
        <td><b>list.count()</b></td>
        <td>매개변수의 문자열이 몇개 있는지 반환(대 소문자 구분)</td>
        <td>
            str('문자열', 시작위치, 끝위치) 가능
            str = 'I am jinoh' <br>
            str.count('i') -> 1반환<br>
            str.count('o', 7, len(str)) -> 1반환
    </td>
    </tr>
</table>

## dictionary


## 정규표현식

<table>
    <th>Method</th>
    <th>Return</th>
    <tr>
        <td><b>p.match(str)</b></td>
        <td>문자열이 조건에 맞는지 판단해 객체를 반환</td>
    </tr>
    <tr>
        <td><b>p.findall(str)</b></td>
        <td>조건에 맞는 문자열만 반환</td>
    </tr>
    <tr>
        <td><b>p,match(str)</b></td>
        <td>문자열이 조건에 맞는지 판단</td>
    </tr>
</table>


```
import re

str = '1a2b3c4d'
p = re.compile('[a-zA-Z]') // 위 코드의 축약 result = re.match('[a-z]+', "1a2b3c4d")
p.findall(str) // ['a', 'b', 'c', 'd']
p.match(str) // 'None'

all = re.compile('[a-zA-Z]+')
result = all.match(str)
print(result.group()) // '1a2b3c4d'
    
```
Give a ⭐️ if this project helped you!

***

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
