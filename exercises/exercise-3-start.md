<img src="../img/redis-logo-full-color-rgb.png" height=100/>

# Exercise 3 - Managing Stream Length

While Redis Streams can grow indefinitely when they are left unchecked, it's possible to cap a stream's length to an exact or approximate number either by:
1- A producer, when it adds an entry to the stream with XADD
2- Invoking the XTRIM command at any point.
Both approaches remove the oldest entries from a stream.

* Add to stream `new-hires` and includes the fields name and start-date for yourself
```
XADD new-hires * name Amine start-date 2022-05-16
```
Rerun this command a few times (let's say 10 times)

* Get the total number of elements (length) in the stream
```
XLEN new-hires
```

* Add to stream `new-hires` but this time limit the number of entries to 20 and then check for length
```
XADD new-hires MAXLEN 20 * name Skipper start-date 2020-02-01
XLEN new-hires
```
What do you observe ?

* Now, let's TRIM the stream `new-hires` down to approximately 10 entries
```
XTRIM new-hires MAXLEN ~ 10
XLEN new-hires
```

How many entries does the stream have?
* Do you need more details about the stream ? Get info with:
```
XINFO STREAM new-hires
```

## Next steps

Well done, you made it through the third exercise! You can move on to [exercise 4](exercise-4-start.md) directly.
