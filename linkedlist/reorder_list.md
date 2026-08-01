# 📘 Linked List Revision Notes – Reorder List (My Doubts Explained)

## Problem

Given:

```
1 → 2 → 3 → 4 → 5
```

Convert it into:

```
1 → 5 → 2 → 4 → 3
```

Without creating a new linked list.

---

# Overall Strategy

Never try to solve the entire problem at once.

Think of it as **4 independent problems**.

```
Build List
     ↓
Find Middle
     ↓
Split
     ↓
Reverse Second Half
     ↓
Merge
```

If each step works individually, the final solution becomes easy.

---

# Doubt 1: Why do we need `head`?

`head` is the only pointer that remembers where the linked list starts.

```
head
 ↓
1 → 2 → 3 → 4
```

If you lose `head`, you cannot traverse the list from the beginning.

Think of `head` as the entrance to a building.

---

# Doubt 2: Why do we save `next_node` while reversing?

Wrong:

```python
current.next = prev
current = current.next
```

Why?

Because after

```
current.next = prev
```

the original next node is lost.

Example

Before

```
4 → 5
```

After

```
4 → None
```

Where did node 5 go?

You lost it.

Correct order:

```python
next_node = current.next
current.next = prev
prev = current
current = next_node
```

Golden Rule:

> **Save first, then overwrite.**

---

# Doubt 3: How does Slow & Fast find the middle?

Start

```
S
F

1 → 2 → 3 → 4 → 5
```

Iteration 1

```
    S
        F

1 → 2 → 3 → 4 → 5
```

Iteration 2

```
        S
                F

1 → 2 → 3 → 4 → 5
```

Fast reaches the end.

Slow stays at the middle.

Middle = 3

Remember

```
Slow moves 1 step.

Fast moves 2 steps.
```

---

# Doubt 4: How do I split a linked list?

Original

```
1 → 2 → 3 → 4 → 5
          ↑
        slow
```

Step 1

Save where the second half starts.

```python
second_head = slow.next
```

Now

```
second_head
      ↓
      4 → 5
```

Step 2

Cut the list.

```python
slow.next = None
```

Now

First list

```
1 → 2 → 3
```

Second list

```
4 → 5
```

Only ONE pointer changes.

---

# Doubt 5: Why does the reversed list start from `prev`?

Before reverse

```
4 → 5
```

After reverse

```
5 → 4
```

The variable

```
prev
```

points to

```
5
```

NOT

```
4
```

Always remember:

```
After reversing,

prev = New Head
```

Never print using the old head.

---

# Doubt 6: Why shouldn't I do

```python
head = prev
```

Suppose

```
head

1 → 2 → 3
```

```
prev

5 → 4
```

If you write

```python
head = prev
```

Now

```
head

5 → 4
```

You lost the first list.

Instead keep

```
master_head

1 → 2 → 3
```

and

```
prev

5 → 4
```

Use different variables.

---

# Doubt 7: Why doesn't merging use `current`?

During reverse,

```
current
```

visits every node.

So

```python
while current:
```

makes sense.

During merge,

you already have TWO lists.

```
First

1 → 2 → 3

Second

5 → 4
```

You need TWO pointers.

```
first_current

second_current
```

There is no generic `current`.

---

# Doubt 8: Why do we save `first_next` and `second_next`?

Suppose

```
1 → 2 → 3

5 → 4
```

If you connect

```
1 → 5
```

without saving

```
2
```

you lose where to continue.

So save

```python
first_next = first_current.next
second_next = second_current.next
```

THEN reconnect.

Exactly the same idea as reversing.

---

# Doubt 9: Merge Order

Never do

```
Move
↓

Connect
```

Always do

```
Save
↓

Connect
↓

Move
```

Every iteration:

```
Save

first_next
second_next

↓

Connect

1 → 5

↓

Connect

5 → 2

↓

Move

first_current = 2

second_current = 4
```

Repeat.

---

# The Final Merge Visualization

Initial

```
First

1 → 2 → 3

Second

5 → 4
```

Iteration 1

```
1 → 5 → 2 → 3
```

Iteration 2

```
1 → 5 → 2 → 4 → 3
```

Done.

---

# Biggest Lesson I Learned

Almost every linked list problem follows this pattern:

```
1. Save pointers

↓

2. Change pointers

↓

3. Move pointers
```

Never change a pointer before saving where it was pointing.

---

# My Linked List Cheat Sheet

## Reverse

```
Save

↓

Reverse

↓

Move
```

---

## Find Middle

```
Slow = 1 step

Fast = 2 steps
```

---

## Split

```
second_head = slow.next

slow.next = None
```

---

## Reverse Second Half

```
prev becomes the new head
```

---

## Merge

```
Save first_next

Save second_next

↓

first → second

↓

second → first_next

↓

Move both pointers

Repeat
```

---

# Golden Rules (Remember Forever)

✅ Never overwrite a pointer without saving its next node.

✅ `head` should continue pointing to the beginning of the original list.

✅ After reversing, `prev` becomes the new head.

✅ During merge, use **two current pointers**, not one.

✅ Every linked list problem can be solved by thinking:

```
Save

↓

Connect

↓

Move
```

If you remember just these three words, you'll be able to reconstruct most linked list algorithms during interviews without memorizing code.
