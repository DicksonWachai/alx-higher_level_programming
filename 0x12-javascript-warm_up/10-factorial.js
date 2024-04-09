#!/usr/bin/node
function factorial (a) {
  if (isNaN(a)) {
    return 1;
  } else if (a <= 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
console.log(factorial(Number(process.argv[2])));
