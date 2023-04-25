#!/usr/bin/node
// Anakin SkyWalker
// STAR WARS ! THE CLONE WARS
// I need a life, lol.
const request = require('request');
const id = process.argv[2];
const starWarsApi = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(starWarsApi, function (error, response, body) {
  if (response) {
    console.log(JSON.parse(body).title);
  } else {
    console.log(error);
  }
});
