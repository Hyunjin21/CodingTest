function solution(arr, n) {
    var len = arr.length;
    if(len%2 != 0){
        for(let i = 0; i<len; i+=2){
            arr[i] = arr[i] + n;
        } 
    } else {
        for(let i = 1; i<len; i+=2){
            arr[i] = arr[i] + n;
        }
    }
    return arr;
}