function solution(arr) {
    var answer = 0;
    while(true){
        var newArr = [];
        var changed = false;
        var next;
        
        for (let i = 0; i<arr.length; i++){
            if (arr[i]>=50 && arr[i]%2==0){
                next = arr[i]/2;
            } else if (arr[i]<50 && arr[i]%2!=0){
                next = arr[i]*2+1;
            } else {
                next = arr[i];
            }
            newArr[i] = next;
            if (next !== arr[i]){
                changed = true;
            }
        }
        if (!changed){
            break;
        } 
        for (let j = 0; j<arr.length; j++){
            arr[j] = newArr[j];
        }
        answer += 1;
    }
    return answer;
}