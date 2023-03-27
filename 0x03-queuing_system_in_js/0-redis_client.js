import redis from 'redis';
const client = redis.createClient(6379, '127.0.0.1');
client.on('connect', () => {
    console.log('Redis client connected to the server')
});

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${Error}`);
});
