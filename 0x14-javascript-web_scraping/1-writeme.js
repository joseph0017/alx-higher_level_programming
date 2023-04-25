#!/usr/bin/node
const fs = require('fs');
const data = process.argv[3];
fs.writeFile(process.argv[2], data, (err) => {
  if (data) {
    console.log(data);
  } else {
    console.log(err);
  }
});
