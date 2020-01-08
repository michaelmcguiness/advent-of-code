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

function createDictObj(arrOfWords) {
    let obj = {};
    for (let i = 0; i < arrOfWords.length; i++) {
        if (obj[arrOfWords[i]]) {
            obj[arrOfWords[i]] += 1;
        } else {
            obj[arrOfWords[i]] = 1;
        }
    }
    return obj;
}

// Complete the checkMagazine function below.
function checkMagazine(magazine, note) {
    let m = createDictObj(magazine);
    let n = createDictObj(note);

    for (let w in n) {
        if (m[w] < n[w] || !m[w]) {
            console.log("No");
            return;
        }
    }
    console.log("Yes");
}

function main() {
    const mn = readLine().split(' ');

    const m = parseInt(mn[0], 10);

    const n = parseInt(mn[1], 10);

    const magazine = readLine().split(' ');

    const note = readLine().split(' ');

    checkMagazine(magazine, note);
}
