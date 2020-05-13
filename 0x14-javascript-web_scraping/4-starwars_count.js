#!/usr/bin/node
// this script return the count of a character in the starwars movies

const request = require('request');
let co = 0;

request(process.argv[2], (err, res, bd) => {
  if (err) return err;
  for (const i in JSON.parse(bd).results) {
    for (const character of JSON.parse(bd).results[i].characters) {
      if (character.includes('18')) co++;
    }
  }
  console.log(co);
});
