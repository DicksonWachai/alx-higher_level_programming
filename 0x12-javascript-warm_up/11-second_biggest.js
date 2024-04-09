#!/usr/bin/node
let max = 0;
let secondMax = 0;
if (process.argv.length < 3) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] > max) {
      secondMax = max;
      max = process.argv[i];
    } else if (process.argv[i] > secondMax && process.argv[i] < max) {
      secondMax = process.argv[i];
    }
  }
  console.log(secondMax);
}
