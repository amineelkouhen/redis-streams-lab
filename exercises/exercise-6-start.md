<img src="../img/redis-logo-full-color-rgb.png" height=100/>

# Exercise 6 - Redis caching use case with Java/Jedis

In this exercise we will meet 'the other Redis client' for Java: Jedis, and use it to cache data retrieved from an external API for ultra fast lookups.

As with the previous exercise, the application we'll build is super light-weight without relying much on higher-level abstraction frameworks such as Spring, Quarkus, JakartaEE or others. We do use Spring Boot for starting a webserver, but other than that the only dependency is jedis. 

Let's get started!

## Running the code

Assuming you still have Redis running in GitPod, all we have to do is compile the app and run it.

From the *exercise6-start* folder in the terminal window:

- `./mvnw -f pom.xml clean package` to build the code
- `java -jar target/redisbankplaces-0.0.1-SNAPSHOT-jar --spring.profiles.active=prod` to run the app

This app hosts a website at port 8080. Try to connect to it. What do you see?

## Tasks

## Tips

You will find a complete working application including all the steps above in the *exercise6-solution* folder. However, try not to look at the solution before you tried to get it working yourselves.

## Next steps

Nice! By now you experienced and got a taste of both Java clients, and will probably have a favorite already. 

After seeing Redis in action in this 'simple' caching use case, we'll next see Redis in full glory as the real-time database it is in our final [exercise](exercise-7-start.md). 