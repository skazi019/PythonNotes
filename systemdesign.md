# Systems Design

## Microservice Architecture
 - You switch to a microservice architecture not when the scale of the users increase, but when the scale of your team increases i.e. when you get more developers.
 - Instead of one service making API calls to another. What we can do is create a library that has functions that do the job of calling the APIs on the other service and the new service just has to download this library and call those functions.
 - Deployments can be done using CI/CD methodologies like Jenkins and should be deployed in container, this is done to make the deployments much more seamless.
 - Push logs from all the microservices into one single datbase, eg: elastic stack works best here, thorugh a service like kafka.
 - Every microservice needs to encapsulate the data it is responsible for.