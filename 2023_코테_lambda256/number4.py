# 임의의 숫자가 적힌 N개의 카드가 있습니다.
# 카드를 이용하여 증가구간을 가장 많이 만드는것이 목적입니다.
# 증가구간이란 카드를 배치했을 때, k-1번쨰 카드보다 k번째 카드가 더 큰 경우를 말합니다. 이 경우 1개로 셉니다.
# 만약 카드목록 P = [3,2,1,4,5] 로 주어질 때, P를 [1,2,3,4,5]로 배치하게 되면 
# 증가구간은 2개(1->4, 4->5)에서 4개(1->2, 2->3, 3->4, 4->5)로 증가합니다.이 경우 리턴 값은 최댓값인 4가 됩니다. 
# 위 문제에 대한 입출력 예시를 제공해줄게. 
# 입력이 [3, 2, 1, 4, 5] 일때, 출력은 4
# 입력이 [20, 10, 10, 20] 일때, 출력은 2 
# 입력이 [103, 101, 103, 103, 101, 102, 100, 100, 101, 104]일떄, 출력은 7 

# 카드 목록 P가 주어질 때, 배치를 바꾸어 증가구간의 최댓값을 반환하는 함수를 완성해 주세요. 
# python으로 solution()을 구현해주세요. 배열 p가 매개변수로 주어집니다. 
# 메모리 가 얼마나 사용되는지도 알려주세요.


from itertools import permutations

def count(arr):
  cnt = 0
  for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
      cnt += 1
  return cnt

def solution(cards):
  max_cnt = 0
  for arrangement in permutations(cards):
    cnt = count(arrangement)
    max_cnt = max(max_cnt, cnt)
  return max_cnt

# 예시 테스트 케이스
test_case_1 = [3, 2, 1, 4, 5]
test_case_2 = [20, 10, 10, 20]
test_case_3 = [103, 101, 103, 103, 101, 102, 100, 100, 101, 104]

result_1 = solution(test_case_1)
result_2 = solution(test_case_2)
result_3 = solution(test_case_3)

print("Test Case 1:", result_1)  # 출력 결과: 4
print("Test Case 2:", result_2)  # 출력 결과: 2
print("Test Case 3:", result_3)  # 출력 결과: 7


from itertools import permutations #permutations 모듈 import

def count(arr):
  cnt = 0
  
  for i in range(len(arr)-1): #모든 카드 쌍 반복
    if arr[i] < arr[i+1]: #인접 카드 비교
      cnt += 1 #증가구간 처리

  return cnt #증가구간 개수 반환
  

def solution(cards):

  max_cnt = 0 #최대 증가구간 개수

  for arrangement in permutations(cards): #모든 배열 순열 반복

    cnt = count(arrangement) #순열 별 증가구간 개수 세기

    max_cnt = max(max_cnt, cnt) #최댓값 업데이트

  return max_cnt #최종 최댓값 반환