#!/usr/bin/node
// Anakin SkyWalker
// STAR WARS ! THE CLONE WARS
// I need a life, lol.
const request = require('request')
star_wars_id = process.argv[2]
star_wars_api = `https://swapi-api.alx-tools.com/api/films/${star_wars_id}`

request(star_wars_api, function (error, response, body) {
  if (response) {
    console.log(JSON.parse(body).title);
  } else {
    console.log(error);
  }
});
