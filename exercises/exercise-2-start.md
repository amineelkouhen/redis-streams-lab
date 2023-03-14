<img src="../img/redis-logo-full-color-rgb.png" height=100/>

# Exercise 2 - RedisInsight

In the previous exercise, we started core Redis - or Redis Open Source (OSS) and worked with some basic stream commands via the redis-cli. This works well but is pretty hardcore. For development purposes, the Docker image we started also hosts the RedisInsight tool which offers a much improved user experience.
In this exercise, we'll discover this tool.

### Opening RedisInsight

The running redis-stack container already hosts the running RedisInsight application.

You can open it by going to 'Ports' in the Gitpod VS Code IDE (next to terminal), and clicking on the 8001 entry (as RedisInsight is running on port 8001).

Your browser should open a new tab and present you with a dialog asking for EULA and Privacy settings. If it doesn't it can be you have to open the url manually (or allow your browser to accept pop-ups from GitPod). Accept the recommended settings and the terms of use and Submit.

### Finding your way

In the top left you should see a view on the Redis Stack database. If you continued from the previous exercise, you will find three keys. Guess which they are? Right: 'hello', 'myhash' and 'mysortedset'.
Click on them to find their values displayed on the right.
Can you find out what the minimum Key Size in Redis is? 

Now set the TTL of the 'hello' string key to 5. Wait a while. Now try to edit the key again. What just happened?

While the GUI is convenient, it may be necessary to enter commands directly. We got you covered there: to enter commands, you can click the 'CLI' icon on the bottom left. Try to edit a key now.

But RedisInsight provides a more advanced CLI and tutorial as well: click on the 'Workbench' tab on the very left (below the Browser tab you are in now).

For the next exercises, we'll use the CLI for interacting with Redis.

## Next steps

Well done, you made it through the second exercise! Take a short break if you want, and then move on to [exercise 3](exercise-3-start.md).
