#!/usr/bin/node
// this script write to a file

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }
});
