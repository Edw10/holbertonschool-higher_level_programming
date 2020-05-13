#!/usr/bin/node
// this script return the completed tasks

const request = require('request');
const rest = Object();

request(process.argv[2], (err, res, bd) => {
  if (err) return err;
  for (const i in JSON.parse(bd)) {
    if (JSON.parse(bd)[i].completed) {
      const id = JSON.parse(bd)[i].userId;
      if (rest.hasOwnProperty(id)) {
        rest[id] += 1;
      } else {
        rest[id] = 1;
      }
    }
  }
  console.log(rest);
});
