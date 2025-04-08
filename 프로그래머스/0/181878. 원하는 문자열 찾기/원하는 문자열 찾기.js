function solution(myString, pat) {
    myString = myString.toUpperCase();
    pat = pat.toUpperCase();
    
    if (myString.includes(pat)){
        return 1;
    } else {
        return 0;
    }
}