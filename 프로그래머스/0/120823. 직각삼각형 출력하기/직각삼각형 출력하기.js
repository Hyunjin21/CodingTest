const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    arr = input[0];
    for(let i=1; i<=arr; i++) {
        console.log('*'.repeat(i));
    }
});