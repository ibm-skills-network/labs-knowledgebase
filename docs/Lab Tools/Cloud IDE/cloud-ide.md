---
sidebar_position: 4
---

# Cloud IDE

Cloud IDE is an online integrated development environment that closely mimics Visual Studio Code (VS Code). It offers users a familiar interface and functionality, making it accessible to those already comfortable with VS Code. This cloud-based platform supports VS Code plugins and provides a comprehensive set of development tools. Users can access their development environment from any location, eliminating the need for local installation. Cloud IDE is designed as a learning environment, but the skills and familiarity gained here are directly transferable to Visual Studio Code. This design ensures that learners can easily transition from educational projects to professional development work, bridging the gap between learning and real-world application in the software development industry.

## Working Directory

The base directory for all learner projects is ```/home/project```. All files and folders created during lab exercises will be stored in this directory by default.

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

## Skills Network Toolbox:

Within Cloud IDE, learners can access the Skills Network Toolbox by clicking the Skills Network Toolbox Icon button located on the left-hand side of the Cloud IDE menu bar. This toolbox offers a variety of tools to enhance the learning experience and facilitate completion of labs:

- Databases
  - MySQL
  - PostgreSQL
  - Cassandra
  - MongoDB
- Big Data
  - Apache Airflow
- Cloud
  - [Code Engine](./Code-Engine.md)
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
- Launch Application - This is how you view the application you run within Cloud IDE. 

#### Viewing your running Applications

As part of your lab, you may start a web server that accepts traffic to:

- **Preview static sites or front-end projects:**
  Viewing your HTML/CSS/JS projects with live-server.

- **Integration testing:**
  Test APIs or webhooks from apps running inside the IDE. For example, if your backend server runs in the IDE, you can point Postman or a front-end app to the proxied URL.

- **Cross-browser testing:**
  Access the proxied app from different browsers on the same machine or on a device that can reach the proxy URL, to test responsiveness and behavior.

After you've done this, you can use the launch application button to view your application.

#### How to use:

1. **Start your server**
   - If you use the built-in live server, a notification will display the port that was opened.

2. Go to **Skills Network Toolbox**, access **"Launch Application"** tool and input the port.

3. **Access your application:**
   - Click the **"Your Application"** button to open the server inside the Cloud IDE, or
   - Open it in a new browser tab.

---

## DISCLAIMER

  - If the user is inactive for an hour, the session will be deleted
  - After 12 hours the session will be deleted, even if the user is active