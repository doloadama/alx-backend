import express from 'express';
import redis from 'redis';
import { promisify } from 'util';
import kue from 'kue';

const app = express();
const port = 1245;
const client = redis.createClient();
const queue = kue.createQueue();

const reserveSeat = async (number) => {
  const setAsync = promisify(client.set).bind(client);
  await setAsync('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  const getAsync = promisify(client.get).bind(client);
  const availableSeats = await getAsync('available_seats');
  return parseInt(availableSeats, 10) || 0;
};

// Set the initial number of available seats to 50
reserveSeat(50);

let reservationEnabled = true;

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
    }
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const availableSeats = await getCurrentAvailableSeats();

    if (availableSeats === 0) {
      reservationEnabled = false;
    }

    if (availableSeats >= 1) {
      try {
        await reserveSeat(availableSeats - 1);
        done();
      } catch (error) {
        done(new Error('Not enough seats available'));
      }
    } else {
      done(new Error('Not enough seats available'));
    }
  });
});

queue.on('job complete', (id) => {
  console.log(`Seat reservation job ${id} completed`);
});

queue.on('job failed', (id, errorMessage) => {
  console.log(`Seat reservation job ${id} failed: ${errorMessage}`);
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
