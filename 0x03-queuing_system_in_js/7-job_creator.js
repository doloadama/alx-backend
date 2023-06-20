import kue from 'kue';

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account',
  },
  // ...rest of the jobs
];

const queue = kue.createQueue();

jobs.forEach((jobData) => {
  const job = queue.create('push_notification_code_2', jobData)
    .save((error) => {
      if (!error) {
        console.log(`Notification job created: ${job.id}`);
      }
    });

  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  job.on('failed', (error) => {
    console.log(`Notification job ${job.id} failed: ${error}`);
  });

  job.on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
});

queue.on('error', (error) => {
  console.log(`Queue error: ${error}`);
});
