import kue from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
    job.fail(error);
    done(error);
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
}

const queue = kue.createQueue({
  concurrency: 2, // Process two jobs at a time
});

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

queue.on('error', (error) => {
  console.log(`Queue error: ${error}`);
});
