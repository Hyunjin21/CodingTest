function solution(my_string) {
    var answer = 0;
    let str = my_string.split(' ');
    answer = Number(str[0]);
    for(let i = 1; i<str.length; i++){
        if(str[i] == '+'){
            answer += Number(str[i+1]);
        } else if(str[i] == '-'){
            answer -= Number(str[i+1]);
        } 
    }
    return answer;
}