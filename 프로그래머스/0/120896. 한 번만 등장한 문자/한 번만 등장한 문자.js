function solution(s) {
    let answer = [];
    let str = s.split('');
    str.forEach((item) => {
        if(str.indexOf(item) === str.lastIndexOf(item)){
            answer.push(item);
        }
    })
    return answer.sort().join('');
}