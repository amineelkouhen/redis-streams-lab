<img src="../img/redis-logo-full-color-rgb.png" height=100/>

# Exercise 3 - Managing Stream Length

While Redis Streams can grow indefinitely when they are left unchecked, it's possible to cap a stream's length to an exact or approximate number either by:
- A producer, when it adds an entry to the stream with XADD
- Invoking the XTRIM command at any point.
Both approaches remove the oldest entries from a stream.

* Add to stream `new-hires` and includes the fields name and start-date for yourself
```
XADD new-hires * name Amine start-date 2022-05-16
```

Rerun this command a few times (let's say 30 times)






## Next steps

Well done, you made it through the third exercise! You can move on to [exercise 4](exercise-4-start.md) directly.
