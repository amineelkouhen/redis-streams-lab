<img src="../img/redis-logo-full-color-rgb.png" height=100/>

# Demo 2 - Ingest data (flat files) into Redis Streams

To load data from plain files to Redis Streams, we will use RIOT (Redis Input Output Tools) to ingest plain CSV files into Redis as streams.

Let's get started!

## Install RIOT tools 

Now, let's install the RIOT-File tool. 

RIOT-File can be installed in different ways depending on your environment and preference. If you want to install it in MacOS, you can use Homebrew with the command:

```bash
brew install redis-developer/tap/riot-file
```

You can also download the [latest release](https://github.com/redis-developer/riot/releases/latest), unzip, and copy to the desired location. Then launch the `bin/riot-file` script.

Or, you can simply run the latest docker image: 

```bash
docker run fieldengineering/riot-file [OPTIONS] [COMMAND]
```
## Batch Ingestion using RIOT
 
Redis Input/Output Tools (RIOT) is a series of utilities designed to help you get data in and out of Redis in a batch fashion. It consists of several module that can ingest data from files (RIOT-File), or from relational databases to Redis (RIOT-DB). It can be also used to migrate data from/to Redis (RIOT-Redis). RIOT supports Redis open-source (OSS) and Redis Enterprise in either standalone or cluster deployments.

The RIOT tool reads a fixed number of records (batch chunk), processes it, and writes it at a time. Then the cycle is repeated until there’s no more data on the source. The default batch size is 50, which means that an execution step reads 50 items at a time from the source, processes them, and finally writes then to the target. If the target is Redis, writing is done in a single command [pipeline](https://redis.io/topics/pipelining) to minimize the number of roundtrips to the server. You can change the batch size (and hence pipeline size) using the `--batch` option. The optimal batch size in terms of throughput depends on a few factors like record size and command types (see [here](https://stackoverflow.com/a/32165090) for details). 

RIOT can implement processors to perform custom transformations to the ingested data, and apply filters based on regular expressions before writing data in the landing storage support.

It is possible to parallelize processing by using multiple threads using the `--threads` option. In that configuration, each chunk of items is read, processed, and written in a separate thread of execution. This is different from partitioning where items would be read by multiple readers (see Redis Data Integration). Here, only one reader is being accessed from multiple threads.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEid0eb-406mXHGDy75wAAKQMkqbLw_ZLhGGj_Y0hZ-wmd0OhOAvCjzUE3FXVlfSZdzFa4yaShRkGyma43lxrklmrRqyudb2S77mebFC3p-pUsR7YNqw5yyPQf4T_5hT-uPey0tlX0hYrm7Sk99cd7jDsNaUqBV_PX69iG_TJidY_DuvgzXWz7mIcpDH)
    
## Flat files ingestion using RIOT-File  

RIOT-File provides commands to read from files and write to Redis. It supports a variety of file formats as delimited flat files : CSV, TSV, PSV, or fixed-width files. RIOT-File can also import files in JSON or XML formats.

To ingest data from flat files to a Redis database, you need to execute the import command: 

```
riot-file -h <host> -p <port> import FILE... [REDIS COMMAND...]
```

The import command reads from files and writes to Redis. The file paths can be absolute or in a URL form. Paths can include wildcard patterns (eg., file\_\*.csv).You can also ingest objects from AWS S3 or GCP storage service using the object URL.

RIOT-File will try to determine the file type from its extension (e.g. .csv or .json), but you can specify it explicitly using the `--filetype` option.

For flat file formats (delimited and fixed-length) you can use the `--header` option to automatically extract field names from the first row of the file. Otherwise you can specify the field names using the `--fields` option.

The default delimiter character is comma (,). It can be customized by using the `--delimiter` option.

Let's consider this CSV [file]( https://raw.githubusercontent.com/aelkouhen/Geo-Maersk/master/geo_unlocode/airport.csv):

<div class="table-wrapper" markdown="block">
    
| **AirportID** | **Name**                                    | **City**     | **Country**      | **IATA** | **ICAO** | **Latitude**        | **Longitude**      | **Altitude** | **Timezone** | **DST** | **Tz**               | **Type** | **Source**  |
| ------------- | ------------------------------------------- | ------------ | ---------------- | -------- | -------- | ------------------- | ------------------ | ------------ | ------------ | ------- | -------------------- | -------- | ----------- |
| **1**         | Goroka Airport                              | Goroka       | Papua New Guinea | GKA      | AYGA     | \-6.081689834590001 | 145.391998291      | 5282         | 10           | U       | Pacific/Port_Moresby | airport  | OurAirports |
| **2**         | Madang Airport                              | Madang       | Papua New Guinea | MAG      | AYMD     | \-5.20707988739     | 145.789001465      | 20           | 10           | U       | Pacific/Port_Moresby | airport  | OurAirports |
| **3**         | Mount Hagen Kagamuga Airport                | Mount Hagen  | Papua New Guinea | HGU      | AYMH     | \-5.826789855957031 | 144.29600524902344 | 5388         | 10           | U       | Pacific/Port_Moresby | airport  | OurAirports |
| **4**         | Nadzab Airport                              | Nadzab       | Papua New Guinea | LAE      | AYNZ     | \-6.569803          | 146.725977         | 239          | 10           | U       | Pacific/Port_Moresby | airport  | OurAirports |
| **5**         | Port Moresby Jacksons International Airport | Port Moresby | Papua New Guinea | POM      | AYPY     | \-9.443380355834961 | 147.22000122070312 | 146          | 10           | U       | Pacific/Port_Moresby | airport  | OurAirports |
| **6**         | Wewak International Airport                 | Wewak        | Papua New Guinea | WWK      | AYWK     | \-3.58383011818     | 143.669006348      | 19           | 10           | U       | Pacific/Port_Moresby | airport  | OurAirports |

</div>

The following command imports that CSV file into a Redis Stream `airports`. 

```
riot-file -h localhost -p 6379 import https://raw.githubusercontent.com/aelkouhen/Geo-Maersk/master/geo_unlocode/airport.csv --header xadd --keyspace airports
``` 
<img width="1512" alt="RedisInsight" src="https://user-images.githubusercontent.com/105490765/225297192-d06dc2fa-196c-498a-8dc6-cac3a6c5caba.png">

## Next steps

Excellent work! We have ingested a plain into Redis Streams using RIOT. In the next [exercise](exercise-7-start.md), we will try to persist our Redis streams in an AWS S3 bucket. 
