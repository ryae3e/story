
# Personal Journaling Application

## Brief Roadmap
1. **Backend Development**
   - Set up Flask App and folder structure
   - Create API Endpoints: upload, list, retrieve, delete files, and run transcription script
   - Integrate `meet.py` script for transcription
   - Set up Celery for asynchronous tasks
   - Implement token-based authentication
2. **Frontend Development**
   - Set up Vue.js for reactive interfaces
   - Implement calendar view and individual date pages
   - Develop features for transcription and interaction with text files
   - Create a dashboard for metrics and trends
3. **Testing and Debugging**
4. **User Documentation**
5. **Future Implementations**
   - Voice Recognition
   - Sentiment Analysis
   - Advanced Data Visualization
   - Notifications/Reminders
   - Machine Learning Insights

## Overview of the Project Framework
The application is built around a Flask backend and Vue.js frontend. The Flask backend manages API endpoints, file storage, transcription, and authentication. Vue.js is used for creating a user-friendly interface with features like calendar view, date navigation, and dashboard. The application also uses Celery for handling asynchronous tasks and integrates a `meet.py` script for audio transcription using OpenAI Whisper.

## Description of File Structure
- **app.py**: Main Flask app file
- **/templates**: Folder for HTML templates
- **/static**: Folder for JS, CSS, and other static files
- **/audio**: Store uploaded audio categorized by date
- **/text**: Store transcribed text files categorized by date
- **meet.py**: CLI tool to transcribe audio to text
- **/celery_worker**: Folder containing Celery worker files
- **Dockerfile**: Docker configuration file
- **docker-compose.yml**: Docker Compose configuration file
- **requirements-dev.txt**: List of dependencies

## Detailed Instruction Set for Development
1. **Set up the Environment**
   - Install Python, Docker, Node.js, and Vue.js CLI
   - Clone the repository and navigate to the project folder
   - Build the Docker image and run the container
2. **Backend Development**
   - Implement API endpoints in `app.py`
   - Integrate `meet.py` script for transcription
   - Set up Celery for handling asynchronous tasks
   - Implement token-based authentication using Flask-HTTPAuth
3. **Frontend Development**
   - Initialize Vue.js project in the `/static` folder
   - Develop Vue components for calendar view, date pages, and dashboard
   - Connect frontend to Flask API endpoints
   - Implement features for file upload, transcription, and interaction with text files
4. **Testing and Debugging**
   - Test each component and API endpoint
   - Debug any issues and verify the functionality of the application
5. **Deployment**
   - Deploy the application on a local server or a cloud platform of your choice
6. **Future Enhancements**
   - Plan and integrate additional features like voice recognition, sentiment analysis, advanced data visualization, notifications/reminders, and machine learning insights as per the roadmap.

Note: This is a personal project, and while the initial build focuses on core functionalities, it is designed to be extensible for future dynamic features.
