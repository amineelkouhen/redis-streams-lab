<img src="../img/redis-logo-full-color-rgb.png" height=100/>

# Exercise 3 - Introduction to modules (RediSearch)

While Redis has a very powerful set of data structures straight out of the box, it's always possible that you find yourself in a situation where these are not enough to cover your use cases. In those situations Redis Modules comes to the rescue! Modules allow you to extend Redis data structures and features in a modular way; you only add those modules to a specific database that you want and no more. This keeps your Redis setup fast and lean. There are many community modules available and Redis provides several modules itself as well. If that's not enough you can also write your own. The Docker container that we used to start Redis has a few modules bundled with it already, so let's take a look at a few examples. For more information on modules, see the [Redis Modules Hub](https://redis.com/community/redis-modules-hub/) and the [Redis Enterprise Modules](https://redis.com/redis-enterprise/modules/) pages.

### RediSearch
Let's start with RediSearch, a full-text search module for Redis. Retrieving keys by their primary value is fine for many use cases, but what if I have data in the cache that needs to be searched? E.g. a product model, or stores, or transactions by a certain vendor, etc. Typically this is where a key/value model starts to show its limitations. RediSearch to the rescue! RediSearch adds full-text search capabilities to Redis as well as a lot more. See the [RediSearch documentation](https://docs.redis.com/latest/modules/redisearch/) for more detailed information on this module, or checkout the [GitHub repo](https://github.com/RediSearch/RediSearch).

* First, we'll create a search index on Hash structures matching a certain prefix:
```
ft.create my_idx on hash prefix 1 my schema hello text phonetic dm:en
```
This command is a little bit more elaborate than the previous ones, so let's explore it in detail a bit more. We're creating an index called `my_idx` on the `hash` datastructure with one prefix `my` (remember that we created a Hash earlier that had the key `myhash`? also note that if you used a different key for the hash that you should also use a different prefix here) and we define the schema to be on the `hello` field (this field is present in the Hash we created earlier) which we define as a `TEXT` field and we also setup phonetic search using the `Double Metaphone for English` matcher. That's quite a handful, so don't worry if that doesn't mean a lot to you right now, let's just see what it actually does!
* Let's search our immense data set of 1 Hash and see if we can find what we want by typing a few different commands:
```
ft.search my_idx "world"
```

This will return our Hash that we created earlier.

* You can also do a wildcard search:
```
ft.search my_idx "wor*"
```
* Remember that we setup the index to be phonetic? Try it out by something that sounds like `world` but not quite:
```
ft.search my_idx "wurld"
```
This is great if your users need to search for something, but may not be able to recall exactly what it was they are searching for, or how it is spelled exactly. Another great feature is that search results can be highlighted on which part the match was found:
```
ft.search my_idx "world" highlight
```
Notice how the word `world` has no been surrounded by ```<b></b>``` tags. This is great in case we want to visually display the matching words differently in our UI. We can also change the tags by doing the following:
```
ft.search my_idx "world" highlight tags <hello> </hello>
```
Notice how the word `world` is now surrounded with the tags of our choosing.

And that's not all of the module's functionality; there's plenty more, so if you want to learn more about all the functionality of the RediSearch module, please check the [RediSearch documentation](https://oss.redis.com/redisearch/).

## Next steps

Well done, you made it through the third exercise! You can move on to [exercise 4](exercise-4-start.md) directly.