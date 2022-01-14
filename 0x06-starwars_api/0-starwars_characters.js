#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  function (error, response, body) {
    if (error !== null) {
      const characters = JSON.parse(response.body).characters;
      characters.forEach(element => {
        request(element, function (error, res, body) {
          if (error !== null) {
            const nameChar = JSON.parse(res.body).name;
            console.log(nameChar);
          }
          else {
              console.log("name not fetched")
          }
        });
      });
    }
    else {
        console.log("not here")
    }
  });
