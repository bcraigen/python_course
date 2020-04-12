# python_course
A cloud guru python course to list AWS EC2 instances and create snapshots

## About

This projec is a demo, and uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

This uses the configuration file created by the AWs cli. e.g.

`aws configure --profile shotty`

## Running

`pipenv run python shotty/shotty.py <command> <--project=PROJECT>`

*command* is list, start or stop
*project* is optional
