#!/usr/bin/node
const initialArray = require('./100-data').list;
const newArray = initialArray.map((item, index) => item * index);
console.log(initialArray);
console.log(newArray);
