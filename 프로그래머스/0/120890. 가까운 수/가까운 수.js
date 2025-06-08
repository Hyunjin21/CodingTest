function solution(array, n) {
    let new_arr = [];
    array.sort((a, b) => a - b);
    for(let i=0; i<array.length; i++){
        new_arr.push(Math.abs(array[i]-n))
    }
    let idx = new_arr.indexOf(Math.min(...new_arr));
    return array[idx];
}