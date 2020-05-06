#!/usr/bin/node
// print multilenguages

const argv = process.argv.slice(2);

if (argv[0] === undefined) {
  console.log('No argument');
} else {
  argv.forEach(val => {
    console.log(val);
  });
}
