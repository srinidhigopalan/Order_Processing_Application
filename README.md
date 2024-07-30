# Order Processing Application

This project processes order data to compute various revenue metrics and validates the processing logic using unit tests. Docker is used for containerization, ensuring a consistent environment for running the application and tests.

## File Structure

/

├── Dockerfile

├── Dockerfile-tests

├── main.py

├── test.py

├── requirements.txt

├── orders.csv

└── README.md

## File Descriptions

main.py: Contains the main code for processing order data. This script reads data from orders.csv, computes revenue metrics, and prints the results.

test.py: Contains unit tests that verify the correctness of the data processing logic implemented in main.py. It uses the unittest framework to ensure the application behaves as expected.

Dockerfile: Dockerfile for building an image to run the main application. It sets up the environment, installs dependencies, and executes main.py.

Dockerfile-tests: Dockerfile for building an image to run the unit tests. It sets up the environment, installs dependencies, and executes test.py.

requirements.txt: Lists the Python dependencies needed for both the application and the tests. Currently, it includes pandas.

orders.csv: Contains sample order data used for running the application and performing tests. It includes fields such as order_id, customer_id, order_date, product_id, product_name, product_price, and quantity.

README.md: This file. It provides an overview of the project, setup instructions, and details about each file.

## Setup

### Prerequisites

Ensure Docker is installed on your system. You can follow the instructions on Docker's website to install Docker.

### Building and Running the Application and Tests

1. Build the Docker Image for the Application
   
docker build -t myapp .

docker build -t myapp-tests -f Dockerfile-tests .

This command builds a Docker image named myapp using the Dockerfile.

3. Run the Application
   
docker run --name myapp-container myapp

docker run --name myapp-tests-container myapp-tests

This command runs the Docker container named myapp-container, mounts the orders.csv file into the container, and executes the main.py script. The --name flag gives the container a name for easy reference.


### Stopping and Removing Containers

To stop and remove the containers after running them:

1. Remove the Application Container
   
docker rm myapp-container

This command removes the myapp-container after it has stopped.

3. Remove the Test Container
   
docker rm myapp-tests-container

This command removes the myapp-tests-container after it has stopped.
