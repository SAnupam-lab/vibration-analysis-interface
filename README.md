# vibration-analysis-interface

A full stack project for the analysis of vibration data using time and frequency techniques applied on public dataset signals.

## 1. Getting started

Before you start, here are some important points about this project.

### 1.1. Development tools used in this project

- FastAPI: backend.
- Docker: image containerization.
- Jenkins: CI/CD pipeline.

### 1.2. Vibration analysis techniques used in this project

- Statistical analysis (RMS, variance, peak-to-peak).
- Frequency-domain analysis (fast Fourier transform).

### 1.3. Downloading the vibration datasets

In order to obtain the datasets for testing the application, please access the following shared folder, download and paste the available folders into the directory "vibration-analisis-interface/app/datasets".

*https://drive.google.com/drive/folders/1nGa_2gpgtRKGYrosxdpbed2UQdmaI23q?usp=sharing*

## 2. Running the application

You can run this application through three different methods.

### 2.1. Running the application directly

- Navigate to the application folder.

        cd <local-path-to-the-repository>/app

- Create a virtual environment.

        python -m venv venv

- Activate the virtual environment.

        source venv/bin/activate

- Install the required packages.

        pip install -r requirements.txt

- Run tha main fille.

        python main.py

### 2.2. Running the application as a container

- Navigate to the project folder.

        cd <local-path-to-the-repository>
    
- Build the application image.

        docker build -t vai-image .

- Run the image in a container.

        docker run -d -p 8000:8000 --name vai-container vai-image

### 2.3. Running the application within a Jenkins CI/CD pipeline

- In your browser, access the address where your Jenkins  server is running.
    
- After logging in, click on "New Item" at the left bar.

- Type a name for your project, select the option "Pipeline", and then click "OK".

- In the section "Build Trigger" of the pipeline configuration, select the option "Poll SCM", and type * * * * * in the scheduling field. This means that Jenkins will check for updates on Git repository every minute.

- In the section "Pipeline", select "Pipeline script from SCM".

- In the subsection "SCM", select "Git", and then provide your git credentials.

- Don'tt forget to specify the branch you are using for your project in the subsection "Branches to build".

- Click on "Save" to confirm your pipeline.

 