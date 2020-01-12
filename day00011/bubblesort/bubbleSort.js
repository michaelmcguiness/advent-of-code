'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function () {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the countSwaps function below.
function countSwaps(a) {
    let totalSwaps = 0;
    let swaps = 1;
    while (swaps != 0) {
        swaps = 0;
        for (let i = 0, n = a.length - 1; i < n; i++) {
            if (a[i] > a[i + 1]) {
                let tmp = a[i];
                a[i] = a[i + 1];
                a[i + 1] = tmp;
                swaps++;
                totalSwaps++;
            }
        }
    }
    console.log(`Array is sorted in ${totalSwaps} swaps.`);
    console.log(`First Element: ${a[0]}`);
    console.log(`Last Element: ${a[a.length - 1]}`);
}

function main() {
    const n = parseInt(readLine(), 10);

    const a = readLine().split(' ').map(aTemp => parseInt(aTemp, 10));

    countSwaps(a);
}
