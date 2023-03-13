#!/usr/bin/node
const args = process.argv[2];

let i = 0

if (!args) {
    console.log('Missing number of occurrences');
}
for (i; i < args; i++) {
    console.log('C is fun');
}
