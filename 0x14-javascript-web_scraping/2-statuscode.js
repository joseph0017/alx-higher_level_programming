#!/usr/bin/node
const request = require('request')
arg = procsess.argv[2]

request(arg, function (error, response, body) {
  if (response) {
    console.log('code:', response.statusCode);
  } else {
    console.log(error);
  }
});