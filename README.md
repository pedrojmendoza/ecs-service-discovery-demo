# ECS Service Discovery

![Architecture](https://github.com/ranman/ecs-service-discovery-demo/raw/master/backend/static/sd.png)

Full details in the [blog post](https://aws.amazon.com/blogs/aws/amazon-ecs-service-discovery/)!

This provides two docker containers: backend and worker. Both run simple flask apps. The ".corp" domain name is assumed.

= Step by step

* Create cluster (Fargate) for ecs-service-registry

* Create ECR repo for ecs-service-registry-worker
* Create ECR repo for ecs-service-registry-backend

* $(aws ecr get-login --no-include-email --region us-east-1)

* docker build -t ecs-service-registry-worker .
* docker tag ecs-service-registry-worker:latest 264359801351.dkr.ecr.us-east-1.amazonaws.com/ecs-service-registry-worker:latest
* docker push 264359801351.dkr.ecr.us-east-1.amazonaws.com/ecs-service-registry-worker:latest
* Create task definition for ecs-service-registry-worker
* Create/deploy service for ecs-service-registry-worker

* aws servicediscovery list-services
* aws servicediscovery get-service --id <SERVICE_ID_FROM_PREVIOUS_OUTPUT>
* Adjust backend/app.py to reflect NAMESPACE_ID's value based on the output of the aws servicediscovery get-service above as well as namespace's name (aka hosted zone's domain name)

* docker build -t ecs-service-registry-backend .
* docker tag ecs-service-registry-backend:latest 264359801351.dkr.ecr.us-east-1.amazonaws.com/ecs-service-registry-backend:latest
* docker push 264359801351.dkr.ecr.us-east-1.amazonaws.com/ecs-service-registry-backend:latest
* Create task definition for ecs-service-registry-backend
* Create/deploy service for ecs-service-registry-backend

* Test by hitting public IP for ecs-service-registry-backend's task
