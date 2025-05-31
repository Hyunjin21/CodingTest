function solution(numbers) {
    var answer = 0;
    let arr = numbers.sort((a, b) => b - a);
    answer = arr[0] * arr [1];
    return answer;
}