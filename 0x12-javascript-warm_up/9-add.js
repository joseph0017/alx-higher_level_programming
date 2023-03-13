#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const args1 = process.argv[2];
const parameter1 = parseInt(args1);
const args2 = process.argv[3];
const parameter2 = parseInt(args2);
a = parameter1;
b = parameter2;
console.log(add(a, b));
