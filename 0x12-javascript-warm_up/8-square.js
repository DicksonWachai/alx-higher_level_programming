#!/usr/bin/node
const arg = Number(process.argv[2]);
if (!isNaN(arg)) {
  for (let i = 0; i < arg; i++) {
    let row = '';
    for (let j = 0; j < arg; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
