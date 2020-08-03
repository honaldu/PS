const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const a = input[0];
const b = input[1];

for (i = b.length - 1; i >= 0; i--) {
  console.log(a * b[i]);
}
console.log(a * b);
