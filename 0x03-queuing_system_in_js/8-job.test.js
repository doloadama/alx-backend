import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    // Create a queue with Kue
    queue = kue.createQueue();
  });

  beforeEach(() => {
    // Set the queue to test mode
    queue.testMode(true);
  });

  afterEach(() => {
    // Clear the queue and exit the test mode
    queue.testMode(false);
    queue.clear();
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => {
      createPushNotificationsJobs('invalid', queue);
    }).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
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

    // Validate the jobs in the queue
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });
});
