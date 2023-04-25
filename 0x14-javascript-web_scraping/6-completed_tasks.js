#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
    if (response) {
      const get_results = JSON.parse(body)
      const userTaskCompleted = {};
      get_results.map((result) => {
          if (result.completed == true) {
              if (result.userId in userTaskCompleted) {
                  userTaskCompleted[result.userId] += 1;
              }
              else {
                  userTaskCompleted[result.userId] = 1;
              }
          }
      })
      console.log(userTaskCompleted);
    } else {
      console.log(error);
    }
  });
  