# NLP-Abbreviation-Detection
## Overview
The focus of this project is sequence classification/labelling, a crucial task in natural language processing (NLP) that involves predicting class labels for sequences of observations. This has wide-ranging applications, from healthcare monitoring to error recognition in machine translation. Specifically, this project deals with detecting abbreviations (labelled as AC) and their corresponding long forms (labelled as LF) using the BIO (Beginning, Inside, Outside) labelling schema.

## Experimentation and Findings
The experimentation phase involved various NLP techniques and models, with a significant emphasis on fine-tuning pre-trained language models. The key steps included:

1. Data Analysis and Visualization: Understanding the dataset through visualizations and statistical analysis.
2. Experimental Setups:
- Data preprocessing techniques such as tokenization.
- Comparing different NLP algorithms (BiLSTM, SVM, RNN, CRF).
- Evaluating text encoding methods (e.g., TF-IDF, word2vec).
- Hyperparameter tuning and loss function optimization of LLM's (RoBERTa, BERT, ALBERT)
  
3.Evaluation: Models were assessed using the F1-score, confusion matrices, and error analysis to determine their effectiveness.

## Best Performing Model
From our findings and observations, it can be concluded that fine-tuning large language models (LLMs) such as RoBERTa yields the best performance for our application. These models demonstrated superior performance in sequence classification tasks due to their ability to leverage pre-trained knowledge and adapt to specific datasets through fine-tuning. The advantages of using RoBERTa included improved accuracy and robustness in identifying and labelling abbreviations and long forms.

## Deployment
The current architecture is effective as a small-scale proof of concept. Using Flask as a general-purpose framework facilitated simple development and offers flexibility for future scaling. However, frameworks like Django could be considered if the application grows in complexity and size.

## Build Instructions
Our service implementation is hosted using Docker, ensuring consistent execution across different environments. The Dockerfile in our repository defines all necessary dependencies, execution commands, and environment configurations. Here's an overview of the build process:

- Base Image: We use python:PYTHON_VERSION-slim, which contains Python and a minimal Linux distribution.
- Environment Variables: Set PYTHONDONTWRITEBYTECODE and PYTHONUNBUFFERED to prevent Python from writing bytecode files and buffering standard outputs.
- Dependencies: Install dependencies from requirements.txt using pip install -r requirements.txt.
- Port Configuration: Port 8000 is defined for application access.
- Execution: The application is run using Gunicorn, binding to the Flask application.

## Continuous Integration and Deployment (CI/CD)
Our CI/CD process ensures that code changes are automatically tested and integrated into the shared repository. The deploy.sh script simplifies the deployment workflow:

- Updating the Service: Pulls the latest version of the service repository from GitHub.
- Stopping Existing Containers: Stops any running Docker services to maintain data integrity.
- Rebuilding and Restarting: Uses docker-compose up --build to rebuild and restart the Docker containers.
- This manual script provides additional control and flexibility, acting as a fail-safe against problematic code and offering immediate feedback on deployment success.

## Monitoring
User inputs and model outputs are recorded in a CSV file, which includes timestamps for each request. This lightweight solution simplifies monitoring and data analysis without the need for complex relational database setups. The data is accessible and easy to understand, promoting transparency and facilitating quick insights into service performance.

## Conclusion and Future Works
The current architecture, leveraging Flask for development and Docker for deployment, proves suitable for a small-scale proof of concept. Fine-tuning LLMs such as RoBERTa has shown the best results in our context. As we consider future growth, exploring more robust frameworks like Django could provide enhanced scalability and feature richness.
