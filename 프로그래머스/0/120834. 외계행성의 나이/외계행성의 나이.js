function solution(age) {
    const ageProgram = ['a','b','c','d','e','f','g','h','i','j'];
    return String(age)
        .split('')
        .map(index => ageProgram[parseInt(index)])
        .join('');
    
    // var answer = '';
    // const ageProgram = ['a','b','c','d','e','f','g','h','i','j'];
    // const strAge = String(age);
    // for(let i=0; i<strAge.length; i++){
    //     const index = parseInt(strAge[i]);
    //     answer += ageProgram[index];
    // }
    // return answer;
}