---
sidebar_position: 2
---

# Cloud IDE Kubernetes

This learning environment is called "Cloud IDE", it is Theia-based, offering functionalities like file/folder management, a terminal, and more. It operates on a Ubuntu foundation and is enabled for working with Docker and Kubernetes.

### Layout

#### Right side: 
The Cloud IDE development environment resides here, providing the tools for code development and execution.

#### Left side: 
This area is divided into two sections:
 - Tai's Chat Interface: This interface facilitates communication between the learner and Tai, featuring chat history, and learners' message input field.
 - Lab instructions: These instructions guide learners through the learning activities and exercises.

## Cloud IDE Features

Cloud IDE empowers learners with a comprehensive IDE experience, including:
 - File/folder management: Organize and manage files and folders efficiently.
 - Terminal: Execute commands and interact with the underlying operating system.
 - Docker and Kubernetes integration: The learner is provided both a Kubernetes namespace (with value `$SN_ICR_NAMESPACE`) and an ICR (IBM Container Registry) namespace (with the value `us.icr.io/$SN_ICR_NAMESPACE`) to store Docker images.

#### Skills Network Toolbox:

Within Cloud IDE, learners can access the Skills Network Toolbox by clicking the Skills Network Toolbox Icon button located on the left-hand side of the Cloud IDE menu bar. This toolbox offers a variety of tools to enhance the learning experience and facilitate completion of labs:

- Databases
  - MySQL
  - PostgreSQL
  - Cassandra
  - MongoDB
- Big Data
  - Apache Airflow
- Cloud
  - Code Engine
- Embeddable AI
  - Text-To-Speech
  - Speech-To-Text
  - Watson NLP
    - Sentiment Analysis (BERT and CNN)
    - Categories
    - Classification
    - Concepts
    - Detag
    - Emotion
    - Keywords
    - Lang-detect
    - Noun-phrases
    - Relations (Transformer)
    - Syntax
- Launch Application - This is how you view the application you run within Cloud IDE. Launch Application starts a proxy server that makes your local app accessible through the cloud IDE. You can run it with a built-in live server or with a framework-specific server (e.g., Flask, Express via npm)

  - How to use:

    - Start your server. (Note: If you used the built-in live server a notification with the port opened will appear)

    - Go to Skills Network Toolbox, and input the port.

    - Press "your application" to access the server within the cloud IDE, or open a new tab to access it from you browser
