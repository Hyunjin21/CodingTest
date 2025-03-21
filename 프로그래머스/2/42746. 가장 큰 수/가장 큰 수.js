function solution(numbers) {
    var answer = '';
    const sorted = numbers.map(String).sort((a, b) => (b + a) - (a + b));
    answer = sorted.join('');
    return answer[0] === '0' ? '0' : answer;
    
}