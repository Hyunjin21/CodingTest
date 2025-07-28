function solution(my_string) {
    return my_string.split(/[a-zA-Z]/g)
    .map(Number)
    .reduce((a, b) => {
        return (a += b)
    });
}