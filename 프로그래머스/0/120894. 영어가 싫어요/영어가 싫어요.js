function solution(numbers) {
    let numStr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    numStr.forEach((str, i) => {
        numbers = numbers.replaceAll(str, i);
    })
    return Number(numbers);
}