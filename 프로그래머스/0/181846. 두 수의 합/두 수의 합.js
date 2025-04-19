function solution(a, b) {
    var answer = '';
    var carry = 0; // 올림수
    
    let i = a.length - 1;
    let j = b.length - 1;
    
    // 뒤에서부터 하나씩 더함
    while (i >= 0 || j >= 0 || carry > 0) {
        let digitA = i >= 0 ? Number(a[i]) : 0;
        let digitB = j >= 0 ? Number(b[j]) : 0;

        let sum = digitA + digitB + carry;

        answer = (sum % 10) + answer; // 현재 자리 숫자
        carry = Math.floor(sum / 10); // 올림 처리

        i--;
        j--;
    }

    return answer;
    // return (BigInt(a) + BigInt(b)).toString();
}