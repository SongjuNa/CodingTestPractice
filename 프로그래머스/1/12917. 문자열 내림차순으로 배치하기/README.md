# [level 1] 문자열 내림차순으로 배치하기 - 12917 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12917?language=python3) 

### 성능 요약

메모리: 8.91 MB, 시간: 0.05 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2026년 05월 14일 14:43:58

### 문제 설명

<p>문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.<br>
s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.</p>

<h5>제한 사항</h5>

<ul>
<li>str은 길이 1 이상인 문자열입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>"Zbcdefg"</td>
<td>"gfedcbZ"</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges


### [오답 정리]
- 핵심 개념: 문자열 정렬

- 나의 실수: 1. sorted() 함수는 아스키 코드 기준으로 알파벳 순서 정렬하고 원본 안바꿈/ list.sort() 함수는 오름차순 정렬이고 문자열에서 리스트에서만 사용 가능, 원본 리스트 바꿈
           2. sorted()함수는 리스트로 리턴

- 해결: 파이썬 함수 헷갈리지 않게 잘 익히기
