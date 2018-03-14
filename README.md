# Albert AWS console opener plugin "awscaller"

<p align="center">
  <!-- <img src="https://i.imgur.com/gPCNyGQ.png" alt="Cover image"/> -->
  <img src="https://i.imgur.com/2Uf93Rp.png" alt="Cover image"/>
</p>

This is a very simple Python extension for the Albert Launcher that aims to help us developers/devops by opening and AWS console page using the provided service name.

## Installation

> Note: This plugin depends on [Albert Launcher v0.14.*](https://albertlauncher.github.io/docs/installing/)

```
git clone https://github.com/luccamendonca/awscaller /usr/share/albert/org.albert.extension.python/modules/awscaller
```

Then you just need to go to the Extension settings and enable the "awscaller" Python extension:

<p align="center">
  <img src="https://i.imgur.com/XlOlSNc.png" alt="Enabling Python Extension"/>
</p>

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

---

We also support query string parameters that can be used for pretty much anything AWS console supports doing via query strings.

How to use:

```
aws <service> <key>:<value>...
```

Example:

```
aws ec2 region:us-east-1
```

## Backlog

- Allow specific querying for specific aws services, such as EC2 filters
