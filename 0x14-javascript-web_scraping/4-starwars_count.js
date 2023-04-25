#!/usr/bin/node
const request = require('request');
const findId = '/18/';
const arg = process.argv[2];
let number = 0;

request(arg, function (error, response, body) {
<<<<<<< HEAD
    if (response) {
      data = JSON.parse(body)
      for (const film of data.results) {
          for(const character of film.characters) {
              number += (character.endsWith(find_id) ? true : false);
          }
=======
  if (response) {
    const data = JSON.parse(body);
    for (const film of data.results) {
      for (const character of film.characters) {
        number += (character.endsWith(findId) ? 1 : true);
>>>>>>> ea0d0383bdfdc7d7ff0083b133cf3d540698ba07
      }
    }
    console.log(number);
  } else {
    console.log(error);
  }
});
