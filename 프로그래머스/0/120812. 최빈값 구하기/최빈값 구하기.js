function solution(array) {
    let count = {};
    for(let num of array){
        count[num] = (count[num] || 0)+1; 
    }
    
    let maxCount = 0;
    let maxNumbers = [];
    for(let key in count){
        if(count[key] > maxCount){
            maxCount = count[key];
            maxNumbers = [Number(key)];
        } else if (count[key] == maxCount){
            maxNumbers.push(Number(key));
        }
    }
    return maxNumbers.length === 1 ? maxNumbers[0] : -1;
}