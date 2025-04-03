function solution(num_list, n) {
    var answer = [];
    var after = num_list.slice(n);
    var before = num_list.slice(0, n);
    answer.push(after);
    answer.push(before);
    return answer.flat();
}