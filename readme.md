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

# Selecting Data along Axes
first_rows = arr3D[:,0,:] #Get first row from each sheet in a 3D array
print(first_rows)

arr3D
array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]]])

output
[[1 2 3]
 [7 8 9]]

 # changing data along an Axis

arr3D[:,0,:] = 0

array([[[ 0,  0,  0],
        [ 4,  5,  6]],

       [[ 0,  0,  0],
        [10, 11, 12]]])

2D - arr[row, col]
3D - arr[depth, row, col]
slicing allows extracting subarrays
Operations along axes help efficiently manipulate data without loops

## Day9 - Data types in Numpy

arr = np.array([23,4,3,32]) - 16 bytes

arr2 = np.array([23,4,3,32,1])
arr2.nbytes # each number is 4 bytes and hence 5 elements *4 bytes= 20 bytes or int64 will make it 8 bytes each
20 bytes

Strings
#Numpy is mainly used for numbers and so using strings is not a great idea
arr3 = np.array(['a','b'], dtype='U10' or 'str')

Complex Numbers (real part, imaginary part)
arr = np.array([1+2j, 3+4j, 5+6j])

arr = np.array([1+2j, 3+4j, 5+6j], dtype='complex128')
print(arr)

Dictionary - object Data type (not a great idea to use it as it will impact performance)

arr = np.array([{'a':1}, [1,2,3], 'hello'], dtype=object)
print(arr)

[{'a': 1} list([1, 2, 3]) 'hello']

Choose Right datatype- to optimize memory, Improve performance and precision

Primarily useful for numbers and other data types will result in degraded performance

## Day10 - Numpy: Broadcasting

#Speed Boost - Vectorization and Broadcasting

Python loops are very slow as interpreter does sequential processing. Numpy is optimized for memory and computation

Vectorization helps to fix the loop problem.

arr = np.array([1,2,3,4,5])
result = arr**2
print(result)

[ 1  4  9 16 25]

Above operation is faster because numpy's vectorized operation is implemented in C language which is much faster than python loops

Numpy also does Batch processing (multiple elements in parallel) using SIMD (Single instruction multiple data), allowing multiple operations to be done simultaneously. this is vectorization

Broadcasting - Numpy automatically expands arrays of different shapes to make them compatible for element-wise operations without actually replicating data in memory

result + 10 - Here scalar 10 is broadcasted across the entire array and no extra memory is used.

array([11, 14, 19, 26, 35])

A vector can also be broadcasted
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([1,2,3])
result = arr1+arr2 # broadcasting arr2 across arr1
print(result)

output
[[2 4 6]
 [5 7 9]]

For broadcasting to work-
1. Array dimensions must be compatible- samme or one must be 1
2. Stretching arrays - Numpy stretches the smaller array to match the larger one, element-wise, without copying data

#Real world scenario for Broadcasting

Normalization

data = np.array([[10,20,30],[15,20,25],[2,4,6],[30,40,50]])
mean = data.mean(axis=0)
std = data.std(axis=0)

normalized_data = (data-mean)/std
print(normalized_data)

Output
[[-0.41637162 -0.07832604  0.14369225]
 [ 0.07347734 -0.07832604 -0.17562387]
 [-1.20012997 -1.33154276 -1.38902512]
 [ 1.54302424  1.48819485  1.42095673]]

 ## Day 11- Numpy Builtin Mathematical Functions

 np.mean(arr), np.min(arr), np.max(arr), np.std(arr), np.var(arr), np.sum(arr), np.median(arr), np.percentile(arr,50)
 np.argmin(arr), np.argmax(arr), np.unique(arr), np.cumsum(arr)

## Day 12 - Getting started with Pandas

powerful open source python library used for data manipulation, cleaning and analysis. it's built on Numpy. It uses 2 main data structures

1. Series : 1D-labeled array
2. Dataframe : 2D- labeled table(like Excel or SQL table)

Pandas is to be used when we work with tables, spreadsheets or csvs in python. it makes structured data fast, expressive and flexible.
Pandas has the speed of numpy and usability of excel. Anytime we work with structured data we will use pandas. Any dastscientist will be using Pandas


# Core Data Structures in Pandas

Pandas is built on **two main data structures**:

1. **Series** → One-dimensional (like a single column in Excel)
2. **DataFrame** → Two-dimensional (like a full spreadsheet or SQL table)

***

## Series — 1D Labeled Array

A `Series` is like a list with **labels (index)**.

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)
```

**Output:**

```
0    10
1    20
2    30
3    40
dtype: int64
```

Notice the **automatic index**: 0, 1, 2, 3

You can also define a custom index:

```python
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
```

A `pandas.Series` may look similar to a Python dictionary because both store data with labels, but a Series offers much more. Unlike a dictionary, a Series supports fast vectorized operations, automatic index alignment during arithmetic, and handles missing data using `NaN`. It also allows both label-based and position-based access, and integrates seamlessly with the pandas ecosystem, especially DataFrames. While a dictionary is great for simple key–value storage, a Series is better suited for data analysis and manipulation tasks where performance, flexibility, and built-in functionality matter.

***

## DataFrame — 2D Labeled Table

A `DataFrame` is like a **dictionary of Series** — multiple columns with labels.

```python
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["Delhi", "Mumbai", "Bangalore"]
}

df = pd.DataFrame(data)
print(df)
```

**Output:**

```
     name  age      city
0   Alice   25     Delhi
1     Bob   30    Mumbai
2  Charlie   35  Bangalore
```

Each column in a `DataFrame` is a `Series`.

***

## Index and Labels

Every Series and DataFrame has an **Index** — it helps with:

* Fast lookups
* Aligning data
* Merging & joining
* Time series operations

```python
df.index         # Row labels
df.columns       # Column labels
```

You can change them using:

```python
df.index = ["a", "b", "c"]
df.columns = ["Name", "Age", "City"]
```

***

## Why Learn These Well?

Most Pandas operations are built on these foundations:

* Selection
* Filtering
* Merging
* Aggregation

Understanding Series & DataFrames will make everything else easier.

***

## Summary

* `Series` = 1D array with labels
* `DataFrame` = 2D table with rows + columns
* Both come with index and are the heart of Pandas

## Day13 - Create Data frames
1. Read from csv
2. Read from Excel
3. Read df from array
4. Read df from json

EDA - Exploratory data Analysis

EDA is an essential first step in any data science project.
it involves taking a deep look at the dataset to understand its structure, spot patterns, identify anomalies, and uncover relationship between variables.
df.head()
df.tail()
df.info()
df.shape
df.describe()
df.columns
We can also run sql queries using pandas

## Day14 - Data Selection and Filtering

we will come to know the power of Pandas

 
# Data Selection & Filtering

Selecting the right rows and columns is *the first step* in analyzing any dataset. Pandas gives you several powerful ways to do this.

---

## Selecting Rows & Columns

### Selecting Columns

```python
df["column_name"]        # Single column (as Series)
df[["col1", "col2"]]     # Multiple columns (as DataFrame)
```

### Selecting Rows by Index

Use `.loc[]` (label-based) and `.iloc[]` (position-based):

```python
df.loc[0]                # First row (by label)
df.iloc[0]               # First row (by position)
```

### Select Specific Rows and Columns

```python
df.loc[0, "Name"]        # Value at row 0, column 'Name'
df.iloc[0, 1]            # Value at row 0, column at index 1
```

You can also slice:

```python
df.loc[0:2, ["Name", "Age"]]   # Rows 0 to 2, selected columns
df.iloc[0:2, 0:2]              # Rows and cols by index position
```

---

## Fast Access: `.at` and `.iat`

These are optimized for **single element access**:

```python
df.at[0, "Name"]       # Fast label-based access
df.iat[0, 1]           # Fast position-based access
```

---

## Filtering with Conditions

### Simple Condition

```python
df[df["Age"] > 30]
```

### Multiple Conditions (AND / OR)

```python
df[(df["Age"] > 25) & (df["City"] == "Delhi")]
df[(df["Name"] == "Bob") | (df["Age"] < 30)]
```

> Use parentheses around each condition!

---

## Querying with `.query()`

The `.query()` method in pandas lets you filter DataFrame rows using a string expression — it's a more readable and often more concise alternative to using boolean indexing.

This is a cleaner, SQL-like way to filter:

```python
df.query("Age > 25 and City == 'Delhi'")
```

Dynamic column names:

```python
col = "Age"
df.query(f"{col} > 25")
```



Here are the main **rules and tips** for using `.query()` in pandas:

---

### **1. Column names become variables**
You can reference column names directly in the query string:

```python
df.query("age > 25 and city == 'Delhi'")
```

---

### **2. String values must be in quotes**
Use **single** or **double** quotes around strings in the expression:

```python
df.query("name == 'Harry'")
```

If you have quotes inside quotes, mix them:

```python
df.query('city == "Mumbai"')
```

---

### **3. Use backticks for column names with spaces or special characters**
If a column name has spaces, use backticks (`` ` ``):

```python
df.query("`first name` == 'Alice'")
```

---

### **4. You can use `@` to reference Python variables**
To pass external variables into `.query()`:

```python
age_limit = 30
df.query("age > @age_limit")
```

---

### **5. Logical operators**
Use these:
- `and`, `or`, `not` — instead of `&`, `|`, `~`
- `==`, `!=`, `<`, `>`, `<=`, `>=`

Bad:
```python
df.query("age > 30 & city == 'Delhi'")  # ❌
```

Good:
```python
df.query("age > 30 and city == 'Delhi'")  # ✅
```

---

### **6. Chained comparisons**
Just like Python:

```python
df.query("25 < age <= 40")
```

---

### **7. Avoid using reserved keywords as column names**
If you have a column named `class`, `lambda`, etc., you’ll need to use backticks:

```python
df.query("`class` == 'Physics'")
```

---

### **8. Case-sensitive**
Column names and string values are case-sensitive:

```python
df.query("City == 'delhi'")  # ❌ if actual value is 'Delhi'
```

---

### **9. `.query()` returns a **copy**, not a view**
The result is a new DataFrame. Changes won't affect the original unless reassigned:

```python
filtered = df.query("age < 50")
```

---


## Summary

- Use `df[col]`, `.loc[]`, `.iloc[]`, `.at[]`, `.iat[]` to access data  
- Filter with logical conditions or `.query()` for readable code  
- Mastering selection makes the rest of pandas feel easy
 