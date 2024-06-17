#!/usr/bin/node
if (process.argv.length === 3) {
  const x = parseInt(process.argv[2]);
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
