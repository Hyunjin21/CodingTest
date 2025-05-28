function solution(numbers, k) {
    var idx = 0;
    idx = ((k-1)*2) % numbers.length;
    return numbers[idx];
}