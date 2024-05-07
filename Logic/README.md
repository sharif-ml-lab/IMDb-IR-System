
# Logic Module
This module contains files and classes responsible for doing the main tasks of the project. The explanations of each class and what it does is provided below (and will be completed as the project goes on).

**Attention:**
Inputs, outputs and logic of each function is explained in the comments of each function. So, **Please read** the comments and the docstrings of each class and method to understand the logic and the requirements of each part.

## 1. [Crawler](./core/utility/crawler.py)

In the beginning, we need to crawl our required data and create a dataset for our needs. For this sake, we implement a [crawler](./core/crawler.py). The structure and functions required for this part, are explained in the `crawler.py` file.

For **Testing** the correctness of your implementation for crawler part, you can run `tests/test_crawler.py` and see if you crawled correctly. Feel free to change `json_file_path` variable to meet the path of your crawled data.

## 2. [Near-duplicate page detecion](./core/indexer/LSH.py)
We provided you `MinHashLSH` class. This class is responsible for doing near duplicate detection. As you know, this section consists of 3 sub-sections. First, you need to shingle documents. Then, after characteristic matrix, using mini-hashing technique, improve near duplicate detection. Finally, you need to use LSH so that you can find movies that are suspicious to being duplicate. **Note** that you are only allowed to use `perform_lsh` function outside of your class and other methods only inside the class. **Another Note** is that in your crawled data, you have one section named `first_page_summary` and another section named `summaries`. The first one is a String and the second one is a list of Strings and note that you should work with the second one and by combining those Strings make a summary of the movie and do LSH on the set of summaries. The final output of this class should be a dictionary where the keys are the hashes of the buckets, and the corresponding values should be lists of document IDs, representing the indices of those summaries in the main list of all summaries. We have provided you with a file containing some fake movies in JSON format. Specifically for the Locality-Sensitive Hashing (LSH) part, please integrate this additional data into your main dataset and proceed with LSH. It's important to note that the file includes 20 movies, and each pair of consecutive movies is considered a near duplicate. For instance, the first and second movies, the third and fourth movies, and so on, are near duplicates. Verify your code to account for this characteristic. However, it is crucial to emphasize that after this stage, you must remove all fake movies from your corpus and refrain from utilizing them in further steps. There is a method in the class called `jaccard_similarity_test`. You can assess your results using this method by passing the bucket dictionary and the documents containing all the summaries, where the indexes correspond to the summaries in the buckets.

## 3. [Preprocess](./core/utility/preprocess.py)
This class is responsible for doing preprocessings required on the input data. The input the crawled data and the output is the data without extra info.

Using prebuilt libraries for stopwords is an option, but it can be slow to process large amounts of text. For faster performance, we have prepared a `stopword.txt` file containing common stopwords that you can use instead. The stopwords file allows preprocessing to be completed more efficiently by removing common, non-informative words from the text before further analysis.

## 4. [Indexing](./core/indexer/index.py)
This class is responsible for building index. Its input is preprocessed data and the output is indexes required for searching. This section will be used in next phases and the functions will be used for information retrieval.

- `check_add_remove_is_correct` method is used to test if your add and remove methods are correct or not. You should run this method and see if your add and remove methods are correct.
Run it and **report** the results to us.
- `check_if_index_loaded_correctly` method is used to test if your index is loaded correctly or not. You should run this method and see if your index is loaded correctly.
Run it and **report** the results to us.
- `check_if_indexing_is_good` method is used to test your indexing, and you can call it to understand how well your indexing is.
You should run this method, **for each of the 4 indexing methods and for 2 different words** and compare if your indexing is better or not.
Report the results to us.

- **Note** that one or many of the methods (or signatures of methods) in this class may need to be changed based on your implementations. Feel free to do so!

## 5. [Search](./core/search.py)
in this part you have to work on implementing the search feature, which is the most important part of the retrieval process. To accomplish this, you need to create search functions and a scorer that will score each document based on the input query. Keep in mind that you may need to index additional information that was not previously indexed. Make sure to carefully review the structures and functions documentation of the added files.

## 6. [Spell Correction](./core/utility/spell_correction.py)
In this file, you have a class for the spell correction task. You must implement the shingling and Jaccard similarity approach for this task, aiming to correct misspelled words in the query. Additionally, integrate the Term Frequency (TF) of the token into your candidate selection. For instance, if you input `whle`, both `while` and `whale` should be considered as candidates with the same score. However, it is more likely that the user intended to enter `while`. Therefore, enhance your spell correction module by adding a normalized TF score. Achieve this by dividing the TF of the top 5 candidates by the maximum TF of the top 5 candidates and multiplying this normalized TF by the Jaccard score. In the UI component of your project, present these probable corrections to the user in case there are any mistakes in the query.

## 7. [Snippet](./core/utility/snippet.py)
In the snippet module, extract a good summary from the document. To achieve this, focus on non-stop word tokens from the query. For each token, locate the token or its variations in the document. Display "n" tokens before and after each occurrence of the token in the document. Merge these windows with '...' to create the snippet. Also put query tokens in the summary inside three stars without any space between stars and the word inside them; for example if token2 is present in the query, the returned snippet should be like "token1 \*\*\*token2\*\*\* token3". But you should find these windows carefully, for example if you have token1 in the doc in 2 places and 3 tokens before the second token1, is token2 of the query, you must consider the second window instead of the first one. Additionally, identify tokens in the query that are absent in the document and return them.

## 8. [Utils](./utils.py)

This file contains functions that is needed by UI to do some of the important functionalities. For now, you should complete the `clean_text` function that is used by UI to do the pre-processing operations that you implemented in `Preprocessor` class, on the input query by user.  You can **test** your implementation by running the UI, and giving different inputs and see that how is it being corrected (or actually, being cleaned! so it can be used better as we proceed in the project).

## 9. [Evaluation](./core/utility/evaluation.py)
This file contains code to evaluate the performance of an information retrieval or ranking system. There are several common evaluation metrics that can be implemented to systematically score a system's ability to retrieve and rank relevant results. The metrics calculated here are `precision`, `recall`, `F1 score`, `mean average precision (MAP)`, `normalized discounted cumulative gain (NDCG)`, and `mean reciprocal rank (MRR)`.

Each metric makes use of the actual relevant items and the predicted ranking to calculate an overall score. A higher score indicates better performance for that particular aspect of retrieval or ranking.

 - Precision measures the percentage of predicted items that are relevant.
 - Recall measures the percentage of relevant items that were correctly predicted.
 - The F1 score combines precision and recall into a single measure.
- MAP considers the rank of the relevant items, rewarding systems that rank relevant documents higher.
- NDCG applies greater weight to hits at the top of the ranking.
- MRR looks at the position of the first relevant document in the predicted list.

Together, these metrics provide a more complete picture of how well the system is able to accurately retrieve and highly rank relevant information.

## 10. [Scorer](./core/utility/scorer.py)
Please refer to the docstrings in the `scorer.py` for complete explanation of each functionality and what you should complete.

# Phase 2

## 1. Extending [Search](./core/search.py)

In this section, you should implement the `find_scores_with_unigram_model` function in the `Search` class, where it is responsible for finding document scores based on the Unigram Model. You can use the new prototype functions that we have added to [Scorer](./core/utility/scorer.py) to calculate these scores.

## 2. Extending [Scorer](./core/utility/scorer.py)

In this section, you should implement the `compute_scores_with_unigram_model` and `compute_score_with_unigram_model` functions in the `Scorer` class. These functions are responsible for creating document scores based on the unigram model to be used in [Search](./core/search.py) and computing the best match documents for a given query.

## 3. [Link Analysis](./core/link_analysis/analyzer.py)

This section involves analyzing the link between actors and movies using the Hits algorithm, and thereafter determining which actors and movies received the most scores based on the algorithm. We do this step-by-step in the `analyzer.py`. The first step is to initialize the parameters of your link analyzer, such as the list of hubs and authorities and the links graph from the given root set. You may need preprocessing for this, so you can pass these to the `initiate_params` function and call it in your code. Graphs derived from the root set can be expanded before the Hits algorithm is run. For this purpose, `expand_graph` is defined. You can read the link analysis slide for a better understanding. At the end, run the algorithm by calling the `hits` function and output ten actors and movies with the highest scores.

**Note**: To implement the Hits algorithm, you need to implement a graph. For this, you can get help from the `LinkGraph` class in the `graph.py`. In this class, a template is placed for your implementation. You are free to modify this class in any way you like.

## 4. [Word Embedding](./core/word_embedding/README.md)
Please refer to the specific [Readme file](./core/word_embedding/README.md) for the explanation of the word embedding part.

## 5. [Classification](./core/classification/README.md)
Please refer to the specific [Readme file](./core/classification/README.md) for the explanation of the classification part.

## 6. [Clustering](./core/clustering/README.md)
Please refer to the specific [Readme file](./core/clustering/README.md) for the explanation of the clustering part.