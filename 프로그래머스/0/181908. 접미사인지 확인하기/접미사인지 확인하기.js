function solution(my_string, is_suffix) {
    var arr = [];
    for(let i = 0; i < my_string.length; i++){
        arr.push(my_string.slice(i));
    }
    return arr.includes(is_suffix) === true ? 1 : 0;
}