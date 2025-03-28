function solution(my_string, queries) {
    for (let i=0; i<queries.length; i++){
        const [start,end] = queries[i];
        var arr = my_string.slice(start, end+1);
        var before = my_string.slice(0,start);
        var after = my_string.slice(end+1, my_string.length);
        my_string = before + arr.split('').reverse().join('') + after;
    }
    return my_string;
}