function solution(num, k) {
    let str = String(num).split('');
    if(str.includes(String(k))){
        return str.indexOf(String(k)) + 1;
    } else {
        return -1;
    }
}