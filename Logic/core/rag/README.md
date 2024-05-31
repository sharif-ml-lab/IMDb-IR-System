# Movie Retriever using RAG

This module uses LLM and Sentence Transformers (trained for better sentence similarity tasks) to design a conversational movie retrieval system using RAG.

## Steps

1. **Load and Preprocess the dataset**
   - Load the movie dataset containing the first page summary and genre information in json format and save it in CSV format.

2. **Vectorize the dataset**
   - Load the dataset using `CSVLoader`.
   - Vectorize the documents using a vectorizer.
   - Save the vectors in a vector database that supports fast approximate K nearest neighbors query like `FAISS`.
   
4. **Load Large Language Model**
   - Load a 4 bit quantized version of a small LLM (<7b parameters) and write the text generation pipeline.

5. **Design query chain**
   - Query chain is initialized with a prompt to extract a search query from the given conversation using the LLM.
   - Connect the query chain with the retriever from the vector database.

6. **Design context chain**
   - This chain gets the selected movies output from the query chain and generates the movie suggestion.

7. **Chat**
   - Connect everything together using `Conversation` class and chat with the final result to get movies suggestions.
