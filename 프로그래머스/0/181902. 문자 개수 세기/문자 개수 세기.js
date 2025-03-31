function solution(my_string) {
    const answer = Array(52).fill(0);
    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
    for (let i = 0; i < my_string.length; i++) {
        const letter = alphabet.indexOf(my_string[i]);
        if (letter !== -1) {
            answer[letter] += 1;
        }
    }
    return answer;
}