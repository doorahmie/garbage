/**
 * 자연수 num이 주어질 때, num보다 크거나 같은 자연수 중에 다음 조건을 만족하는 가장 작은 수를 구하려 합니다. 

- 구하는 숫자의 자릿수는 짝수여야 합니다. 
- 숫자가 2 x n 자릿수 일때, 앞 n자리의 각자릿수 곱과 뒤 n자리의 각 자릿수 곱이 같아야 합니다. 
num이 매개변수로 주어집니다. 

solution()이라는 함수를 javascript로 구현해주세요.
*/

function solution(num) {
    let n = 2;
    while (true) {
      let numString = String(num);
      let halfLength = numString.length / 2;
      let firstHalf = numString.substring(0, halfLength);
      let secondHalf = numString.substring(halfLength);
      let firstHalfProduct = [...firstHalf].reduce((acc, digit) => acc * Number(digit), 1);
      let secondHalfProduct = [...secondHalf].reduce((acc, digit) => acc * Number(digit), 1);
      if (firstHalfProduct === secondHalfProduct) {
        return num;
      }
      num++;
    }
  }

  // tc  21 답 22
  // tc 3462 답 2462
  // tc 235386
const answer =  solution(235386);
console.log(answer)



function solution1(num) {
  // n을 2로 초기화합니다.
  let n = 2;
  // 무한 루프를 시작합니다.
  while (true) {
    // 주어진 숫자를 문자열로 변환합니다.
    let numString = String(num);
    // 숫자의 반을 계산합니다.
    let halfLength = numString.length / 2;
    // 숫자의 앞 부분을 추출합니다.
    let firstHalf = numString.substring(0, halfLength);
    // 숫자의 뒷 부분을 추출합니다.
    let secondHalf = numString.substring(halfLength);
    // 앞 부분의 각 자릿수를 곱한 결과를 계산합니다.
    let firstHalfProduct = [...firstHalf].reduce((acc, digit) => acc * Number(digit), 1);
    // 뒷 부분의 각 자릿수를 곱한 결과를 계산합니다.
    let secondHalfProduct = [...secondHalf].reduce((acc, digit) => acc * Number(digit), 1);
    // 앞 부분과 뒷 부분의 곱이 같으면 현재 숫자를 반환합니다.
    if (firstHalfProduct === secondHalfProduct) {
      return num;
    }
    // 숫자를 증가시킵니다.
    num++;
  }
}