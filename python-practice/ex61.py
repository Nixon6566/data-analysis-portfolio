'''FIZZ BUZZ
The problem is simple. Print out every number between 1 and 100, one
number per line, but if the number is divisible by three, print out "Fizz";
if the number is divisible by five, print out "Buzz"; and if the number is
divisible by both three AND five, print out FIZZ BUZZ.
Now we need to break it down further and check to see if x is divisible
by JUST 3 or JUST 5. Sounds like a job for Elif. '''

for x in range(1, 101):
	if x % 3 == 0 and x % 5 == 0:
		print (f"{x} FIZZ BUZZ!")
	elif x % 3 == 0:
		print (f"{x} FIZZ")
	elif x % 5 == 0:
		print (f"{x} BUZZ")
	else:
		print (x)

'''**Short answer:** Use **string concatenation** or a **generator + `join` one-liner** to make the code much shorter while keeping it readable. Below are 4 compact options, with pros/cons and recommended choice for clarity and extensibility.

### Quick guide — what to consider
- **Readability vs terseness**: shorter code can be clever but harder to maintain.  
- **Extensibility**: if you may add more rules (e.g., 7 → "Bazz"), prefer a mapping-based approach.  
- **Performance**: all options are \(O(n)\); differences are negligible for 1–100.

---

### Compact implementations

#### 1. String concatenation (clear and short)
```python
for i in range(1, 101):
    s = ('Fizz' if i % 3 == 0 else '') + ('Buzz' if i % 5 == 0 else '')
    print(f"{i} {s}" if s else i)
```

#### 2. Build string then fallback (very readable)
```python
for i in range(1, 101):
    out = ''
    if i % 3 == 0: out += 'Fizz'
    if i % 5 == 0: out += 'Buzz'
    print(f"{i} {out}" if out else i)
```

#### 3. One-liner using generator + join (most concise)
```python
print('\n'.join((f"{i} " + ('Fizz'*(i%3==0) + 'Buzz'*(i%5==0)) or str(i)) for i in range(1,101)))
```

#### 4. Mapping approach for easy extension
```python
m = {3: 'Fizz', 5: 'Buzz'}
for i in range(1, 101):
    s = ''.join(v for k, v in m.items() if i % k == 0)
    print(f"{i} {s}" if s else i)
```

---

### Comparison table

| **Method** | **Lines** | **Readability** | **Extensible** |
|---|---:|---:|---:|
| If/elif (original) | 6–8 | High | Low |
| String concatenation | 3–4 | High | Medium |
| One-liner join | 1 | Low | Low |
| Mapping dict | 3–5 | Medium | High |

> Sources: .

---

### Recommendation and trade-offs
- **Best balance:** **string concatenation** (option 1 or 2). It’s short, easy to read, and avoids special tricks while still producing `FizzBuzz` and `Fizz`/`Buzz` combinations without extra `and` checks.  
- **If you want the shortest code:** use the **one-liner** (option 3). It’s compact but less readable for others and slightly trickier to debug.  
- **If you plan to add rules:** use the **mapping approach** (option 4); adding a new divisor is a one-line change and the loop logic stays the same.

---

### Final tip
**Order matters** only in the `if/elif` style; using concatenation or mapping naturally produces `"FizzBuzz"` for multiples of both without special-case checks, which simplifies logic and reduces code duplication.
 '''