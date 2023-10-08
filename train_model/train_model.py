import cv2
import os
import numpy as np
import csv

# Define the paths to the training dataset
train_data_dir = 'train_model/train_data'

def train_face_recognition_model(algorithm='LBPH'):
    # Initialize face recognition model based on the specified algorithm
    if algorithm == 'LBPH':
        face_recognizer = cv2.face_LBPHFaceRecognizer.create()
    elif algorithm == 'Eigen':
        face_recognizer = cv2.face_EigenFaceRecognizer.create()
    elif algorithm == 'Fisher':
        face_recognizer = cv2.face_FisherFaceRecognizer.create()
    else:
        raise ValueError("Invalid algorithm specified")

    faces = []
    labels = []

    # Create a dictionary to map label (numeric) to person's name
    label_to_name = {}

    # TODO
    # Load training data
    # Walk through each sub-folder
    # Assume each sub-folder is a different person
    # Append each image to the training set
    # Append the corresponding label to the labels list
    # Add the person's name to the label-to-name dictionary using the label as the key
    # Your code goes here

    # Train the face recognition model

    # Save the trained model to a .xml file in the app/trained_models folder
    # The name of the file should be according to example presented in docs

    # Save label-to-name mapping to a CSV file

    # TODO
    # Print a summary of the training
    print(f'Training complete. Number of users trained: {len(set(labels))}')

if __name__ == '__main__':
    # Specify the algorithm ('LBPH', 'Eigen', or 'Fisher')
    selected_algorithm = 'LBPH'
    train_face_recognition_model(selected_algorithm)
