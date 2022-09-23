<img src="../img/redis-logo-full-color-rgb.png" height=100/>

# Exercise 4 - Advanced data models (TimeSeries, JSON)

In the previous exercise, we saw how modules augment the capabilities of Redis by adding functionality and data models depending on your needs. We also took RediSearch for a spin.
In this exercise, we'll dive into two more popular modules that extend Redis with data models for working natively with timeseries and JSON/document data.
Let's go!

### RedisTimeSeries
We start of with the RedisTimeSeries module. Where RediSearch is a module that adds capabilities to existing data structures, RedisTimeSeries is a module that adds a whole new data structure: Time Series. As a developer you may already be familiar with a lot of time series data already, e.g. are you monitoring memory usage over time in your production environment, or CPU usage, or maybe data from IoT sensors? 

* Let's see how this works in Redis and start by creating a Time Series data structure and put some data in it:
```
ts.create my_ts retention 0
```
This will create a Time Series called `my_ts` with its retention set to 'forever', e.g. there's not a moving window after which data values are discarded. Typically time series data would be discarded after doing aggregations, downsampling etc. in order to conserve resources and keep your data set small (==fast!). But since we don't want to be pressed by time in these exercises and we won't add a ton of data we'll store it forever (well, at least until you shut Redis off). Also notice that in the previous part we used `ft.<command>` and now we are using `ts.<command>`? That's because module commands have their own namespaces, so they do not interfere with the existing core Redis commands.

* Let's put some data in the Time Series and see what happens by typing the following commands:
```
ts.add my_ts 0 1.0
ts.add my_ts 1 2.0
ts.add my_ts 2 3.0
```
This will add three values to the Time Series at timestamps 0, 1 and 2 respectively. From your app, you'd probably add something like `System.currentTimeInMillis()` in here, but since we're typing things manually in this exercise we'll keep it short.
* Get the most recent value of the Time Series by typing:
```
ts.get my_ts
```
This will show you the most recent value of the Time Series, in this case `3`. 
* If we want to get the full range of the Time Series, we can type:
```
ts.range my_ts 0 2
```

In your own app you could try something like 'give me all the values in this Time Series between now and a week ago' or something similar. For now, we're done with the basics of Redis and the CLI. If you want to read more about time series, aggregation, compaction and downsampling then check out the [RedisTimeseries documentation](https://oss.redis.com/redistimeseries/).

### RedisJSON

RedisJSON is perhaps the most popular module together with RediSearch, as it introduces the capability to work with document/JSON data structures on the Redis server.

Let’s go ahead and test drive some JSON-specific operations for setting and retrieving a Redis key with a JSON value:

- Scalar
- Objects (including nested objects)
- Arrays of JSON objects
- JSON nested objects

#### Scalar

Under RedisJSON, a key can contain any valid JSON value. It can be scalar, objects or arrays. JSON scalar is basically a string. You will have to use the JSON.SET command to set the JSON value. For new Redis keys the path must be the root, so you will use “.” path in the example below. For existing keys, when the entire path exists, the value that it contains is replaced with the JSON value. 

* Here you will use JSON.SET to set the JSON scalar value to “Hello JSON!” Scalar will contain a string that holds “Hello JSON!”
```
JSON.SET greetings . ' "Hello JSON!" ''
```

* Use JSON.GET to return the value at path in JSON serialized form:
```
JSON.GET greetings
```

#### Objects

Let’s look at a JSON object example. A JSON object contains data in the form of a key-value pair. The keys are strings and the values are the JSON types. Keys and values are separated by a colon. Each entry (key-value pair) is separated by a comma. The { (curly brace) represents the JSON object:
```
{
    "employee": {
        "name": "alpha",
        "age": 40,
        "married": true
    }
}
```

* Let's try to insert JSON data into Redis:
```
JSON.SET employee_profile $ '{ "employee": { "name": "alpha", "age": 40,"married": true }  } '
```
* And to read it again:
```
JSON.GET employee_profile
```

The power of JSON in the database, is that you can't only store/load complete documents, but you can actually work with parts of the data. We'll go into this in the next few exercises.

##### Working with parts of JSON documents

To only query the JSON parameter you are interested in, use a JSONPath, so for instance to get only the age of the employee above:
```
JSON.GET employee_profile .employee.age
```

To find out the type of a JSON value at a certain path, use JSON.TYPE:
```
JSON.TYPE employee_profile
```

What is the type you get back? Is that expected?
Try to find the type of the age field. Is the result what you expect?

This is not all of the module's functionality. There's a lot more you can do with it, so if you want to learn more about all the functionality of the RedisJSON module, please check the [RedisJSON documentation](https://oss.redis.com/redisjson/).

## Next steps

Are you bored of walkthroughs in the CLI/GUI yet? In the next exercise, we're going to move to some actual code. So take a short break, get some coffee, and prepare for some coding in [exercise5](exercise-5-start.md).