#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const argsOne = process.argv[2]
const parameterOne = parseInt(argsOne);
const argsTwo = process.argv[3]
const parameterTwo = parseInt(argsTwo);
a = parameterOne
b = parameterTwo
console.log(add(a, b));
