const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");

let number = Number(input[0]);

for (let i = 1; i <= number; i++) {
  console.log(i);
}
