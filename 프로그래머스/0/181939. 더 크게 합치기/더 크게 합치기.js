function solution(a, b) {
    var str1 = String(a)+String(b);
    var str2 = String(b)+String(a);
    var answer = str1 >= str2 ? Number(str1) : Number(str2);

    return answer;
}