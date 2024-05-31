# Movie Genre Prediction using BERT

This module aims to predict the genre of movies based on their first page summary using a fine-tuned BERT model.

## Steps

1. **Load the Dataset**
   - Load the movie dataset containing the first page summary and genre information.

2. **Analyze Genre Distribution**
   - Get the distribution of each genre in the dataset.
   - Identify the top 5 most common genres.
   - Remove or group other entries into the top 5 genres if they are similar.
   
4. **Split Dataset**
   - Split the dataset into train, validation, and test sets with a ratio of 80:10:10.

5. **Fine-tune BERT Model**
   - Fine-tune a pre-trained BERT model on the training data, using the first page summary as input and the genre as the target variable.
   - Use appropriate hyperparameters and techniques for fine-tuning.

6. **Evaluate Model**
   - Evaluate the fine-tuned BERT model on the test set.
   - Report relevant metrics for classification, such as accuracy, precision, recall, and F1-score.

7. **Save Model**
   - Save the fine-tuned BERT model to the Hugging Face Model Hub for easy access and sharing.

