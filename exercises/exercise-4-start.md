<img src="../img/redis-logo-full-color-rgb.png" height=100/>

# Exercise 4 - Streams Consumer Groups

In the previous exercise, we saw that streams can be consumed by a single process using XREAD. For scalability reasons and to avoid bottlenecks, you can be pushed to consume Streams using consumer groups. In this exercise, we'll dive into this way of Streams consumption and see how to deal with the challenges that come with.

* Create a new stream and a consumer group with the MKSTREAM option
```
XGROUP CREATE jobs worker-group $ MKSTREAM
```

* Add a few jobs to the stream
```
XADD jobs 1-0 name job-1
XADD jobs 2-0 name job-2
XADD jobs 3-0 name job-3
XADD jobs 4-0 name job-4
```

* Create two consumers and have each read two elements of the stream
```
XREADGROUP GROUP worker-group worker-1 COUNT 2 STREAMS jobs >
XREADGROUP GROUP worker-group worker-2 COUNT 2 STREAMS jobs >
```

* You can examine the state of the consumer group and its consumers
```
XINFO CONSUMERS jobs worker-group
```

* ACKNOWLEDGE entries 1-0 and 2-0 read by worker-1
```
XACK jobs worker-group 1-0 2-0
```

* To see the pending entries in the consumer group you can use the XPENDING command. 
``` 
XPENDING jobs worker-group
```
This command can be used to identify which messages may have been read but not processed by a failed consumer. In this case, a working consumer can claim these pending messages. 

* Here worker-1 can claim the entries 3-0 and 4-0 (both are not acknowledged yet by worker-2) after a minimum idle time of 60s.
```
XCLAIM jobs worker-group worker-1 60000 3-0 4-0
```

## Next steps

Are you bored of walkthroughs in the CLI/GUI yet? In the next exercise, we're going to move to some actual code. 

So take a short break, get some coffee, and prepare for some coding in [exercise5](exercise-5-start.md).
