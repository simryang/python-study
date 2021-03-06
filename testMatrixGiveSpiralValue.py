#http://codingdojang.com/scode/266?answer=7784#answer_7784
'''
문제는 다음과 같다:

6 6

  0   1   2   3   4   5
 19  20  21  22  23   6
 18  31  32  33  24   7
 17  30  35  34  25   8
 16  29  28  27  26   9
 15  14  13  12  11  10
위처럼 6 6이라는 입력을 주면 6 X 6 매트릭스에 나선형 회전을 한 값을 출력해야 한다.
'''
'''
이를 선형으로 펴서 변화가 일어나는 부분을 보자
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35
          *          *              *           *           *        *        *     *     *  *  *
          6          5              5           4           4        3        3     2     2  1  1
숫자는 0에서 시작이지만 이를 첫번째(1)라고 인지한다면 6번째까지 동일 패턴이고 여기에서 변화가 일어났고
이 처음 한번을 제외하면 2번마다 변화량이 줄어들었다.
처음 6은 맨 처음 열의 길이와 일치한다.
m x n 행렬이면 m개의 행과 n 개의 열을 뜻한다.
위 예에서는 m=6, n=6 에서 첫 n=6 만큼 동일 패턴(열 위치 증가) 후
다음 패턴(행 위치 증가)은 m - 1(5) 만큼 변화했고,
다음 패턴(열 위치 감소)은 n - 1(5) 만큼 변화했고,
다음 패턴(행 위치 감소)은 m - 2(4) 만큼 변화했고,
다음 패턴(열 위치 증가)은 n - 2(4) 만큼 변화했고
다음 패턴(행 위치 증가)은 m - 3(3) 만큼 변화했다.
...
선형일 때의 인덱스(1부터 시작시)로 치면
 1일 때 n - 1만큼 n++ (또는 0일 때 n만큼 n++)
 6일 때 m - 1만큼 m++
11일 때 n - 1만큼 n--
16일 때 m - 2만큼 m--
20일 때 n - 2만큼 n++
24일 때 m - 3만큼 m++
...
'''