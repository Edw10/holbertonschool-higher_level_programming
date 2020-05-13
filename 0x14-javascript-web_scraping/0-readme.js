#!/usr/bin/node
// this script read a file

var fs = require('fs');

fs.readFile(process.argv[2], (err, data) => {
  if (err) throw err;
  console.log(data);
});
