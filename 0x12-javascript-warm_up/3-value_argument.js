#!/usr/bin/node
const i = 2;
if (process.argv[i]) {
  console.log(process.argv[i]);
} else {
  console.log('No argument');
}
