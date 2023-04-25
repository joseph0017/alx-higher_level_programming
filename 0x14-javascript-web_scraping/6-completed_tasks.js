#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (response) {
    const getResults = JSON.parse(body);
    const userTaskCompleted = {};
    getResults.forEach((result) => {
      if (result.completed === true) {
        if (result.userId in userTaskCompleted) {
          userTaskCompleted[result.userId] += 1;
        } else {
          userTaskCompleted[result.userId] = 1;
        }
      }
    });
    console.log(userTaskCompleted);
  } else {
    console.log(error);
  }
});
