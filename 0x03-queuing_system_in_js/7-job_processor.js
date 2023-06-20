import kue from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781', '4153518743', '4153538781', '4153118782', '4153718781',
'4159518782', '4158718781', '4153818782', '4154318781',  '4151218782'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);

  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  // Perform notification sending here...

  done();
}

const queue = kue.createQueue({ concurrency: 2 });

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message, job, done);
});

queue.on('error', (error) => {
  console.log(`Queue error: ${error}`);
});
