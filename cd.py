import boto3

client = boto3.client('codedeploy')

response = client.create_deployment(
    applicationName='deployment',
    deploymentGroupName='shrmnik',
    revision= {
        'revisionType': 'S3',
        's3Location': {
           'bucket': 'garmihai',
           'Key': 'test',
           'bundleType': 'zip'
    }
}
)
