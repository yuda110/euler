"""
다음은 연속된 1000자리 숫자입니다.
이런 식으로 맨 처음 (7 × 3 × 1 × 6 × 7 = 882) 부터 맨 끝 (6 × 3 × 4 × 5 × 0 = 0) 까지 5자리 숫자들의 곱을 구할 수 있습니다.
이렇게 구할 수 있는 5자리 숫자의 곱 중에서 가장 큰 값은 얼마입니까?
"""

import functools
import operator
from py_modules.timer import logging_time

# def multiple_five_num(five_num) :
#     multiple = 1
#     for i in range(0, 5) :
#         multiple = multiple * int(five_num[i])
#     return multiple


# def pickup_multiple_five_num(num):
#     range_to = len(num)
#     max_num = 0
#     for i in range(5, range_to+1) :
#         five_num = num[i-5 : i]
#         multiple_num = multiple_five_num(five_num)
#         if max_num < multiple_num :
#             max_num = multiple_num
#     return max_num


@logging_time
def solution(num):
    result = 0
    num_list = [int(i) for i in num]    # for loop 안에서 자료형 변환 중복을 방지하기 위해 먼저 해둠
    for idx, _ in enumerate(num_list[:-4]):
        five_list = num_list[idx:idx + 5]
        mul = functools.reduce(operator.mul, five_list)
        if mul > result:
            result = mul
    print(result)


if __name__ == '__main__':
    n = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    solution(n)
