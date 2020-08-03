const number = Number(prompt());

for (i = 1; i <= number; i++) {
  for (let j = number - i; j > 0; j--) {
    document.write("$");
  }
  for (j = 1; j <= i; j++) {
    document.write("*");
  }
  document.write("\n");
}
