'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function (inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function () {
    inputString = inputString.split('\n');
    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the countTriplets function below.
function countTriplets(arr, r) {
    let seconds = {};
    let thirds = {};

    let count = 0;
    for (let j = 0; j < arr.length; j++) {
        let i = arr[j];
        count += (thirds[i] ? thirds[i] : 0);
        if (thirds[i * r]) {
            thirds[i * r] += seconds[i] ? seconds[i] : 0;
        } else {
            thirds[i * r] = seconds[i] ? seconds[i] : 0;
        }
        seconds[i * r] = seconds[i * r] ? seconds[i * r] + 1 : 1;
    }

    return count;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const nr = readLine().replace(/\s+$/g, '').split(' ');

    const n = parseInt(nr[0], 10);

    const r = parseInt(nr[1], 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    const ans = countTriplets(arr, r);

    ws.write(ans + '\n');

    ws.end();
}
