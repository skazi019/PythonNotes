# Systems Design

## Microservice Architecture
 - You switch to a microservice architecture not when the scale of the users increase, but when the scale of your team increases i.e. when you get more developers.
 - Instead of one service making API calls to another. What we can do is create a library that has functions that do the job of calling the APIs on the other service and the new service just has to download this library and call those functions.
 - Deployments can be done using CI/CD methodologies like Jenkins and should be deployed in container, this is done to make the deployments much more seamless.
 - Push logs from all the microservices into one single datbase, eg: elastic stack works best here, thorugh a service like kafka.
 - Every microservice needs to encapsulate the data it is responsible for.

## Pub/Sub Messaging
It is a form of asynchronous service-to-service communication used in _serverless_ and _microservice_ architectures.\
In a Pub/Sub model, a _message published_ to a _topic_ is immediately receieved by all of the _subscribers of this topic_.\
Pub/Sub messaging can be used to **enable event-driven programming** or to de-couple applications in order to increase performance, reliablity,
and scalability.\
The Pub/Sub model allows for message to be broadcast to different part of the system asynchronously. A **message topic**, sibling to a _message queue_, provides a light-weight mechanism to broadcast asynchrounous event notifications, and endpoints to allow software components to connect to the topic in order send or receive those messages.\
To _broadcast_ a message, a component called a **publisher** simply pushes a **message** to the **topic**.\
Unlike **message queues** which _batch messages_ until they are retrieved, message topic transfer messages with no or very little queuing, and push them out immediately to all subscribers.\
All components that subscribe to a topic will receive every message that is broadcast.

<br />

![Pub/Sub](https://d1.awsstatic.com/product-marketing/Messaging/sns_img_topic.e024462ec88e79ed63d690a2eed6e050e33fb36f.png)

<br />

The subscribers can do whatever they like with the message in parallel.\
The publisher doesn't need to know who is using the information and the subscribers don't need to know who is broadcasting the message.
