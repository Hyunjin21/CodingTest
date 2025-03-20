function solution(a, b) {
    var answer = 0;
    var str1 = String(a)+String(b);
    var str2 = 2 * a * b;
    answer = str1 >= str2 ? Number(str1) : Number(str2);
    return answer;
}