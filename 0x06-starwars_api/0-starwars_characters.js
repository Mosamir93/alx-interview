#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, async (error, res, body) => {
  if (error) {
    console.log('Error fetching data:', error);
    return;
  }

  const film = JSON.parse(body);

  const fetchCharacterName = (characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, res, body) => {
        if (error) {
          reject(new Error('Error fetching character data'));
          return;
        }
        const character = JSON.parse(body);
        resolve(character.name);
      });
    });
  };

  const characterNames = await Promise.all(
    film.characters.map((characterUrl) => fetchCharacterName(characterUrl))
  );

  characterNames.forEach((name) => console.log(name));
});
