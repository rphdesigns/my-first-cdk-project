from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as _s3,
    # aws_sqs as sqs,
)
from constructs import Construct

class MyFirstCdkProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        _s3.Bucket(
            self,
            "MyBucketId",
            bucket_name="myfirstcdkproject2727",
            versioned=True,
            encryption=_s3.BucketEncryption.KMS_MANAGED
        )
