#!/usr/bin/node
function factorial (x) {
  if (x == 0 || isNaN(x)) {
      return 1;
  } else {
      return x * factorial(x - 1);
  }
}
let args = process.argv[2];
const x = parseInt(args);
console.log(factorial(x));
