function solution(numbers) {
    let array = numbers.sort((a, b) => a-b);
    let num1 = array[0]*array[1];
    let num2 = array[array.length-1]*array[array.length-2];
    return num1 >= num2 ? num1 : num2;
}