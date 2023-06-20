**Curriculum**

**Short Specializations**
- Average: 110.33%

**0x03. Queuing System in JS**
- Back-end
- JavaScript
- ES6
- Redis
- NodeJS
- ExpressJS
- Kue
- By: Johann Kerbrat, Engineering Manager at Uber Works
- Weight: 1
- Project will start on Jun 19, 2023, at 3:00 AM and must end by Jun 22, 2023, at 3:00 AM
- Manual QA review must be done (request it when you are done with the project)

**Resources**
Read or watch:
- Redis quick start
- Redis client interface
- Redis client for Node JS
- Kue (deprecated but still used in the industry)

**Learning Objectives**
At the end of this project, you are expected to be able to explain to anyone, without the help of Google, the following:

- How to run a Redis server on your machine
- How to run simple operations with the Redis client
- How to use a Redis client with Node JS for basic operations
- How to store hash values in Redis
- How to deal with asynchronous operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to build a basic Express app interacting with a Redis server and queue

**Requirements**
- All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- All of your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the `.js` extension

**Required Files for the Project**
- package.json
- .babelrc

To get started, you need to:
1. Install a Redis instance. Download, extract, and compile the latest stable Redis version (higher than 5.0.7).
2. Start Redis in the background with `src/redis-server`.
3. Make sure the server is working by using `src/redis-cli ping` (it should return "PONG").
4. Set the value "School" for the key "Holberton" using the Redis client.
5. Kill the server with the process ID of the `redis-server`.
6. Copy the `dump.rdb` from the `redis-5.0.7` directory into the root of the Queuing project.

Next, you need to perform the following tasks:

**Task 0: Node Redis Client**
- Install `node_redis` using npm.
- Write a script named `0-redis_client.js` that connects to the Redis server running on your machine.
- When the connection to Redis works correctly, it should log the message "Redis client connected to the server" to the console.
- When the connection to Redis does not work, it should log the message "Redis client not connected to the server: ERROR_MESSAGE" to the console.

**Task 1: Node Redis Client and Basic Operations**
- Copy the code from the previous task (0-redis_client.js) to a file named `1-redis_op.js`.
- Add two functions to the file:
  - `setNewSchool`: Accepts two arguments (`schoolName` and `value`) and sets the value for the key `schoolName` in Redis. It should display a confirmation message using `redis.print`.
  - `displaySchoolValue`: Accepts one argument (`schoolName`) and logs to the console the value for the key passed as an argument.
- At the end of the file, call `displaySchool