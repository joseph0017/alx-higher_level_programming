#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const args_1 = process.argv[2];
const parameter_1 = parseInt(args_1);
const args_2 = process.argv[3];
const parameter_2 = parseInt(args_2);
a = parameter_1;
b = parameter_2;
console.log(add(a, b));
