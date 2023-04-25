#!/usr/bin/node
// Anakin SkyWalker
// STAR WARS ! THE CLONE WARS
// I need a life, lol.
const request = require('request');
const id = process.argv[2];
const starWarsApi = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(starWarsApi, function (error, response, body) {
  if (response) {
    const getResults = JSON.parse(body);
    getResults.characters.forEach((results) => {
        //console.log(results)
        request(results, function(err, res, body2) {
            if (res) {
            const characters_name = JSON.parse(body2)
            console.log(characters_name.name)
        }
        })
    })    
  } else {
    console.log(error);
  }
});
