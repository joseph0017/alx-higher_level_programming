#!/usr/bin/node
const request = require('request');
const findId = '/18/';
const arg = process.argv[2];
let number = 0;

request(arg, function (error, response, body) {
  if (response) {
    const data = JSON.parse(body);
    for (const film of data.results) {
      for (const character of film.characters) {
        number += (character.endsWith(findId) ? true : 0);
      }
    }
    console.log(number);
  } else {
    console.log(error);
  }
});
