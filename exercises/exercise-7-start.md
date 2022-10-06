<img src="../img/redis-logo-full-color-rgb.png" height=100/>

# Exercise 7 - real-time data in action in a complete app: RedisBank

In this exercise we will put everything that we've learned together as well as adding a few more interesting features. We'll be building a real application this time so let's get started! For this part we've provided you with a basic scaffolding application with a fully functional front-end which can be found [over here](exercise7-start/). This will be the starting point for this exercise. You will be building the backend to make the whole application fully functional. We also provided a separate app for test data generation that can be found [over here](exercise7-datageneration) Last, but not least, you can find a fully working solution [over here](exercise7-solution).

## Architecture
Data generation app -> Generates bank transactions and puts them on a Redis Stream. It also populates a RediSearch index and creates a TimeSeries for the account balance and a Sorted Set for the 'biggest spenders' on the account. The transactions Stream is stored under a key called `transactions_lars` (as `lars` is the only user in the app at the moment), the TimeSeries under a key called `balance_ts_lars`, the Sorted Set under a key called `bigspenders_lars` and the search indices under a general key. 

The app that we're going to be working on will consume these data structures and show them in a UI (which has been provided).

You can view a picture of the overall architecture [over here](../img/architecture.png).

## Getting started

Assuming you still have Redis running in GitPod, all we have to do is compile the app and run it.

From the *exercise7-start* folder in the terminal window:

- `./mvnw clean package` 
- `./mvnw spring-boot:run` to build and run the app

This app hosts a website at port 8080. Try to connect to it, and pass the login page with user `lars` and password `larsje`. You should be able to login, but the following screen is still kind of empty. So let's stop the app for now, and then do something about that!

### Consuming a Redis Stream
* Consume the transactions Stream

A [Redis Stream](https://redis.io/topics/streams-intro) is an append-only log. The [data generator](https://github.com/ruurdk/redisbank/blob/basicstart/src/main/java/com/redislabs/demos/redisbank/transactions/BankTransactionGenerator.java#117) will put transaction on the Stream, and our application will subscribe to this Stream and will consume any income transactions.

The only thing we have to do now is store them as JSON in Redis and send them to the frontend over a Websocket connection. The magic happens in the [onMessage method](https://github.com/ruurdk/redisbank/blob/basicstart/src/main/java/com/redislabs/demos/redisbank/transactions/BankTransactionForwarder.java#L57)

In here, include the code to do just that:
```java
try {
    // if we need an object we could do this but we can use native String/JSON as well
    // BankTransaction bankTransaction = SerializationUtil.deserializeObject(messageString, BankTransaction.class);
    RedisJSONCommands<String, String> red = redismod.sync();
    red.jsonSet("RedisBank:BankTransaction:"+ message.getId().getValue(),
        ".", // JSON Path
        messageString
    );
} catch (Exception e) {
    LOGGER.error("Error parsing JSON: {}", e.getMessage());
}

// Stream message to websocket connection topic
smso.convertAndSend(config.getStomp().getTransactionsTopic(), message.getValue());
LOGGER.info("Websocket message: {}", messageString);
```

And that's it for this part. Now let's see how that looks in our application. Build and run our app:

```
./mvnw clean package
./mvnw spring-boot-run
```

If all is well, if you navigate to http://localhost:8080 and log in using `lars/larsje`, you should now see an overview of transactions and a few not-yet functional bits (because we will be enabling those next!). If all is well you should see new transactions popping in every ten seconds or so. If not, check your source code and see if you missed any annotations or other parts. Next, let's add the search feature! 



## Tips

You will find a complete working application including all the steps above in the *exercise7-solution* folder. However, try not to look at the solution before you tried to get it working yourselves.

# Interesting code to explore

- [BankTransaction](https://github.com/ruurdk/redisbank/blob/basic/src/main/java/com/redislabs/demos/redisbank/transactions/BankTransaction.java) is a plain POJO
- Stored in Redis using RedisJSON Lettuce [redis.jsonSet](https://github.com/ruurdk/redisbank/blob/442905b1c47bf045a12f288d4af932740e5a0b51/src/main/java/com/redislabs/demos/redisbank/transactions/BankTransactionForwarder.java#L65)  
- With an index in RediSearch [BankTransactionGenerator](https://github.com/ruurdk/redisbank/blob/442905b1c47bf045a12f288d4af932740e5a0b51/src/main/java/com/redislabs/demos/redisbank/transactions/BankTransactionGenerator.java#L87)
- and with RediSearch query thru a REST/JSON api [TransactionOverviewController](https://github.com/ruurdk/redisbank/blob/442905b1c47bf045a12f288d4af932740e5a0b51/src/main/java/com/redislabs/demos/redisbank/transactions/TransactionOverviewController.java#L99)

and also
- biggest spenders categories using Redis sorted set [redis.incrementScore](https://github.com/ruurdk/redisbank/blob/442905b1c47bf045a12f288d4af932740e5a0b51/src/main/java/com/redislabs/demos/redisbank/transactions/BankTransactionGenerator.java#L162)
- accessed using a Redis sorted set range [redis.rangeByScoreWithScores](https://github.com/ruurdk/redisbank/blob/442905b1c47bf045a12f288d4af932740e5a0b51/src/main/java/com/redislabs/demos/redisbank/transactions/TransactionOverviewController.java#L81)

## Next steps

Congrats! You made it to the end of our workshop.

By now you should have a solid overview of Redis data types, ways to interact (CLI, GUI, Java and client options). 

On top of that we also explored some use cases ranging from Redis as a cache to a modern real-time database.