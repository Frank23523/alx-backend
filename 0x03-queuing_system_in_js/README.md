# Redis Setup for Queuing System in JS

This project uses Redis version 6.0.10. Follow these steps to set up Redis:

1. Download and compile Redis:

   ```
   wget http://download.redis.io/releases/redis-6.0.10.tar.gz
   tar xzf redis-6.0.10.tar.gz
   cd redis-6.0.10
   make
   ```

2. Start Redis in the background:

   ```
   src/redis-server &
   ```

3. Verify the server is working:

   ```
   src/redis-cli ping
   ```

   This should return `PONG`.

4. Set a test value:

   ```
   src/redis-cli
   127.0.0.1:[Port]> set Holberton School
   127.0.0.1:[Port]> get Holberton
   ```

   This should return "School".

5. To stop the Redis server:

   ```
   ps aux | grep redis-server
   kill [PID_OF_Redis_Server]
   ```

6. The `dump.rdb` file from the Redis directory has been copied to the root of this project.

## Requirements

- Running `get Holberton` in the Redis client should return `School`.
- All code will be interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7.
- All files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- Code should use the `.js` extension.
