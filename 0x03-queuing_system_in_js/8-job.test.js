import { expect } from 'chai';
import kue from 'kue';
import sinon from 'sinon';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw(
      'Jobs is not an array',
    );
  });

  it('should create two new jobs in the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });

  it('should call the console.log with the correct messages', () => {
    const consoleLogSpy = sinon.spy(console, 'log');
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    const job = queue.testMode.jobs[0];

    expect(consoleLogSpy.calledWith(`Notification job created: ${job.id}`)).to
      .be.true;

    job.emit('complete');
    expect(consoleLogSpy.calledWith(`Notification job ${job.id} completed`)).to
      .be.true;

    job.emit('failed', new Error('Job failed'));
    expect(
      consoleLogSpy.calledWith(
        `Notification job ${job.id} failed: Error: Job failed`,
      ),
    ).to.be.true;

    job.emit('progress', 50);
    expect(consoleLogSpy.calledWith(`Notification job ${job.id} 50% complete`))
      .to.be.true;

    consoleLogSpy.restore();
  });
});
