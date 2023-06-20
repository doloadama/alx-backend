import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    // Create a queue with Kue
    queue = kue.createQueue();
  });

  afterEach(() => {
    // Clear the queue and shutdown the queue connection
    queue.shutdown(5000, () => {
      queue.clear();
    });
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => {
      createPushNotificationsJobs('invalid', queue);
    }).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', (done) => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 5678 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    setTimeout(() => {
      // Check the number of jobs in the queue
      queue.inactiveCount((err, count) => {
        expect(count).to.equal(2);
        done();
      });
    }, 100);
  });
});
