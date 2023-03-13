#!/usr/bin/node

function factorial(x) {

    // if number is 0
    if (x == 0 || isNaN(x)) {
        return 1;
    }

    // if number is positive
    else {
        return x * factorial(x - 1);
    };
};

const args = process.argv[2];
const x = parseInt(args);

console.log(factorial(x));