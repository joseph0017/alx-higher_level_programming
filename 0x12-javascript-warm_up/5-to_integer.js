#!/usr/bin/node
const parameter = process.argv[2]
const integer = parseInt(parameter)

if (integer) {
    console.log(`${integer}`)
}
else if(isNaN(integer)) {
    console.log("Not a number")
}
