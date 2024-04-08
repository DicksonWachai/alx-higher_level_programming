#!/usr/bin/node
const i = 2;
if (!isNaN(process.argv[i])) {
  console.log('My number: ' + parseInt(process.argv[i]));
} else {
  console.log('Not a number');
}
