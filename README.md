# MIR-2024-Project
<img src="./IMDB_Logo.jpeg" alt="IMDb Logo" width="100%" height="auto" />
This is the repository for Modern Information Retrieval Course, Instructed by Dr. Mahdieh Soleymani Baghshah at Sharif University of Technology.

## What is this project about?
One of the ways to compare movies and understand which one is a better choice for you, is through websites with this purpose and using appropriate information retrieval methods.

In this phase of project, we begin our journey towards building an information retrieval system for [IMDb](https://www.imdb.com/) website. In this phase, we crawl the required datas from [IMDb](https://www.imdb.com/) and do some preprocessing on them. [IMDb](https://www.imdb.com/) has one of the reachest datasets of movies (with their ratings, comments, actors and etc.).

## A note on forking this repository
You should make a **private** repository in your personal github account in order to push your answers and also, for TAs being able to track your work. Please choose `Use this Template` in this repository and choose `Create a new repository`. Make sure you make your repository **private**.

In order to be able to get the new changes and files from our main repository into your own repository, you should add this repository as a remote:
```bash
git remote add template [URL of the template repo]
```
and then, you can simply run `git fetch` to update the changes whenever you want:
```bash
git fetch --all
```

## General Structure
The project contains 2 main modules: [Logic](./Logic/README.md) and [UI](./UI/README.md). The `Logic` module is responsible for doing the main tasks of the project and the `UI` module is responsible for providing a user interface for the user to interact with the system. In each task, you will be told to implement a part or a whole file in one of these modules. Please read the comments for each file and functions inside it to understand what you need to do.

## Crawled Data
You can find _raw_ crawled data for IMDB movies (which you should've done in Phase 1) [here](https://drive.google.com/file/d/1Lq2zVJlN_B4kUAu4VafQ4jXMIQiAR9vI/view?usp=sharing).

## Contributions
Please create a new issue whenever you find a problem ir you had any suggestions regarding this project. Also, you can create PRs for issues with "student" label.