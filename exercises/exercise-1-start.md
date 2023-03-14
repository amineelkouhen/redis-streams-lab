<img src="../img/redis-logo-full-color-rgb.png" height=100/>

# Exercise 1 - Introduction to Redis
Hello and thank you for joining this hands-on lab! We're happy to have you join, so welcome! This first exercise aims to show you what is Redis Streams, how one can create and read events using it. 

## Goals

* Learn some of the basic Redis Streams commands by using the [Redis CLI](https://redis.io/topics/rediscli)

## Exercise
### Starting Redis and opening the CLI
* Open a terminal Window and start a Redis by using the following command:
```
docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```
* In a second terminal Window, open the Redis CLI (from the Docker image) by typing:
```
docker exec -it redis-stack redis-cli
```

By default, the Redis CLI will connect to 127.0.0.1 and port 6379. If you want to use a different hostname and port, you can use the `-h` and `-p` options to specify a diferent hostname and port.

### Strings and hashes
* Let's see if we can store something in Redis Streams and retrieve it again, so let's start simple and start with adding to a stream called `new-hires` and includes the fields name and start-date for yourself.

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
```

* Retrieve the entire stream starting from first entry

```
XREAD STREAMS new-hires 0
```

* You can read only the first two element of the stream
```
XREAD COUNT 2 STREAMS new-hires 0-0
```

* Get the elements using XRANGE from oldest to newest
```
XRANGE new-hires - +
XRANGE new-hires - + COUNT 2
```

* Get the elements using XREVRANGE from newest to oldest
```
XRANGE new-hires - +
XRANGE new-hires - + COUNT 2
```

Congratulations, you are now a Redis veteran! Of course, these are not the only two commands available for dealing with Streams in Redis. You can find out about all of the other commands for Streams (and all the other datatypes) by visiting the [Redis documentation](https://redis.io/commands/?group=stream)

## Next steps

Well done, you made it through the first exercise! Take a short break if you want, and then move on to [exercise 2](exercise-2-start.md).
