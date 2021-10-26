<img src="../img/redis-logo-full-color-rgb.png" height=100/>

# Exercise 5 - Putting it all together

In this exercise we will put everything that we've learned together as well as adding a few more interesting features. We'll be building a real application this time so let's get started! For this part we've provided you with a basic scaffolding application with a fully functional front-end which can be found [over here](exercise5-start/). You will be building the backend to make the whole application fully functional. We also provided a separate app for test data generation that can be found [over here](excercise5-datageneration)

## Goals

* Build a backend for a mobile banking app
* With a login page
* A streaming overview of transactions
* A searchable transaction overview
* Displays your bank balance over time
* An overview of 'biggest spenders on your bank account

## Application setup

For this exercises, we've provided you with a ready-to-go app to generate bank transaction data into Redis for you, so you do not have to write this yourself. You can find the app [over here](exercise5-datageneration). Build the app using

```
./mvnw clean package
```

But don't run it just yet, we'll run it later after we've finished building our own app. The data generation app generates bank transactions every ten seconds and puts them on a Redis Stream. A Stream is another Redis data structure and we'll be consuming the Stream in our own app. The app also populates a RedisTimeSeries of the account balance and a search index for RediSearch. We will be consuming these from our app as well.

* Start with the basic application provided [over here](exercise5-start) as this already contains the front-end that we will be using to interact with our backend application.

## Consuming a Redis Stream
* Consume the transactions Stream

A [Redis Stream](https://redis.io/topics/streams-intro) is an append-only log. The data generation app will put transaction on the Stream, and our application will consume the stream and send it to the frontend over a Websocket connection. Let's set this up!

* Add a new class called `BankTransactionForwarder` to the application that implements the `InitializingBean`, `DisposableBean`, and `StreamListener<String, MapRecord<String, String, String>>` interfaces. Also give it an `@Component` annotation. The first two interfaces make us implement the `afterPropertiesSet()` method and the `destroy()` method. The third one makes us implement the `onMessage(MapRecord<String, String, String> message)`. We'll use the first two for initialisation and cleanup and the onMessage is the callback for whenever a new BankTransaction comes in via the Redis Stream.
* In the constructor of the `BankTransactionForwarder`, add three parameters to the method signature (which will be autowired): a `RedisTemplate`, a `SimpMessageSendingOperations` and a `Config` object (the `Config` object is provided in our application already). Store them in instance variables.
* In the `afterPropertiesSet()` method, create a new `StreamMessageListenerContainer<String, MapRecord<String, String, String>>` and store it in an instance variable called `container`. To create the `StreamMessageListenerContainer`, use the following: `StreamMessageListenerContainer.create(redis.getConnectionFactory(), StreamMessageListenerContainerOptions.builder().pollTimeout(Duration.ofMillis(1000)).build())`.
* In the same method, start the newly created container using `container.start()`
* In the same method, create a new subscription using `container.receive(StreamOffset.latest("lars_transactions"), this)` and store it in an instance variable called `subscription`
* In the same method, call `subscription.await(Duration.ofSeconds(10))` to wait until the subscription is active

We are now subscribed to the Redis Stream. Whenever a new message arrives on the Stream, the `onMessage(...)` method of this class will be called. Of course, we still need to implement this method, so let's do that now.

* In the `onMessage(...)` method, call the `convertAndSend(config.getStomp().getTransactionsTopic(), message.getValue())` on the `SimpMessageSendingOperations` you created in the constructor.

* In the `destroy(...)` method, we can cancel the `Subscription` and stop the `Container` using

```
if (subscription != null) {
    subscription.cancel();
}

if (container != null) {
    container.stop();
}
```

And that's it! What we've just done is create a MessageListener and subscribed to the Redis Stream of BankTransactions and, for each incoming BankTransaction, forward the BankTransaction to the Stomp/Websocket topic. Now let's see how that looks in our application. Run the data generation in a terminal window. After that one is running, in a separate terminal window, build and run our app:


```
./mvnw clean package
./mvnw spring-boot-run
```

If all is well, both should now be running, so navigate to http://localhost:8080 and log in using `lars/larsje`. You should now see an overview of transactions and a few not-yet functional bits (because we will be enabling those next!). If all is well you should see new transactions popping in every ten seconds or so. Next, let's add the search feature!

* Add a new class called `BankTransactionController` and provide it with a `@RestController` annotation. Also add `@RequestMapping(path = "/api")` and `@CrossOrigin`.
* In the constructor, inject a `StatefulRediSearchConnection<String, String>` and save it in an instance variable called `srsc`.
* Create a method called `searchTransactions(@RequestParam("term") String term)` that returns a type of `SearchResults<String, String>`.
* Inside this method, we'll add the following code and return the `results` object:
```
    RediSearchCommands<String, String> commands = srsc.sync();

    SearchOptions options = SearchOptions
            .builder().highlight(Highlight.builder().field("description").field("fromAccountName")
                    .field("transactionType").tag(Tag.builder().open("<mark>").close("</mark>").build()).build())
            .build();

    SearchResults<String, String> results = commands.search(SEARCH_INDEX, term, options);
```        
What does this all mean? The first statement opens a RediSearch connection. The second one creates SearchOptions, based on our preferences. The third executes the search. 

* Now add a `@GetMapping("/search")` on the method. Then build and run the app and try the search!

Ok, now that we've got the search and the transaction overview working, let's do the balance over time view. The data generation app also populates a TimeSeries, so we can query this one and pass the result to the UI. Let's do that right now:

* Add a method called `balance()` that returns a `Map<String, String>` and add a `@GetMapping("/balance") on it. Using the following code we'll get the information out of the TimeSeries data structure:

```
tsc.range(BALANCE_TS, System.currentTimeMillis() - (1000 * 60 * 60 * 24 * 7),
                System.currentTimeMillis())
```

What we're doing here is asking "Give us the time series values of BALANCE_TS between now and (now -1 week).

* Build and run the app and see the balance over time populateed!

Now, last, but certainly not least, let's add the 'biggest spenders' functionality. This will show the biggest deductors from your bank account, in other words: where is my money going. For this purpose, the data-generation app is populating a Sorted Set. It's up to us to get the data out, so let's do exactly that!

* Add a method called `biggestSpenders()` that returns a `Set<TypedTuple<String>>` and put a `@GetMapping("/biggestspenders")` annotation on it. Use the following code to get the information out of the Sorted Set:

```
Set<TypedTuple<String>> range = redis.opsForZSet().rangeByScoreWithScores(SORTED_SET_KEY, 0, Double.MAX_VALUE);
```

This will get the range out of the sorted set by their scores and with the score, all the way from 0 up to `Double.MAX_VALUE`.

* Build and run the app, and watch in awe as the biggest spenders are now shown in the app!
