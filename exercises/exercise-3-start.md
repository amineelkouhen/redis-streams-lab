<img src="../img/redis-logo-full-color-rgb.png" height=100/>

# Exercise 3 - Managing Stream Length

While Redis Streams can grow indefinitely when they are left unchecked, it's possible to cap a stream's length to an exact or approximate number either by:
1. A producer, when it adds an entry to the stream with XADD
2. Invoking the XTRIM command at any point.
Both approaches remove the oldest entries from a stream.

* Add to stream `new-hires` and includes the fields name and start-date for yourself
```
XADD new-hires * name Amine start-date 2022-05-16
```

* Add a few more new-hires:

```
XADD new-hires * name François start-date 2017-02-08
XADD new-hires * name Pierre start-date 2022-12-12
XADD new-hires * name Yacine start-date 2022-12-05
XADD new-hires * name Kamran start-date 2019-09-02
XADD new-hires * name Alexandre start-date 2021-02-15
XADD new-hires * name Luigi start-date 2021-07-01
XADD new-hires * name Virgilio start-date 2022-10-10
XADD new-hires * name Ruurd start-date 2022-03-14
XADD new-hires * name Hannu start-date 2022-11-09

XADD new-hires * name Greg start-date 2021-03-15
XADD new-hires * name Allen start-date 2018-02-05
XADD new-hires * name Tal start-date 2015-11-15
XADD new-hires * name Julien start-date 2018-04-15
XADD new-hires * name Marie start-date 2021-12-06
XADD new-hires * name Raul start-date 2022-06-13
XADD new-hires * name Alberto start-date 2021-09-01
XADD new-hires * name Markus start-date 2017-04-10
```

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
