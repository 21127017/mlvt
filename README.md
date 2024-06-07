# Multi-Language Video Translation

## Introduction
This project aims to facilitate multi-language video translation. Please follow the instructions below to perform the tasks correctly.

## Instructions

### 1. Folder Structure
Within the `models` directory, there are four folders corresponding to four different processes (referred to as "Process Folders"). Your task is to navigate to the folder corresponding to your work and add the model (if any).

- `1-S2T`: Convert video to text
- `2-T2T`: Translate text from one language to another
- `3-T2S`: Convert text to speech
- `4-Lipsing`: Sync lip movements with speech

### 2. Makefile
Write a `Makefile` in your Process Folder to run commands (refer to the `Makefile` in `3-T2S` for guidance).

### 3. Process Folder README
Write a `README` file in your Process Folder. This file can include:
- An introduction to the process
- Required libraries to run the process
- Reference models
- Any other relevant information

### 4. Data
This directory contains all the input and output information for the processes. This means that the inputs for the models must be taken from here (refer to `models/1-S2T/transcribe_video.py`). The folder naming convention should be `input/output_<process_name>`.

### 5. Commit
Please do not push directly to the `main` branch. Create a separate branch instead. Once you have pushed your changes, a designated team member responsible for merging will combine them into the `main` branch.

## Example
Refer to the `3-T2S` folder for an example of how to set up the `Makefile` and `README` file.

## Contact
For any questions or further assistance, please reach out to the project maintainers.
