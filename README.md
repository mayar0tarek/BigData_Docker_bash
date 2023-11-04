# BigData_Docker_bash
This repository contains the code and instructions for data processing and analysis using Dockerfile
Setup
Start by creating a directory on your local machine named bd-a1/.
Download and place the dataset of your choice in the bd-a1/ directory.
Inside the bd-a1/ directory, create a Dockerfile.
Specify the base image as Ubuntu in the Dockerfile.
 
Docker Container setup
Install the following packages in the Dockerfile:
Python3
Pandas
Numpy
Seaborn
Matplotlib
scikit-learn
Scipy
Docker

Create a directory inside the container.
Move the dataset file to the container.
Open the bash shell upon container startup.


Python Files
Within the container's doc-bd-a1/ directory, create the following Python files:
load.py: Design this file to dynamically read the dataset file by accepting the file path as a user-provided argument.
dpre.py: This file should perform Data Cleaning, Data Transformation, Data Reduction, and Data Discretization steps. In each step, apply a minimum of 2 tasks. Save the resulting data frame as a new CSV file named res_dpre.csv.
eda.py: Conduct exploratory data analysis, generating at least 3 insights without visualizations. Save these insights as text files named eda-in-1.txt, and so on.
vis.py: Create a single visualization and save it as vis.png.
model.py: Implement the K-means algorithm on your data frame with the columns you deem suitable for K-means, setting k=3. Save the number of records in each cluster as a text file named k.txt.

Bash Script
Create a bash script named final.sh to:
Copy the output files generated by dpre.py, eda.py, vis.py, and model.py from the container to your local machine in bd-a1/service-result/.
Close the container.
 
Execution Steps
To execute your project, perform the following steps:
After creating the Dockerfile, build it to produce an image.
Run the image (bd-a1-image).
Inside the image, run Python as specified.
Initiate the pipeline using the command: python3 load.py <dataset-path>.
The pipeline will generate several files and figures, conforming to the prescribed outputs.
Outside the image, run the bash file to print the output of the python files and add them to the local machines (your PC).
Execute the bash script to halt/stop the container.
 
Notes
Each Python file responsible for updating the data frame should invoke the next Python file and transmit the data frame path to it. Subsequently, read the CSV file as a data frame and continue processing.
 
 
