# 한번에 최대 N잔까지 동시에 커피를 추출할 수 있는 기계가 있다. 이 기계를 이용해 커피를 만들 때, 커피가 만들어지는 순서를 구하자.

# 만들어지는 커피가 M잔이면, 커피에 1부터 M까지 순서대로 주문번호가 붙어있다. 
# 주문번호 순으로 빈 커피 추출구에서 커피를 만들기 시작한다.
# 만약 빈 추출구가 없다면, 빈 추출구가 생길때까지 다음 주문은 잠시 기다리며, 빈 추출구가 생기면 대기중인 다음 커피를 즉시 만든다.

# 커피종류별로 만드는 시간은 다르다.
# 아래는 이 알고리즘의 입출력 예시이다.

# N=3, coffee_times = [4,2,2,5,3] 일때, return값은 [2,3,1,5,4]이다.
# N=1, coffee_times = [100,1,50,1,1] 일때, return값은 [1,2,3,4,5]이다.

# 커피 추출구 개수 N,
# 커피를 만드는데 걸리는 시간이, 주문번호 순서대로 담긴 배열 coffee_times가 매개변수로 주어진다.
# 커피가 완성되는 순서대로 주문번호를 배열에 담아 return하도록 solution 함수를 완성해보자.



import heapq

def solution(N, coffee_times):
    answer = []
    heap = []  # (종료 시간, 추출구 인덱스)
    idx = 0    # 현재 주문번호

    while idx < len(coffee_times) or heap:
        # 빈 추출구가 있고, 주문번호가 모두 처리되지 않았다면
        while len(heap) < N and idx < len(coffee_times):
            heapq.heappush(heap, (coffee_times[idx], idx + 1))  # (커피가 완성되는 시간, 주문번호)
            idx += 1

        # 가장 먼저 끝나는 커피 추출구 찾기
        time, order = heapq.heappop(heap)
        answer.append(order)

        # 다음 주문이 있으면 해당 추출구에 할당
        if idx < len(coffee_times):
            heapq.heappush(heap, (time + coffee_times[idx], idx + 1))
            idx += 1

    return answer

# 예시
print(solution(3, [4, 2, 2, 5, 3]))  # [2, 3, 1, 5, 4]
print(solution(1, [100, 1, 50, 1, 1]))  # [1, 2, 3, 4, 5]


# 물론이죠! 주어진 문제를 해결하기 위한 코드의 동작을 자세히 설명하겠습니다.

# 1. `heap`은 최소 힙으로 구현된 리스트로, (커피가 완성되는 시간, 주문번호)의 튜플이 저장됩니다. 이 힙을 통해 가장 일찍 완성되는 커피를 추출할 수 있습니다.

# 2. `idx`는 현재까지 처리한 주문의 개수를 나타내며, 이 값은 `coffee_times` 배열의 인덱스를 나타냅니다. 

# 3. `while idx < len(coffee_times) or heap:` 루프는 모든 주문이 처리될 때까지 또는 `heap`에 남아있는 커피가 있다면 계속해서 실행됩니다.

# 4. 내부의 `while len(heap) < N and idx < len(coffee_times):` 루프는 빈 추출구에 커피를 할당하는 역할을 합니다. 빈 추출구의 개수가 `N`보다 작고, 아직 처리되지 않은 주문이 남아 있다면 계속해서 루프가 실행됩니다.

#     - `heapq.heappush(heap, (coffee_times[idx], idx + 1))`: 빈 추출구에 커피를 할당합니다. 여기서 `idx + 1`은 주문번호를 나타냅니다. 주문번호는 1부터 시작하므로 `idx + 1`을 사용합니다.
    
#     - `idx += 1`: 다음 주문으로 넘어갑니다.

# 5. `while heap:` 루프는 `heap`에 남아있는 커피가 있는 동안 계속해서 실행됩니다.

#     - `time, order = heapq.heappop(heap)`: `heap`에서 가장 일찍 완성되는 커피를 추출합니다. `time`은 커피가 완성되는 시간이고, `order`는 주문번호입니다.

#     - `answer.append(order)`: 추출된 커피의 주문번호를 정답 리스트에 추가합니다.

#     - `if idx < len(coffee_times):`: 처리되지 않은 주문이 남아 있다면, 해당 주문을 가장 일찍 완성되는 추출구에 할당합니다.

#         - `heapq.heappush(heap, (time + coffee_times[idx], idx + 1))`: 이전에 추출된 커피가 완성된 시간에 새로운 주문의 커피 만드는 시간을 더하여 힙에 추가합니다.

#         - `idx += 1`: 다음 주문으로 넘어갑니다.

# 이런 방식으로 코드는 주어진 조건에 따라 커피를 만드는 순서를 반환합니다. 최소 힙을 사용하여 항상 가장 일찍 완성되는 커피를 추출하고, 빈 추출구에 새로운 주문을 할당하여 효율적으로 동작합니다.