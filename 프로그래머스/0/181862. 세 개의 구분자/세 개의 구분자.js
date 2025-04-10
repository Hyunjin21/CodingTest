function solution(myStr) {
    var answer = myStr.split(/[abc]/).filter(Boolean);
    return answer.length === 0 ? ["EMPTY"] : answer;
}