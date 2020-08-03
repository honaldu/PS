const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");
const n = input.filter((v) => v).map((v) => v.split(" ").map((v) => Number(v)));

for (let i = 1; i < n.length; i++) {
  console.log(`Case #${i}: ${n[i][0]} + ${n[i][1]} = ${n[i][0] + n[i][1]}`);
}
