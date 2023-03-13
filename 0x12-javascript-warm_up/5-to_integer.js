#!/usr/bin/node
const integer = parseInt(process.argv[2]);
if (integer) {
  console.log(`${integer}`);
} else if (isNaN(integer)) {
  console.log('Not a number');
};
