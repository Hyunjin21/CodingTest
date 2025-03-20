function solution(a, b) {
    const str1 = String(a)+String(b);
    const str2 = String(b)+String(a);
    answer = str1 >= str2 ? Number(str1) : Number(str2);

    return answer;
}