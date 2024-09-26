import kue from 'kue';

const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobInfo) => {
    const job = queue.create('push_notification_code_3', jobInfo);

    job.save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id || 'unknown'}`);
      }
    });

    job.on('complete', () => {
      console.log(`Notification job ${job.id || 'unknown'} completed`);
    });

    job.on('failed', (err) => {
      console.log(`Notification job ${job.id || 'unknown'} failed: ${err}`);
    });

    job.on('progress', (progress) => {
      console.log(
        `Notification job ${job.id || 'unknown'} ${progress}% complete`,
      );
    });
  });
};

export default createPushNotificationsJobs;
