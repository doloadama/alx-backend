import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);


// Handle successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle connection errors
client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(`Value for key ${schoolName}: ${value}`);
    } catch (error) {
        console.log(`Error retrieving value for key ${schoolName}: ${schoolName}: ${error.message}`);
    };
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', 100);
displaySchoolValue('HolbertonSanFrancisco');
