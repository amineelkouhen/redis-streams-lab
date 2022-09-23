<img src="../img/redis-logo-full-color-rgb.png" height=100/>

# Exercise 1 - Introduction to Redis
Hello and thank you for joining this hands-on lab! We're happy to have you join, so welcome! This first exercise aims to show you what core Redis is, how it can be interacted with and gives a tour of some of the available core data types. 

## Goals

* Learn some of the basic Redis commands by using the [Redis CLI](https://redis.io/topics/rediscli)
* Learn about some of the different [datastructures in Redis](https://redis.io/topics/data-types-intro)

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
* Let's see if we can store something in Redis and retrieve it again, so let's start simple and start with a basic String key/value pair.
* Add a String key/value pair to Redis with a key of `hello` and a value of `world`:
```
set hello world
```
* Retrieve the key/value pair from Redis
```
get hello
```
Congratulations, you are now a Redis veteran! Of course, `get` and `set` are not the only two commands available for dealing with Strings in Redis. You can find out about all of the other commands for Strings (and all the other datatypes) by visiting the [Redis documentation](https://redis.io/commands/#string)

Let's check out some of the other data structures in Redis as well. Let's start with a Hash. Hashes are typically used to store flat structures with multiple attributes, such as records or structs. A typical application would be to store an HTTP or user session in Redis so you can keep your own application stateless and add/remove instances/pods as needed while still being able to retrieve state from a logged in user. It's typically much faster and more efficient to store this in a solution that's optimised for fast memory access rather than a general purpose solution.
* Let's add a Hash with the key `myhash` and two key/value pairs within that Hash with keys `hello` and `how` and values `world` and `areyou?`:
```
hset myhash hello world how areyou?
```
* Retrieve the Hash and all its key/value pairs from Redis
```
hgetall myhash
```
* Retrieve a single key from the Hash
```
hget myhash hello
```
Did you notice that Redis has different commands for different data structures? For instance, a `get` command will not work on a hash, but it will work on all other data structures. And an `hget` will work on a hash but not on another data structure. If you try this you will get a 'WRONGTYPE' error. Don't know the type of a certain key? You can ask Redis the type of the `myhash` key by typing:
```
type myhash
```
and Redis will tell you that it's a hash. Alternatively, you can type:
```
type hello
```
To find out that this key is a String type. If you want to learn more about hashes then check out all the available commands at the [Redis Documentation](https://redis.io/commands#hash). You can use the drop down list on that [same page](https://redis.io/commands) to select a different data structure to find out what commands apply to that particular data structure.

### Sorted Sets
Now, let's take a look at a Sorted Set. A Sorted Set (as the name implies) is an ordered collection of unique values. In Redis each value will have a score associated with it, and by updating the score as we go along the Set will maintain its ordering according to the score. Think of scenarios like maintaining a high score leaderboard when playing a game, a list of 'biggest spenders' on your bank account or other scenarios where you need to update a ranking/score as more data becomes available in your application.

* We can add members to a Set directly by using the `zadd` command. There is no need to set a key first. So let's add three members to a Sorted Set using the following commands:
```
zadd mysortedset 2 "two"
zadd mysortedset 3 "three"
zadd mysortedset 1 "one"
```
* Notice how the order is off when adding the members to the set (we're adding the second one first, the third one second and the first one third). Let's get the first two members of the Sorted Set by typing:
```
zrange mysortedset 0 1
```
* Notice that this returns "one" and "two". We can also get the last two members of the Sorted Set by reversing the range:
```
zrange mysortedset 0 1 rev
```
This will produce the result "three" and "two". For more information on Sorted Sets and their assocatied commands, check the [Redis documentation](https://redis.io/commands#sorted_set).

Now that you have seen a few of the most commonly used Redis data structures in action, feel free to take a look at what other data types and command are available in the [Redis documentation](https://redis.io/topics/data-types)

## Next steps

Well done, you made it through the first exercise! Take a short break if you want, and then move on to [exercise 2](exercise-2-start.md).
