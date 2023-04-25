#!/usr/bin/node
const request = require('request')
arg = process.argv[2]

request(arg, function (error, response, body) {
  if (response) {
    console.log('code:', response.statusCode);
  } else {
    console.log(error);
  }
});