function solution(numer1, denom1, numer2, denom2) {
    var answer = [];
    var num = denom1*numer2 + denom2*numer1;
    var denom = denom1*denom2;
    const gcd = (a, b) => (a % b === 0 ? b : gcd(b, a % b));
    const result = gcd(num, denom); 
    answer[0] = num/result;
    answer[1] = denom/result;
    return answer;
}