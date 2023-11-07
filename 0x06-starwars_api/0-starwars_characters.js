#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

function getCharacterName (url) {
  return new Promise((resolve) => {
    request(url, function (error, response, body) {
      if (!error && response.statusCode === 200) {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

request(url, async function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);

    for (const character of data.characters) {
      const name = await getCharacterName(character);
      console.log(name);
    }
  }
});
