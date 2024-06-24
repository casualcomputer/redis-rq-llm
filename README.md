
# FastAPI LLM Server with Redis-RQ Task Queue

## Overview

This project utilizes FastAPI to serve a Language Learning Model (LLM) capable of answering philosophical questions. The setup involves multiple components working together to manage requests and process them efficiently using Redis and RQ for task queuing.

## Components

- `fastapi_app.py`: Tests the LLM in isolation and ensures the API and GPU configurations are correctly set up.
- `ask_questions.py`: Tests the API's ability to handle incoming requests by sending 100 philosophical questions sequentially and logging responses.
- `app.py`: Integrates Redis into the FastAPI setup, routing incoming requests through a Redis queue to manage them more efficiently.
- `worker.py`: Handles processing of queued requests using Redis-RQ, ensuring efficient management of system resources and preventing VRAM overflow or crashes.

## System Configuration and Current Issues

### System Setup

The server runs on **Windows 11** using **Windows Subsystem for Linux (WSL)**. This setup allows for a Linux environment on Windows to host the Redis server and manage RQ worker processes efficiently.

### Current Challenges

With the primary components tested and verified individually, the focus shifts to integrating `app.py` and `worker.py` to ensure that tasks are queued and processed without errors. The next steps involve:

1. Ensuring `app.py` correctly queues incoming requests to Redis.
2. Confirming `worker.py` processes these requests reliably without causing internal server errors or resource management issues.

### Error Investigation and Monitoring

To address potential errors during integration:
- **Logs Review**: Regularly check server and worker logs for error messages or unusual activity.
- **Resource Monitoring**: Keep an eye on GPU and other system resources to identify potential bottlenecks or failures.

## Goal and Testing

The immediate goal is to deploy `app.py` and `worker.py` in a test environment to evaluate the full system's functionality. This includes:
- Testing how the system handles multiple simultaneous requests.
- Monitoring resource usage to ensure there are no overflows or crashes.

## Future Directions

Upon successful integration and robust testing, plans include scaling the system, enhancing error handling, and potentially integrating more advanced machine learning models to handle a broader range of queries and increase throughput.

---

## Setup and Running Instructions

Ensure that the Redis server is operational before starting the application:

1. **Start the FastAPI Server (`app.py`):**
   ```bash
   python app.py
   ```

2. **Run the Redis-RQ Worker (`worker.py`):**
   ```bash
   python worker.py
   ```

3. **Execute the Testing Script (`ask_questions.py`):**
   ```bash
   python ask_questions.py
   ```
