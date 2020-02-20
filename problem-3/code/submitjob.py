#!/usr/bin/env python

import boto3

def main():
    #submit_job(256)
    #submit_job(512)
    submit_job(10240)

def submit_job(array_size_MB):
    batch_client = boto3.client('batch')

    # The job_queue was already created, and is outside of the scope of the problem
    job_queue = 'sb-thes-vqcmain'

    # The job definition was created in /infrastructure. Look at jobdefinition.cftemplate for details
    jobDefinitionName = "SampleProblem3JobDefinitionName"

    response = batch_client.submit_job(
        jobName=f'CreateByteArray_{array_size_MB}',
        jobQueue=job_queue,
        jobDefinition=jobDefinitionName,
        containerOverrides=dict(
            command=['python', '-c', f'x = bytearray({array_size_MB}00000); print("Done")']
        )
    )

    print(response)

if __name__ == "__main__":
    main()