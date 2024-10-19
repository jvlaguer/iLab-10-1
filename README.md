# Visual Question Answering (VQA) System for Medical Images

## Project Description

Visual Question Answering (VQA) for medical images is an advanced task in the field of medical imaging and artificial intelligence. This project aims to bridge the gap between image recognition and medical knowledge, enabling machines to comprehend and interpret the content of medical images (such as X-rays, MRIs, and CT scans) and subsequently answer questions posed in natural language based on that content. The goal is to develop a VQA system specifically designed for medical images to aid healthcare professionals in medical diagnosis and patient care.

## Link & Folder Sturcture

This contains zip file contaning RoBERTa and BLIP. Due to low accuracy of LLAMA in genartaing captions, it's being only used for verfying if image is Radiology or not. Link: https://drive.google.com/file/d/1urZJKEJ3NrxUobV7ExvUVokt3j8pem58/view?usp=share_link

Folder Structer should be like:<br>

<b>VQA</b><br>
|- models (folder)<br>
||- blip_finetuned_model<br>
||- model_roco.keras<br>
||- vqa_model_roberta_finetuned.keras<br>
|- features (folder)<br>
||- features_roco.pkl <br>
|- BLIP.ipynb <br>
|- Integration.ipynb <br>
|- llama.ipynb <br>
|- RoBERTa.ipynb <br>
|- image.jpg <br>



## Team Members

- Anjali Kushabrao Ledade
- Dikshya Tamling Limbu
- Hemang Sharma
- John Victor Laguer
- Molly Dignan
- Rusan Vaidya

## Table of Contents

- [Objectives](#objectives)
- [Key Components](#keyComponents)
- [Datasets](#datasets)

## Objectives

The main objectives of this project are:

- **Image Analysis**: Utilize convolutional neural networks (CNNs) or other state-of-the-art deep learning models to extract visual features from medical images.
- **Question Processing**: Employ natural language processing (NLP) techniques to parse and understand the questions posed about the medical images.
- **Multimodal Fusion**: Integrate visual features from the medical image with the processed question to create a unified representation. This fusion can be achieved through various techniques, such as attention mechanisms or joint embedding spaces, to align visual and textual information effectively.
- **Answer Generation**: Develop a model to generate accurate and relevant answers based on the combined understanding of the medical image and the question. This could involve sequence-to-sequence models, transformer-based architectures, or other advanced deep learning techniques tailored for medical contexts.

## Key Components

1. **Image Analysis**
   - Utilize CNNs or other deep learning models.
   - Extract visual features from medical images.

2. **Question Processing**
   - Use NLP techniques to understand and parse the questions.

3. **Multimodal Fusion**
   - Combine visual features with textual information.
   - Use techniques such as attention mechanisms or joint embedding spaces.

4. **Answer Generation**
   - Generate accurate and relevant answers.
   - Implement advanced deep learning techniques suitable for medical contexts.


## Datasets

We will be using the following datasets for training and evaluation:

- [SLAKE](https://huggingface.co/datasets/BoKelvin/SLAKE)
- [VQA-RAD](https://huggingface.co/datasets/flaviagiammarino/vqa-rad)
- [PathVQA](https://paperswithcode.com/dataset/pathvqa)

