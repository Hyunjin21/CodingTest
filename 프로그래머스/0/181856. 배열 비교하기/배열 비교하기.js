function solution(arr1, arr2) {
    var len1 = arr1.length;
    var len2 = arr2.length;
    if(len1 !== len2){
        return len1>len2 ? 1:-1;
    } else {
        var sum1 = arr1.reduce((a,b)=>a+b);
        var sum2 = arr2.reduce((a,b)=>a+b);
        if (sum1 > sum2) return 1;
        else if (sum1 == sum2) return 0;
        else return -1;
    }
}