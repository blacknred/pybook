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





Python vs JS


- both are scripting
- multyparadigm:
	py: OOP, functional, imperative, procedural
	js: OOP, functional, imperative
- typing
	py: strongly typed – no implicit conversion between types
	js: weakly typed
- repl (read-eval-print-loop):
	py: inbuild(v 2.7, v3)
	js: inbuild for nodejs and no for browser
- mutability:
	py: has mutable(set) and immutable(list) data types
	js: has no concept of mutable/immutable
- strings:
	py: ascii by default
	js: utf-16 by default, no built-in support for raw bites manipulating
- numbers:
	py: int, float, decimal etc
	js: int float
- hash tables:
	py: dictionaries, sets, etc
	js: has no build-in support
- inheritance:
	py: class-based
	js: prototype-based
- code blocks:
	py: uses indentation
	js: uses curly brackets
- function arguments:
	py: will raise an exception if a function is called with incorrect params
	js: any missing params get an undefined value thus no exceptions
- data types:
	py: list(similar to js array) and tuple(similar to list) 
	js: array, Map, Set
- properties and attributes:
	py: by setter & getter
	js: directly define an object property
- modules:
	py: wide range of modules by default (standard library)
	js: limited: Date, Math, JSON, Regexp etc
- multytasking:
	py: ?
	js: not support, async

- Also: ---------------------------------------------------------
- JS has; as statement terminator whereas Py has a newline.
- Py is a better-designed language whereas JS is poor.
- Py is not good for mobile development whereas JS is good.
- Py is slow to run comparatively to JS.
- Py heavily relies on assignment with no difference between variable and assignment whereas JS doesn’t relay.
- JS is more complex modern programming language comparatively to python.
- Py and JS both use a lexical scope with small differences.
- Py has a Self-argument as the first argument for each method whereas JS has accessed the object using “this”.
- Unlike JS, Py does not have a way to inherit from instances.

- Cases:--------------------------------------------------------
py: data analytics, machine learning or math-intensive operations
js: building a website or native applications as it took less time for UI work
