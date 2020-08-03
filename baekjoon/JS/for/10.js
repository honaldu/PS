const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");

const number = Number(input[0]);

for (i = 1; i < number + 1; i++) {
  console.log(`${" ".repeat(number - i)}${"*".repeat(i)}`);
}
