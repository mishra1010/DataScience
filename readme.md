Install Anaconda

create new venv or work in base env
Open anaconda command prompt, cd to folder where all code files will be stored
type command
(base) C:\DataScience>jupyter lab

## Day1-Scenario explanation and Load Data
Introduction

Congratulations! You have just been hired as a Data Scientist Intern at CodeBook – The Social Media for Coders. This Delhi-based company is offering you a ₹10 LPA job if you successfully complete this 1-month internship. But before you get there, you must prove your skills using only Python—no pandas, NumPy, or fancy libraries!

Your manager Puneet Kumar has assigned you your first task: analyzing a data dump of CodeBook users using pure Python. Your job is to load and explore the data to understand its structure.

Task 1 - Load Data
- User Data
- Pages Data
- Connetions Data

Task 2 - Read and display data from data.json

----Output-----
Users and their connections

ID:1 - Amit is friends with [2, 3] and liked pages are [101]
ID:2 - Priya is friends with [1, 4] and liked pages are [102]
ID:3 - Rahul is friends with [1] and liked pages are [101, 103]
ID:4 - Sara is friends with [2] and liked pages are [104]

.....Pages Information....
101 : Python Developers
102 : Data Science Enthusiasts
103 : AI & ML Community
104 : Web Dev Hub

Next Exercise is - Data is not clean, so we need to clean and structure Data

## Day2- Cleaning and Structuring the Data

Introduction

Your manager is impressed with your progress but points out that the data is messy. Before we can analyze it effectively, we need to clean and structure the data properly.

Your task is to:

    Handle missing values
    Remove duplicate or inconsistent data
    Standardize the data format

Task 1  - Identify issues in Data

{
    "users": [
        {"id": 1, "name": "Amit", "friends": [2, 3], "liked_pages": [101]},
        {"id": 2, "name": "Priya", "friends": [1, 4], "liked_pages": [102]},
        {"id": 3, "name": "", "friends": [1], "liked_pages": [101, 103]},
        {"id": 4, "name": "Sara", "friends": [2, 2], "liked_pages": [104]},
        {"id": 5, "name": "Amit", "friends": [], "liked_pages": []}
    ],
    "pages": [
        {"id": 101, "name": "Python Developers"},
        {"id": 102, "name": "Data Science Enthusiasts"},
        {"id": 103, "name": "AI & ML Community"},
        {"id": 104, "name": "Web Dev Hub"},
        {"id": 104, "name": "Web Development"}
    ]
}

Problems:

    User ID 3 has an empty name.
    User ID 4 has a duplicate friend entry.
    User ID 5 has no connections or liked pages (inactive user).
    The pages list contains duplicate page IDs.

1. Remove empty names using strip function in list
2. Remove duplicate friend entry by using set and converting back to list
3. use for loop in list for checking no connection or liked pages using or condition, when both are false then the new list will not have the user id
4. Remove duplicate page ids by using dictionary key, values- key canbe id and values can be the full list and 
then make list with only dictionary values. key is always unique in dictionary

Next is find friends you may knor. This can be achieved by suggesting friends based on mutual connections.

## Day3 - Find People you may know

Finding "People You May Know"

Now that our data is cleaned and structured, your manager assigns you a new task: Build a 'People You May Know' feature!

In social networks, this feature helps users connect with others by suggesting friends based on mutual connections. Your job is to analyze mutual friends and recommend potential connections.

## Day4 - Finding pages you might like

Like finding people you might know, find pages you may like and recommend

import json
load data in form of json
find pages you might like
    create a dictionary to store user id and pages liked
    populate with data by running for loop
    find shared pages between users and other users
    suggest page not liked by an user with a score, if 2 user like a particular page and one of the users does not like a page which another user has liked, then suggest tat page with score 1, else 0
    Created sorted list with page and score for ids
    Display recommendations for a single userid

## Day5 - Why use numpy

Numpy - Numerical python library in python

python list are flixible and numerical operations are slow because they store elements as pointers instead of a continuous block of memory. Example - python lists can store numbers, strings, lists inside lists and more lists and hence it becomes slow because of giving these functionalities as all operations are performed element by element.

Numpy is a library which is written using a low-level C-optimized backend. C language is very close to hardware and hence faster than python. Speed is an issue with python when we scale. Ex - processing million rows takes long time for python

faster
uses less memory
supports vectorized operations (no loops)
Has built-in mathematical operations
contiguois memory, 2D array needs to be of same size, else gives errors
real difference is known with large data and with end-start times

## Day6 - Creating Numpy arrays

Arrays and properties
flatten,reshape, dtype,ndim,shape,size,arange,linspace,zeros,ones,full
np.array([1,2,3])

## Day7 - Indexing and slicing

index starts from 0
Slicing returns view and not copy, so any change in the slice will affect the original array. This helps in
Memory Efficiency - memory is saved as copy is not created and operations are faster
Performance - Enables faster access and manipulation of large datasets without duplicating data

use b=a[3:7].copy() to create a copy

fancy indexing and boolean masking

a = np.array([1,2,3,4,5,6,7,8])
idx = [0,3,6]
print(a[idx])

a[a>3] ------- gives elements greater than 3

## Day8 - Numpy Multidimensional indexing and Axis

    Multidimensional arrays

    Axis  - R, c and depth based on 1D, 2D and 3D

    np.sum(arr, axis=1)

    np.sum(arr, axis=0)

    arr[0][1] and arr[0,1] --- same

    arr[0:2, 1:3] #gives overlapping data
