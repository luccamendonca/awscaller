# Albert AWS console opener plugin "awscaller"

This is a very simple Python extension for the Albert Launcher that aims to help us developers/devops by opening and AWS console page using the provided service name.

## Installation

> Note: This plugin depends on [Albert Launcher v0.14.*](https://albertlauncher.github.io/docs/installing/)

```
git clone https://github.com/luccamendonca/awscaller /usr/share/albert/org.albert.extension.python/modules
```

## Usage

To trigger the extension you should type `aws <service name>` to open the given service page on your aws console, or type only `aws` to open the console home.

Examples:

```
aws lambda
aws s3
aws rds
aws apigateway
aws ec2
aws ecs
```

## Roadmap

- Allow to open the console page on a specific region