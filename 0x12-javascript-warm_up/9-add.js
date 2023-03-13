#!/usr/bin/node
function add (a, b) {
  return a + b;
}
let argsOne = process.argv[2];
let parameterOne = parseInt(argsOne);
let argsTwo = process.argv[3];
let parameterTwo = parseInt(argsTwo);
a = parameterOne;
b = parameterTwo;
console.log(add(a, b));
