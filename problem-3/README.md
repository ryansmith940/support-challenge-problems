# Problem 3

This problem consists of an [AWS Batch job](https://aws.amazon.com/batch/) that is having problems. The `/infrastructure` folder contains a [cloudformation template](https://aws.amazon.com/cloudformation/) which creates the [AWS Batch Job Definition](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html).  The `/code` folder contains the python script which submits 3 Batch Jobs to the Job Definition created in `/infrastructure`.  The `/logs` folder contains the resulting logs for each of the 3 jobs submitted.

Jobs 1 and 2 ran fine, but job 3 failed.

1) Why did job 3 fail?
1) What is a possible solution?
1) Are there any other possible solutions?
