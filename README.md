# AWS Proton Sample Services

This repository contains samples of application code that can be deployed with AWS Proton using the for both [AWS CloudFormation](https://github.com/aws-samples/aws-proton-sample-templates) and [Terraform](https://github.com/aws-samples/aws-proton-terraform-sample-templates). 

To use these services, fork this repository and provide your forked repository as an input when you create a service. The AWS Proton sample templates include a pipeline parameter (service-dir) that allows you to select a directory within the repository, so that you can choose the right service for your particular template type.

- ## ecs-backend

    Flask app that responds with a Hello message along with the Time.  [README](./ecs-backend)

- ## ecs-ping-backend-a-record

    Application code to ping Fargate backend service using service discovery. [README](./ecs-ping-backend-a-record)

- ## ecs-ping-backend-srv-record

    Application code to ping ECS on EC2 backend service using service discovery. [README](./ecs-ping-backend-srv-record)

- ## ecs-ping-sns

    Python application that sends a random 5-letter string along with the time to the shared SNS topic, every 5 minutes. [README](./ecs-ping-sns)

- ## ecs-static-website

    Containerized static website. [README](./ecs-static-website)

- ## ecs-worker

    Python application that polls the SQS queue for messages, and writes the message body to CloudWatch logs. [README](./ecs-worker)

- ## lambda-ping-sns

    Lambda function to send a random string and time to the shared SNS topic, whenever invoked by API Gateway HTTP API. [README](./lambda-ping-sns)

- ## lambda-worker

    Lambda function that writes the event, context object and SQS message to CloudWatch Logs. [README](./lambda-worker)

## Security

See [CONTRIBUTING](./CONTRIBUTING.md#security-issue-notifications) for more information.

## Code of Conduct

See [CODE OF CONDUCT](./CODE_OF_CONDUCT.md) for more information.

## License

This library is licensed under the MIT-0 License. See the [LICENSE](./LICENSE) file.

