<img src="../img/redis-logo-full-color-rgb.png" height=100/>

# Exercise 2 - RedisInsight

In the previous exercise, we started Redis and worked with some basic data types via the redis-cli. This works well but is pretty hardcore. For development purposes, the Docker image we started also hosts the RedisInsight tool which offers a much improved user experience.
In this exercise, we'll discover RedisInsight.

### Opening RedisInsight

The running redis-stack container already hosts the running RedisInsight application.

You can open it by going to 'Ports' in the Gitpod VS Code IDE (next to terminal), and clicking on the 8001 entry (as RedisInsight is running on port 8001).

Your browser should open a new tab and present you with a welcome dialog. Accept the defaults and terms of use and continue.

### Finding your way

In the top left you should see a view on the Redis database. If you continued from the previous exercise, you will find three keys. Guess which they are? Right: 'hello', 'myhash' and 'mysortedset'.
Click on them to find their values displayed on the right.

To enter commands, you can click the 'CLI' icon on the bottom left. Try to edit a key. For the next exercises, we'll use this CLI for interacting with Redis.

## Next steps

Well done, you made it through the first exercise! Take a short break if you want, and then move on to [exercise 3](exercise-3-start.md).
