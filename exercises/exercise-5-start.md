<img src="../img/redis-logo-full-color-rgb.png" height=100/>

# Exercise 5 - Redis with Java/Lettuce

We're finally going to look at how we can programmatically work with Redis. In this case we'll use Java leveraging the Lettuce client to interact with Redis core data structures, RediSearch and TimeSeries.

The application we'll build is super light-weight without relying on higher-level abstraction frameworks such as Spring, Quarkus, JakartaEE or others. The only dependency is lettuce-core.

Let's get started!

## Running the code

Assuming you still have Redis running in GitPod, all we have to do is compile the app and run it.

From the [starting point](exercise5-start/) folder in the terminal window:

`./mvnw clean package assembly:assembly` to build the code
`java -cp target/demo-1.0-SNAPSHOT-jar-with-dependencies.jar com.redis.lars.App` to run the app

After this exercise you will have a running app with the scaffolding in place to interact with Redis. But making it do cool stuff is up to you. What we are looking for is for you to:

1. Store and retrieve a simple key/value pair
2. Store and retrieve a key/hash pair
3. Use the Lettuce Commands interface to extend the supported command set outside of the Redis OSS command set
4. Store and retrieve a collection of RedisTimeSeries values
5. Create an index on the hash data structure and phonetic search ("Try searching for something that sounds like 'world' but type it differently, e.g. 'wurld')
6. Use full-text search with highlighting

## Tips

You will find a complete working application including all the steps above [here](exercise5-solution/). However, try not to look at the solution before you tried to get it working yourselves.

## Next steps

Great! We created our first app interacting with Redis through the Lettuce client. We'll dive some deeper on client choices and caching in the next [exercise](exercise-6-start.md). 
