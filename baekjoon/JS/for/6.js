const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");

let number = Number(input[0]);

for (let i = number; i > 0; i--) {
  console.log(i);
}
