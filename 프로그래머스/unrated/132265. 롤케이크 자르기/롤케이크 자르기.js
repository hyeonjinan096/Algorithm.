function solution(topping) {
  let answer = 0;

  const allTopping = new Map();
  const bro = new Map();

  topping.forEach((n) => {
    allTopping.set(n, (allTopping.get(n) || 0) + 1);
  });

  for (let n of topping) {

    allTopping.set(n, allTopping.get(n) - 1);

    bro.set(n, true);

    if (!allTopping.get(n)) allTopping.delete(n);


    if (allTopping.size === bro.size) answer++;

    if (allTopping.size < bro.size) break;
  }

  return answer;
}

console.log(solution([1, 2, 1, 3, 1, 4, 1, 2]));
console.log(solution([1, 2, 3, 1, 4])); 