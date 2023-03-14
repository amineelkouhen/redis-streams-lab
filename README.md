<img src="img/redis-logo-full-color-rgb.png" height=100/>

## Redis Streams - Technical Lab
In this hands-on lab you will learn how to create and manipulate Redis Streams. You will learn how easy it is to build extremely fast applications using only a minimum of code. The entire hands-on lab is self-service and is made up of several exercises.

The hands-on lab is hosted remotely via [Gitpod](https://gitpod.io/).

## Prerequisites

* A laptop/desktop equipped with a modern browser
* A working internet connection (use corporate proxies or bad WiFi at your own peril)
* Click the 'Open in Gitpod' button in the `Getting Started` section to spin up the hands-on lab on Gitpod (Github/GitLab or Atlassian account required)
* The Gitpod instance will setup all required dependencies for you, including an IDE, no need to install anything!

If you don't like Gitpod, you can also clone the repo and work locally. In that case [Pyhton 3](https://www.python.org/download/releases/3.0/) is required, along with [Docker](https://www.docker.com/products/docker-desktop) and an IDE, e.g. [vscode](https://code.visualstudio.com/), [idea](https://www.jetbrains.com/idea/), [eclipse](https://www.eclipse.org/eclipseide/) or [netbeans](https://netbeans.apache.org/)

## Required knowledge

We expect you to be somewhat familiar with Python but if you're not: don't worry, working source code is provided in this hands-on lab.

## Getting started
Use the button below to create a Gitpod instance and run this hands-on lab. This hands-on lab consists of multiple exercises, see the links below. Each exercise has a goal and a set of sub goals to achieve. Start with exercise 1 and work your way from there. Good luck and enjoy!

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#GITPOD=gitpod/https://github.com/ruurdk/redis-dev-handsonlab)

## Exercises

* Exercise 1 - Streams Simple Add and Reads: [start](exercises/exercise-1-start.md)
* Exercise 2 - GUI: meet RedisInsight: [start](exercises/exercise-2-start.md)
* Exercise 3 - Managing Stream Length: [start](exercises/exercise-3-start.md)
* Exercise 4 - Streams Consumer Groups: [start](exercises/exercise-4-start.md)
* Exercise 5 - Coding: From a RabbitMQ queue to Redis Streams: [start](exercises/exercise-5-start.md)
* Exercise 6 - Coding: Persist Redis Streams to AWS S3: [start](exercises/exercise-6-start.md)

## Troubleshooting

### General

If your laptop has corporate restrictions in terms of installing software, internet proxies or other restrictions, it might be tricky to get this hands-on lab up and running, even though we minimised the required dependencies by running this hands-on lab in the browser via Gitpod. Asking the instructor may help, but we can't guarantee we'll get it working and we won't help you circumvent corporate policies.

### Redis

Make sure Redis is running when running the exercises. During building this is not required as the integration tests support [Testcontainers](https://www.testcontainers.org/).

# Disclaimer

Redis Labs proprietary, subject to the Redis Enterprise Software and/or Cloud Services license
