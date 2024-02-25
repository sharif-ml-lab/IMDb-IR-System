
# Phase 1
One of the ways to compare movies and understand which one is a better choice for you, is through websites with this purpose and using appropriate information retrieval methods.

In this phase of project, we begin our journey towards building an information retrieval system for [IMDb](https://www.imdb.com/) website. In this phase, we crawl the required datas from [IMDb](https://www.imdb.com/) and do some preprocessing on them. [IMDb](https://www.imdb.com/) has one of the reachest datasets of movies (with their ratings, comments, actors and etc.).

This phase will be in 2 parts. First, you need to only implement the parts that are mentioned in **Part1**. Then the second part and required data will be given to you.

**Attention:**
Inputs, outputs and logic of each function is explained in the comments of each function.

# Part 1
This part is consisting of 4 sub-parts.

## 1. [Crawler](https://github.com/sharif-ml-lab/MIR-2024-Project/blob/Phase_1/Logic/part%201/crawler.py)

In the beginning, we need to crawl our required data and create a dataset for our needs. For this sake, we implement a [crawler](https://github.com/sharif-ml-lab/MIR-2024-Project/blob/Phase_1/Logic/part%201/crawler.py). The structure and functions required for this part, are explained in the `crawler.py` file.

For **Testing** the correctness of your implementation for crawler part, you can run `tests/test_crawler.py` and see if you crawled correctly. Feel free to change `json_file_path` variable to meet the path of your crawled data.

## 2. [Near-duplicate page detecion](https://github.com/sharif-ml-lab/MIR-2024-Project/blob/Phase_1/Logic/part%201/LSH.py)
We provided you `MinHashLSH` class. This class is responsible for doing near duplicate detection. As you know, this section consists of 3 sub-sections. First, you need to shingle documents. Then, after characteristic matrix, using mini-hashing technique, improve near duplicate detection. Finally, you need to use LSH so that you can find movies that are suspicious to being duplicate. **Note** that you are only allowed to use `perform_lsh` function outside of your class and other methods only inside the class. **Another Note** is that in your crawled data, you have one section named `first_page_summary` and another section named `summaries`. The first one is a String and the second one is a list of Strings and note that you should work with with the second one and by combining those Strings make a summary of the movie and do LSH on the set of summaries.

## 3. [Preprocess](https://github.com/sharif-ml-lab/MIR-2024-Project/blob/Phase_1/Logic/part%201/preprocess.py)
This class is responsible for doing preprocessings required on the input data. The input the crawled data and the output is the data without extra info.

## 4. [Indexing](https://github.com/sharif-ml-lab/MIR-2024-Project/blob/Phase_1/Logic/part%201/index.py)
This class is responsile for building index. Its input is preprocessed data and the output is indices required for searching. This section will be used in next phases and the functions will be used for information retrieval.
**Note** that in this class, `check_if_indexing_is_good` method is used to test your indexing and you can call it to understand how well your indexing is.

- You should run this method, for each of the 4 indexing methods and for 2 different words and compare if your indexing is better or not.
- **Note** that one or many of the methods (or signatures of methods) in this class may need to be changed based on your implementations. Feel free to do so!

# Part 2
