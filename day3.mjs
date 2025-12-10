import { readFile } from "node:fs/promises";
const inp = await readFile("inputs/day3.txt", "utf-8");
const INPUT = inp.split("\n");

function partone() {
  let totalVoltage = 0;
  let lines = INPUT.map((n) => n.trim());
  lines.forEach((line) => {
    let nums = new Array();
    for (let i = 0; i < line.length; i++) {
      var num = line[i];
      for (let j = i + 1; j < line.length; j++) {
        var num2 = line[j];
        nums.push(Number(num + num2));
      }
    }
    totalVoltage += Math.max(...nums);
  });
  console.log(totalVoltage);
}

partone();
