# Task 1: Docker

The build includes the following data stream:

producer.py (stdin) -> rabbitmq -> consumer.py -> MongoDB -> get_db_contents.py (stdout)

Rabbitmq, consumer.py and MongoDB are located in separate docker containers.


### Building and running

	docker-compose up -d
	
### Using setup from host

#### Installing dependencies (Python 3)
	pip install pymongo pika
	
#### Sending messages to rabbitmq

	$./producer.py
	Enter your message to store in MongoDB.
	> Hello!
	[x] Sent 'Hello!'
	> ^C (Exit)
	
#### Retrieving MongoDB contents

	$ ./get_db_contents.py
	Message 0: b'Hello!'