#!/usr/bin/node
const integer = parseInt(process.argv[2]);
let stringX = '';
if (!integer) {
  console.log('Missing size');
}
for (let i = 0; i < integer; i++) {
  for(let j = 0; j < integer; j++) {
    stringX += 'X';
  }
  stringX += '\n';
}
console.log(stringX);
