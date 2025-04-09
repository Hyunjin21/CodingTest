function solution(binomial) {
    var cal = binomial.split(' ');
    var [a, op, b] = cal;
    switch(op){
        case '+':
            return Number(a)+Number(b);
            break;
        case '-':
            return Number(a)-Number(b);
            break;
        case '*':
            return Number(a)*Number(b);
            break;
    }
}