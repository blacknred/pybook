# ES6+ from PY

## One-liners

```js
const x = a => a + 10;
```

```py
x = lambda a : a + 10
```

## Rest

```js
const [first, ...others] = [1, 2, 3, 4, 5];
```

```py
first, *others = [1, 2, 3, 4, 5]
```

## Spread

```js
const numbers = [1, 2, 3, 4, 5];
const sumOfNumbers = fun(...numbers);
```

```py
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = fun(*numbers)
```

## Copy

```js
const numbers = [1, 2, 3, 4, 5];
const copiedNumbers = [...numbers];
```

```py
numbers = [1, 2, 3, 4, 5]
copied_numbers = [*numbers]
```

## Destructing Assignment

```js
[a, b] = [b, a];
```

```py
a, b = b, a
```

## String literals

```js
console.log(`Hello, ${name}. You are ${age}`);
```

```py
print(f’Hello, {name}. You are {age}.’)
```

## Importing modules

```js
import package from "module-name";
```

```py
from module-name import some_element
```

## Set data type

```js
const mySet = new Set([1, 2, 3, 4, 5]);
```

```py
my_set = set([1, 2, 3, 4, 5])
```

## Generator functions

```js
function* generatorLoop(num) {
  for (let i = 0; i < num; i += 1) {
    yield i;
  }
}
```

```py
def generator_loop(num):
    for i in range(num):
        yield i
```

## Array comprehensions

```js
// Note: This JavaScript feature is obsolete.
// It was initially in the ECMAScript 2015 draft, but got removed.

const numbers = [1, 2, 3, 4, 5];
const doubled = [for (i of numbers) if (i > 1) i * 2];
```

```py
numbers = [1, 2, 3, 4, 5]
doubled = [i * 2 for i in numbers if i > 1]
```
