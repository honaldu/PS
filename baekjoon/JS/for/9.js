const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");

let number = Number(input[0]);

for (i = 1; i < number + 1; i++) {
  console.log(`${"*".repeat(i)}`);
}
