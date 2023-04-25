#!/usr/bin/node
const request = require('request');
const find_id = '/18/';
arg = process.argv[2]
let number = 0;

request(arg, function (error, response, body) {
    if (response) {
      data = JSON.parse(body)
      for (const film of data.results) {
          for(const character of film.characters) {
              number += (character.endsWith(find_id) ? true : false);
          }
      }
      console.log(number)
    } else {
      console.log(error);
    }
  });