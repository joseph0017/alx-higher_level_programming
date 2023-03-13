#!/usr/bin/node
const parameter = process.argv[2];
if(parameter){
  console.log(`${parameter}`);
} else {
  console.log("No argument");
}