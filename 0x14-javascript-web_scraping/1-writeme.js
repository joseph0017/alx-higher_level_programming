#!/usr/bin/node
const fs = require('fs');
const data = process.argv[3];
const url = process.argv[2];

fs.writeFile(url, data, (err) => {
  if (data) {
    console.log(data);
  } else {
    console.log(err);
  }
});
