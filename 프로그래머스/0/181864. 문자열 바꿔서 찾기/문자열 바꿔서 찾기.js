function solution(myString, pat) {
    var str = '';
    for(let i = 0; i<myString.length; i++){
        if (myString[i] == 'A'){
            str += 'B';
        } else {
            str += 'A';
        }
    }
    if (str.includes(pat)){
        return 1;
    } else {
        return 0;
    }
}