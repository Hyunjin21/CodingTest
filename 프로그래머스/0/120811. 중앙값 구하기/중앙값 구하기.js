function solution(array) {
    var answer = 0;
    const mid_index = Math.floor(array.length/2);
    const new_array = array.sort((a,b) => a-b);
    answer = new_array[mid_index];
    return answer;
}