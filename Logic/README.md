
# Logic Module
This module contains files and classes responsible for doing the main tasks of the project. The explanations of each class and what it does is provided below (and will be completed as the project goes on).

**Attention:**
Inputs, outputs and logic of each function is explained in the comments of each function. So, **Please read** the comments and the docstrings of each class and method to understand the logic and the requirements of each part.

## Installing dependencies
It is recommended that you make a virtual environment and install the required packages in it. To do so, you can run the following commands:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 1. [Crawler](https://github.com/sharif-ml-lab/IMDb-IR-System/blob/main/Logic/core/crawler.py)

In the beginning, we need to crawl our required data and create a dataset for our needs. For this sake, we implement a [crawler](https://github.com/sharif-ml-lab/MIR-2024-Project/blob/Phase_1/Logic/part%201/crawler.py). The structure and functions required for this part, are explained in the `crawler.py` file.

For **Testing** the correctness of your implementation for crawler part, you can run `tests/test_crawler.py` and see if you crawled correctly. Feel free to change `json_file_path` variable to meet the path of your crawled data.

## 2. [Near-duplicate page detecion](https://github.com/sharif-ml-lab/IMDb-IR-System/blob/main/Logic/core/LSH.py)
We provided you `MinHashLSH` class. This class is responsible for doing near duplicate detection. As you know, this section consists of 3 sub-sections. First, you need to shingle documents. Then, after characteristic matrix, using mini-hashing technique, improve near duplicate detection. Finally, you need to use LSH so that you can find movies that are suspicious to being duplicate. **Note** that you are only allowed to use `perform_lsh` function outside of your class and other methods only inside the class. **Another Note** is that in your crawled data, you have one section named `first_page_summary` and another section named `summaries`. The first one is a String and the second one is a list of Strings and note that you should work with with the second one and by combining those Strings make a summary of the movie and do LSH on the set of summaries.

## 3. [Preprocess](https://github.com/sharif-ml-lab/IMDb-IR-System/blob/main/Logic/core/preprocess.py)
This class is responsible for doing preprocessings required on the input data. The input the crawled data and the output is the data without extra info.

## 4. [Indexing](https://github.com/sharif-ml-lab/IMDb-IR-System/blob/main/Logic/core/index.py)
This class is responsible for building index. Its input is preprocessed data and the output is indexes required for searching. This section will be used in next phases and the functions will be used for information retrieval.

- `check_add_remove_is_correct` method is used to test if your add and remove methods are correct or not. You should run this method and see if your add and remove methods are correct.
Run it and **report** the results to us.
- `check_if_index_loaded_correctly` method is used to test if your index is loaded correctly or not. You should run this method and see if your index is loaded correctly.
Run it and **report** the results to us.
- `check_if_indexing_is_good` method is used to test your indexing, and you can call it to understand how well your indexing is.
You should run this method, **for each of the 4 indexing methods and for 2 different words** and compare if your indexing is better or not.
Report the results to us.

- **Note** that one or many of the methods (or signatures of methods) in this class may need to be changed based on your implementations. Feel free to do so!
