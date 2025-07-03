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
 
 ## Day 15 - Data cleaning and preprocessing

 Real-world data is messy. Pandas gives us powerful tools to clean and transform data before analysis.

---

## Handling Missing Values

### Check for Missing Data

```python
df.isnull()              # True for NaNs
df.isnull().sum()        # Count missing per column
```

### Drop Missing Data

```python
df.dropna()              # Drop rows with *any* missing values
df.dropna(axis=1)        # Drop columns with missing values
```

### Fill Missing Data

In pandas, fillna is used to fill unknown values. ffill and bfill are methods used to fill missing values (like NaN, None, or pd.NA) by propagating values forward or backward.


```python
df.fillna(0)                     # Replace NaN with 0
df["Age"].fillna(df["Age"].mean())  # Replace with mean
df.ffill()      # Forward fill
df.bfill()      # Backward fill
```

---

## Detecting & Removing Duplicates

df.duplicated() returns a boolean Series where:
True means that row is a duplicate of a previous row.
False means it's the first occurrence (not a duplicate yet).

```python
df.duplicated()          # True for duplicates
df.drop_duplicates()     # Remove duplicate rows
```

Check based on specific columns:

```python
df.duplicated(subset=["Name", "Age"])
```

---

## String Operations with `.str`

Works like vectorized string methods and returns a pandas Series:

```python
df["Name"].str.lower() # Converts all names to lowercase.
df["City"].str.contains("delhi", case=False) # Checks if 'delhi' is in the city name, case-insensitive.
df["Email"].str.split("@") # Outputs a pandas Series where each element is a list of strings (the split parts). This is where a Python list comes into play, but the outer object is still a pandas Series.
```

We can always chain methods like `.str.strip().str.upper()` for clean-up.

---

## Type Conversions with `.astype()`

Convert column data types:

```python
df["Age"] = df["Age"].astype(int)
df["Date"] = pd.to_datetime(df["Date"])
df["Category"] = df["Category"].astype("category")
```

### Why is pd.to_datetime() special?
Unlike astype(), which works on simple data types (like integers, strings, etc.), pd.to_datetime() is designed to:

- Handle different date formats (e.g., "YYYY-MM-DD", "MM/DD/YYYY", etc.).

- Handle mixed types (e.g., some date strings, some NaT, or missing values).

- Convert integer timestamps (e.g., UNIX time) into datetime objects.

- Recognize timezones if provided.

Check data types:

```python
df.dtypes
```

---

## Applying Functions

### `.apply()` → Apply any function to rows or columns

```python
df["Age Group"] = df["Age"].apply(lambda x: "Adult" if x >= 18 else "Minor")
```

### `.map()` → Element-wise mapping for Series

```python
gender_map = {"M": "Male", "F": "Female"}
df["Gender"] = df["Gender"].map(gender_map)
```

### `.replace()` → Replace specific values

```python
df["City"].replace({"Del": "Delhi", "Mum": "Mumbai"})
```

---

## Summary

- Use `isnull()`, `fillna()`, `dropna()` for missing data  
- Clean text with `.str`, convert types with `.astype()`  
- Use `apply()`, `map()`, `replace()` to transform your columns  
- Data cleaning is where 80% of your time goes in real projects


## Day 16 - Data Transformation

# Data Transformation

Once your data is clean, the next step is to **reshape, reformat, and reorder** it as needed for analysis. Pandas gives you plenty of flexible tools to do this.

---

## Sorting & Ranking

### Sort by Values

```python
df.sort_values("Age")                   # Ascending sort
df.sort_values("Age", ascending=False)  # Descending
df.sort_values(["Age", "Salary"])       # Sort by multiple columns
```
df.sort_values(["Age", "Salary"]) sorts the DataFrame first by the "Age" column, and if there are ties (i.e., two or more rows with the same "Age"), it will sort by the "Salary" column.

### Reset Index
If you want the index to start from 0 and be sequential, you can reset it using reset_index()
```python
df.reset_index(drop=True, inplace=True)  # Reset the index and drop the old index
```
### Sort by Index

```python
df.sort_index()
```
The df.sort_index() function is used to sort the DataFrame based on its index values. If the index is not in a sequential order (e.g., you have dropped rows or performed other operations that change the index), you can use sort_index() to restore it to a sorted order.
### Ranking
The .rank() function in pandas is used to assign ranks to numeric values in a column, like scores or points. By default, it gives the average rank to tied values, which can result in decimal numbers. For example, if two people share the top score, they both get a rank of 1.5. You can customize the ranking behavior using the method parameter. One useful option is method='dense', which assigns the same rank to ties but doesn’t leave gaps in the ranking sequence. This is helpful when you want a clean, consecutive ranking system without skips.
```python
df["Rank"] = df["Score"].rank()                 # Default: average method
df["Rank"] = df["Score"].rank(method="dense")   # 1, 2, 2, 3
```

---

## Renaming Columns & Index

```python
df.rename(columns={"oldName": "newName"}, inplace=True)
df.rename(index={0: "row1", 1: "row2"}, inplace=True)
```

To rename all columns:

```python
df.columns = ["Name", "Age", "City"]
```

---

## Changing Column Order

Just pass a new list of column names:

```python
df = df[["City", "Name", "Age"]]   # Reorder as desired
```

You can also move one column to the front:

```python
cols = ["Name"] + [col for col in df.columns if col != "Name"]
df = df[cols]
```

---



## Summary

- Sort, rank, and rename to prepare your data    
- Reordering and reshaping are key for EDA and visualization

 
 ## Day 17 - Melt and Pivot Methods in Pandas

 # Reshaping Data using Melt and Pivot

## `melt()` — Wide to Long
The `melt()` method in Pandas is used to **unpivot** a DataFrame from wide format to long format. In other words, it takes columns that represent different variables and combines them into key-value pairs (i.e., long-form data).

### When to Use `melt()`:
- When you have a DataFrame where each row is an observation, and each column represents a different variable or measurement, and you want to reshape the data into a longer format for easier analysis or visualization.

### Syntax:
```python
df.melt(id_vars=None, value_vars=None, var_name=None, value_name="value", col_level=None)
```

### Parameters:
- **`id_vars`**: The columns that you want to keep fixed (these columns will remain as identifiers).
- **`value_vars`**: The columns you want to unpivot (the ones you want to "melt" into a single column).
- **`var_name`**: The name to use for the new column that will contain the names of the melted columns (default is `'variable'`).
- **`value_name`**: The name to use for the new column that will contain the values from the melted columns (default is `'value'`).
- **`col_level`**: Used for multi-level column DataFrames. 

### Example:
Use this code to generate the Dataframe

```python
import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 78, 92],
    'Science': [90, 82, 89],
    'English': [88, 85, 94]
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)

```

Let's say we have the following DataFrame in a wide format:

| Name   | Math | Science | English |
|--------|------|---------|---------|
| Alice  | 85   | 90      | 88      |
| Bob    | 78   | 82      | 85      |
| Charlie| 92   | 89      | 94      |

### Using `melt()`:
If we want to "melt" the DataFrame so that each row represents a student-subject pair, we can do:

```python
df.melt(id_vars=["Name"], value_vars=["Math", "Science", "English"], var_name="Subject", value_name="Score")
```

This will result in the following long-format DataFrame:

| Name   | Subject | Score |
|--------|---------|-------|
| Alice  | Math    | 85    |
| Alice  | Science | 90    |
| Alice  | English | 88    |
| Bob    | Math    | 78    |
| Bob    | Science | 82    |
| Bob    | English | 85    |
| Charlie| Math    | 92    |
| Charlie| Science | 89    |
| Charlie| English | 94    |

### Explanation:
- **`id_vars=["Name"]`**: We keep the "Name" column as it is because it's the identifier.
- **`value_vars=["Math", "Science", "English"]`**: These are the columns we want to melt.
- **`var_name="Subject"`**: The new column containing the names of the subjects.
- **`value_name="Score"`**: The new column containing the scores.

### Why Use `melt()`?
- **Data normalization**: Helps in transforming data for statistical modeling and data visualization.
- **Pivot tables**: Many times, plotting functions or statistical models work better with long-format data.
 

This is useful for converting columns into rows — perfect for plotting or tidy data formats.

## `pivot()` — Long to Wide

The `pivot()` function in Pandas is used to **reshape** data, specifically to **turn long-format data into wide-format data**. This is the reverse operation of `melt()`.

### How it works:
- **`pivot()`** takes a **long-format DataFrame** and **turns it into a wide-format DataFrame** by specifying which columns will become the new columns, the rows, and the values.

### Syntax:
```python
df.pivot(index=None, columns=None, values=None)
```

### Parameters:
- **`index`**: The column whose unique values will become the rows of the new DataFrame.
- **`columns`**: The column whose unique values will become the columns of the new DataFrame.
- **`values`**: The column whose values will fill the new DataFrame. These will become the actual data (values in the table).

### Example:

Suppose we have the following long-format DataFrame:

| Name   | Subject | Score |
|--------|---------|-------|
| Alice  | Math    | 85    |
| Alice  | Science | 90    |
| Alice  | English | 88    |
| Bob    | Math    | 78    |
| Bob    | Science | 82    |
| Bob    | English | 85    |
| Charlie| Math    | 92    |
| Charlie| Science | 89    |
| Charlie| English | 94    |

### Using `pivot()` to reshape it into wide format:

```python
df.pivot(index="Name", columns="Subject", values="Score")
```

### Resulting DataFrame:

| Name    | English | Math | Science |
|---------|---------|------|---------|
| Alice   | 88      | 85   | 90      |
| Bob     | 85      | 78   | 82      |
| Charlie | 94      | 92   | 89      |

### Explanation:
- **`index="Name"`**: The unique values in the "Name" column will become the rows in the new DataFrame.
- **`columns="Subject"`**: The unique values in the "Subject" column will become the columns in the new DataFrame.
- **`values="Score"`**: The values from the "Score" column will populate the table.

### Why use `pivot()`?

1. **Better data structure**: It makes data easier to analyze when you have categories that you want to split into multiple columns.
2. **Easier visualization**: Often, you want to represent data in a format where categories are split across columns (for example, when creating pivot tables for reporting).
3. **Aggregating data**: You can perform aggregations (like `sum`, `mean`, etc.) to group values before pivoting.

### Important Notes:
1. **Duplicate Entries**: If you have multiple rows with the same combination of `index` and `columns`, **pivot()** will raise an error. In such cases, you should use `pivot_table()` (which can handle duplicate entries by aggregating them).

### Example of `pivot_table()` to handle duplicates:

Suppose the DataFrame is like this (with duplicate entries):

| Name   | Subject | Score |
|--------|---------|-------|
| Alice  | Math    | 85    |
| Alice  | Math    | 80    |
| Alice  | Science | 90    |
| Bob    | Math    | 78    |
| Bob    | Math    | 82    |

We can use **`pivot_table()`** to aggregate values (e.g., taking the **mean** for duplicate entries):

```python
df.pivot_table(index="Name", columns="Subject", values="Score", aggfunc="mean")
```

### Resulting DataFrame:

| Name   | Math | Science |
|--------|------|---------|
| Alice  | 82.5 | 90      |
| Bob    | 80   | NaN     |

In this case, the **Math** score for Alice is averaged (85 + 80) / 2 = 82.5. If a cell is empty, it means there was no value for that combination.

### Summary:
- Use `melt()` to go long, `pivot()` to go wide  
- **`pivot()`** is used to turn long-format data into wide-format by spreading unique column values into separate columns.
- If there are **duplicate values** for a given combination of `index` and `columns`, you should use **`pivot_table()`** with an aggregation function to handle the duplicates.
 
 ## Day 18 - Aggregation and Grouping

 # Aggregation & Grouping

Grouping and aggregating helps you **summarize your data** — like answering:  
> “What’s the average salary *per department*?”  
> “How many users joined the Gym *per month*?”

---

## `.groupby()` Function

df.groupby() is used to group rows of a DataFrame based on the values in one or more columns, which allows you to then perform aggregate functions (like sum(), mean(), count(), etc.) on each group.
Consider this DataFrame:

```python 
df = pd.DataFrame({
    "Department": ["HR", "HR", "IT", "IT", "Marketing", "Marketing", "Sales", "Sales"],
    "Team": ["A", "A", "B", "B", "C", "C", "D", "D"],
    "Gender": ["M", "F", "M", "F", "M", "F", "M", "F"],
    "Salary": [85, 90, 78, 85, 92, 88, 75, 80],
    "Age": [23, 25, 30, 22, 28, 26, 21, 27],
    "JoinDate": pd.to_datetime([
        "2020-01-10", "2020-02-15", "2021-03-20", "2021-04-10",
        "2020-05-30", "2020-06-25", "2021-07-15", "2021-08-01"
    ])
})  

```

```python
df.groupby("Department")["Salary"].mean()
```

This says:  
> “Group by Department, then calculate average Salary for each group.”

---

## Common Aggregation Functions

```python
df.groupby("Team")["Salary"].mean()     # Average per team
df.groupby("Team")["Salary"].sum()      # Total score
df.groupby("Team")["Salary"].count()    # How many entries
df.groupby("Team")["Salary"].min()
df.groupby("Team")["Salary"].max()
```

To group by multiple columns:

```python
df.groupby(["Team", "Gender"])["Salary"].mean()
```

---

## Custom Aggregations with `.agg()`

Apply **multiple functions** at once like this:

```python
df.groupby("Team")["Salary"].agg(["mean", "max", "min"])
```
In pandas, .agg and .aggregate are exactly the same — they're aliases for the same method

Name your own functions:

```python
df.groupby("Team")["Salary"].agg(
    avg_score="mean",
    high_score="max"
)
```

Apply different functions to different columns:

```python
df.groupby("Team").agg({
    "Salary": "mean",
    "Age": "max"
})
```

---

## Transform vs Aggregate vs Filter

| Operation | Returns | When to Use |
|-----------|---------|-------------|
| `.aggregate()` | Single value per group | Summary (like mean) |
| `.transform()` | Same shape as original | Add new column based on group |
| `.filter()`    | Subset of rows | Keep/discard whole groups |

### `.transform()` Example:

```python
df["Team Avg"] = df.groupby("Team")["Salary"].transform("mean")
```

Now each row gets its **team average** — great for comparisons!

### `.filter()` Example:

```python
df.groupby("Team").filter(lambda x: x["Salary"].mean() > 80)
```

Only keeps teams with average score > 80.

---

## Summary

- `.groupby()` helps you summarize large datasets by category  
- Use `mean()`, `sum()`, `count()`, `.agg()` for custom metrics  
- `.transform()` adds values back to original rows  
- `.filter()` keeps only groups that meet conditions

 ## Day 19 - Merging and Joining Data

 # Merging & Joining Data

Often, data is split across multiple tables or files. Pandas lets you **combine** them just like SQL — or even more flexibly!

---

## Sample DataFrames

```python
employees = pd.DataFrame({
    "EmpID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "DeptID": [10, 20, 30]
})

departments = pd.DataFrame({
    "DeptID": [10, 20, 40],
    "DeptName": ["HR", "Engineering", "Marketing"]
})
```

---

## Merge Like SQL: `pd.merge()`

### Inner Join (default)

```python
pd.merge(employees, departments, on="DeptID")
```

Returns only matching DeptIDs:

| EmpID | Name    | DeptID | DeptName    |
|--------|---------|--------|-------------|
| 1      | Alice   | 10     | HR          |
| 2      | Bob     | 20     | Engineering |

---

### Left Join

```python
pd.merge(employees, departments, on="DeptID", how="left")
```

Keeps all employees, fills `NaN` where no match.

---

### Right Join

```python
pd.merge(employees, departments, on="DeptID", how="right")
```

Keeps all departments, even if no employee.

---

### Outer Join

```python
pd.merge(employees, departments, on="DeptID", how="outer")
```

Includes *all* data, fills missing with `NaN`.


---

## Concatenating DataFrames

Use `pd.concat()` to **stack** datasets either vertically or horizontally.

### Vertical (rows)

```python
df1 = pd.DataFrame({"Name": ["Alice", "Bob"]})
df2 = pd.DataFrame({"Name": ["Charlie", "David"]})

pd.concat([df1, df2])
```

### Horizontal (columns)

```python
df1 = pd.DataFrame({"ID": [1, 2]})
df2 = pd.DataFrame({"Score": [90, 80]})

pd.concat([df1, df2], axis=1)
```

> Make sure indexes align when using `axis=1`

---

## When to Use What?

| Use Case                        | Method     |
|---------------------------------|------------|
| SQL-style joins (merge keys)    | `pd.merge()` or `.join()` |
| Stack datasets vertically       | `pd.concat([df1, df2])`   |
| Combine different features side-by-side | `pd.concat([df1, df2], axis=1)` |
| Align on index                 | `.join()` or merge with `right_index=True` |

---

## Summary

- Use `merge()` like SQL joins (`inner`, `left`, `right`, `outer`)  
- Use `concat()` to stack DataFrames (rows or columns)  
- Handle mismatched keys and indexes with care  
- Merging and joining are essential for real-world projects

 
 ## Day 20 - Working with CSVs
 # Reading & Writing Files in Pandas

## CSV Files

### Read CSV
```python
df = pd.read_csv("data.csv")
```

Options:
```python
pd.read_csv("data.csv", usecols=["Name", "Age"], nrows=10)
```

### Write CSV
```python
df.to_csv("output.csv", index=False)
```

---

## Excel Files

### Read Excel
```python
df = pd.read_excel("data.xlsx")
```

Options:
```python
pd.read_excel("data.xlsx", sheet_name="Sales")
```

### Write Excel
```python
df.to_excel("output.xlsx", index=False)
```

Multiple sheets:
```python
with pd.ExcelWriter("report.xlsx") as writer:
    df1.to_excel(writer, sheet_name="Summary", index=False)
    df2.to_excel(writer, sheet_name="Details", index=False)
```

---

## JSON Files

### Read JSON
```python
df = pd.read_json("data.json")
```


## Summary

- `read_*` and `to_*` methods for CSV, Excel, JSON
- Use `sheet_name` for Excel 
 
 ## Day 21 - Data Visualization

 Why Data Visualization is Important

Data visualization is the bridge between raw data and human understanding. When done right, it helps:

Reveal patterns, trends, and correlations in the data.
Communicate insights clearly to stakeholders.
Speed up decision-making by simplifying complex datasets.
Make data storytelling engaging and accessible to all.
A picture is worth a thousand words

“The greatest value of a picture is when it forces us to notice what we never expected to see.” – John Tukey

Exploratory vs Explanatory Visuals

Exploratory Visualizations
Purpose: Explore the data, uncover insights, find patterns.
Audience: You (the data analyst/scientist).
Example: Pair plots, correlation heatmaps, scatter matrix.

Explanatory Visualizations
Purpose: Communicate a specific insight or story.
Audience: Stakeholders, clients, public.

Example: A bar chart in a presentation showing sales trends.
Aspect	Exploratory	Explanatory
Goal	Find insights	Communicate insights

Audience	Analyst / Data Scientist	Stakeholders / Public
Style	Raw, fast, flexible	Polished, focused, clean
Basic Principles of Good Visualizations
Clarity
Avoid clutter. Use labels, legends, and proper axis scales.

# Table 
Aspect	Exploratory	Explanatory
Goal	Find insights	Communicate insights
Audience	Analyst / Data Scientist	Stakeholders / Public
Style	Raw, fast, flexible	Polished, focused, clean

# Basic Principles of Good Visualizations
Clarity
Avoid clutter. Use labels, legends, and proper axis scales.

Context
Always provide context: What is being measured? Over what time frame? In what units?

Focus
Highlight the key insight. Use colors and annotations to draw attention.

Storytelling
Don’t just show data — tell a story. Guide the viewer through a narrative.

Accessibility
Use carefully chosen color palettes that enhance readability for all viewers.

## Day22 - MatplotLib Intro

# Introduction to Matplotlib

Today, we’ll cover the **basics of Matplotlib** — the most fundamental plotting library in Python. By the end, you’ll understand how to make clean and powerful plots, step by step.

---

## What is `matplotlib.pyplot`?

- `matplotlib.pyplot` is a module in Matplotlib — it's like a paintbrush for your data.
- We usually import it as `plt`:

```python
import matplotlib.pyplot as plt
```

> `plt` is just a short alias to save typing!

---

## What is `plt.show()`?

- `plt.show()` is used to **display the plot**.
- Without it, in scripts, you might not see the plot window.

```python
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
```

---

## Interacting with the Plot

When a plot appears, you can:

- Zoom In/Out  
- Pan around  
- Use arrows to navigate history  
- Reset to home  
- Save as PNG using the disk icon  

> These features are **automatically included** in the plot window!

---

## Real Data Example: Sachin Tendulkar’s Runs Over Time

```python
years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
runs =  [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]

plt.plot(years, runs)
plt.show()
```

---

## Adding X and Y Labels

```python
plt.plot(years, runs)
plt.xlabel("Year")
plt.ylabel("Runs Scored")
plt.title("Sachin Tendulkar's Yearly Runs")
plt.show()
```

---

## Multiple Lines in One Plot

```python
kohli = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]
sehwag = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 0]

plt.plot(years, kohli, label="Virat Kohli")
plt.plot(years, sehwag, label="Virender Sehwag")

plt.xlabel("Year")
plt.ylabel("Runs Scored")
plt.title("Performance Comparison")
plt.legend()
plt.show()
```

---

## Why `label` is Better than List in `legend`

Bad practice:

```python
plt.plot(years, kohli)
plt.plot(years, sehwag)
plt.legend(["Kohli", "Sehwag"])  # prone to mismatch
```

Better:

```python
plt.plot(years, kohli, label="Kohli")
plt.plot(years, sehwag, label="Sehwag")
plt.legend()
```

---

## Using Format Strings

```python
plt.plot(years, kohli, 'ro--', label="Kohli")  # red circles with dashed lines
plt.plot(years, sehwag, 'g^:', label="Sehwag")  # green triangles dotted
plt.legend()
```

---

## Color and Line Style Arguments

```python
plt.plot(years, kohli, color='orange', linestyle='--', label="Kohli")
plt.plot(years, sehwag, color='green', linestyle='-.', label="Sehwag")
plt.plot(years, runs, color='blue', label="Tendulkar")
plt.legend()
```

---

## Line Width and Layout Tweaks

```python
plt.plot(years, kohli, linewidth=3, label="Kohli")
plt.plot(years, sehwag, linewidth=2, label="Sehwag")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
```

---

## Using Styles in Matplotlib

```python
print(plt.style.available)
```

Try a few:

```python
plt.style.use("ggplot")
# or
plt.style.use("seaborn-v0_8-bright")
```

---

## XKCD Comic Style

```python
with plt.xkcd():
    plt.plot(years, kohli, label="Kohli")
    plt.plot(years, sehwag, label="Sehwag")
    plt.title("Epic Battle of the Batsmen")
    plt.legend()
    plt.show()
```

---

## Visualizing Tons of Data – What Crowded Looks Like

```python
import numpy as np

for i in range(50):
    plt.plot(np.random.rand(100), linewidth=1)

plt.title("Too Much Data Can Be Confusing!")
plt.grid(True)
plt.tight_layout()
plt.show()
```

---

## Final Tips for Beginners

- Always start with simple plots
- Add labels and legends early
- Use `plt.grid()` and `plt.tight_layout()` to improve readability
- Try different styles to find what works for your use case

---

**Assignment:**  
Create a plot comparing **Kohli**, **Rohit Sharma**, and **Sehwag** across 10 years of hypothetical runs.  
Use:
- Labels
- Legends
- Colors
- Line styles
- One custom style


## Day23 - Bar Charts in Matplotlib

#  Matplotlib Bar Charts

Bar charts are used to **compare quantities** across categories. They are easy to read and powerful for visual analysis.

We’ll use **Sachin Tendulkar’s yearly run data**, then learn how to create grouped bar charts and horizontal bar charts with examples.

---

## Sachin’s Yearly Runs – Vertical Bar Chart

### The Data

```python
import matplotlib.pyplot as plt

years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
runs =  [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]
```

### Basic Bar Plot

```python
plt.bar(years, runs)
plt.xlabel("Year")
plt.ylabel("Runs Scored")
plt.title("Sachin Tendulkar's Yearly Runs")
plt.show()
```

---

## Setting Bar Width & Side-by-Side Bar Charts

Let’s compare **Sachin**, **Sehwag**, and **Kohli** side-by-side for the same years.

```python
import numpy as np

sachin = [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]
sehwag = [0, 200, 900, 1400, 1600, 1800, 1500, 1100, 800, 0]
kohli  = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]

x = np.arange(len(years))  # index positions
width = 0.25
```
The value of width ranges from 0 to 1 (default 0.8); it can go above 1, but bars will start to overlap.
### Plotting Side-by-Side Bars

```python
plt.bar(x - width, sachin, width=width, label="Sachin")
plt.bar(x, sehwag, width=width, label="Sehwag")
plt.bar(x + width, kohli, width=width, label="Kohli")

plt.xlabel("Year")
plt.ylabel("Runs")
plt.title("Run Comparison")
plt.xticks(x, years)  # Show actual year instead of 0,1,2,...
plt.legend()
plt.tight_layout()
plt.show()
```

---

## Why Use `xticks()`?

By default, `plt.bar()` uses numeric x-values (0, 1, 2, ...).  
We use `plt.xticks()` to set the correct category labels like years or names.

---

## Horizontal Bar Charts with `barh()`

Let’s compare **total runs scored in the first 5 years** by different players.

```python
players = ["Sachin", "Sehwag", "Kohli", "Yuvraj"]
runs_5yrs = [500+700+1100+1500+1800, 0+200+900+1400+1600, 0+0+500+800+1100, 300+600+800+1100+900]
```

### Plotting with `barh()`

```python
plt.barh(players, runs_5yrs, color="skyblue")
plt.xlabel("Total Runs in First 5 Years")
plt.title("First 5-Year Performance of Indian Batsmen")
plt.tight_layout()
plt.show()
```

### Why Switch `x` and `y`?

- In `bar()` → `x = categories`, `y = values`
- In `barh()` → `y = categories`, `x = values`

> Horizontal bars help when category names are long or when you want to emphasize comparisons from left to right.

---

### Adding Value Labels with `plt.text()`

You can use `plt.text()` to display values **on top of bars**, making your chart easier to read. It's especially useful in presentations and reports.

```python
import matplotlib.pyplot as plt

players = ["Sachin", "Sehwag", "Kohli"]
runs = [1500, 1200, 1800]

plt.bar(players, runs, color="skyblue")

# Add labels on top of bars
for i in range(len(players)):
    plt.text(i, runs[i] + 50, str(runs[i]), ha='center')

plt.ylabel("Runs")
plt.title("Runs Scored by Players")
plt.tight_layout()
plt.show()
```

**Tip**: Use `ha='center'` to center the text and add a small offset (`+50` here) to avoid overlap with the bar.

---

## Summary

| Feature                  | Use                                                  |
|--------------------------|-------------------------------------------------------|
| `plt.bar()`              | Vertical bars for categorical comparison             |
| `plt.barh()`             | Horizontal bars (great for long labels)              |
| `width=`                 | Control thickness/spacing of bars                    |
| `np.arange()`            | Helps to align multiple bars side by side            |
| `plt.xticks()`           | Replaces index numbers with real labels              |
| `plt.tight_layout()`     | Prevents labels from overlapping                     |

---

**Assignment:**  
Create a side-by-side bar chart comparing runs of Sachin, Kohli, and Sehwag over 5 selected years.  
Then create a horizontal bar chart showing total runs scored in their debut 5 years.

 
## Day 24- Pie charts in Matplotlib

# Matplotlib Pie Charts

Pie charts are used to show **part-to-whole relationships**. They're visually appealing but best used with **fewer categories**, as too many slices can get cluttered and hard to interpret.

---

## Setting a Style

```python
import matplotlib.pyplot as plt

plt.style.use("ggplot")  # Choose any style you like
```

---

## Basic Pie Chart Example

```python
# Data
labels = ["Sachin", "Sehwag", "Kohli", "Yuvraj"]
runs = [18000, 8000, 12000, 9500]

plt.title("Career Runs of Indian Batsmen")
plt.pie(runs, labels=labels)
plt.show()
```

---

## Custom Colors

You can use color names or hex codes.

```python
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
plt.pie(runs, labels=labels, colors=colors)
plt.show()
```

---

## Add Edges and Style Slices with `wedgeprops`

You can customize the look of the slices using `wedgeprops`.

```python
plt.pie(
    runs,
    labels=labels,
    colors=colors,
    wedgeprops={'edgecolor': 'black', 'linewidth': 2, 'linestyle': '--'}
)
plt.show()
```

**Tip**: You can Google “matplotlib wedgeprops” for more customization options.

Visit [this documentation page](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html) for more

---

## Highlight a Slice Using `explode`

Use `explode` to **pull out** one or more slices.

```python
explode = [0.1, 0, 0, 0]  # Only highlight Sachin's slice

plt.pie(runs, labels=labels, explode=explode, colors=colors)
plt.title("Exploded Pie Example")
plt.show()
```

---

## Add Shadows for a 3D Feel

```python
plt.pie(
    runs,
    labels=labels,
    explode=explode,
    colors=colors,
    shadow=True  # adds a 3D-like shadow
)
plt.show()
```

---

## Start Angle

Use `startangle` to rotate the pie for better alignment.

```python
plt.pie(
    runs,
    labels=labels,
    explode=explode,
    colors=colors,
    shadow=True,
    startangle=140
)
plt.show()
```

---

## Show Percentages with `autopct`

```python
plt.pie(
    runs,
    labels=labels,
    autopct='%1.1f%%',
    startangle=140
)
plt.title("Career Run Share")
plt.show()
```

---

## Crowded Pie Chart – Why to Avoid

```python
# Too many categories
languages = ['Python', 'Java', 'C++', 'JavaScript', 'C#', 'Ruby', 'Go', 'Rust', 'Swift', 'PHP']
usage = [30, 20, 10, 10, 7, 5, 4, 3, 2, 1]

plt.pie(usage, labels=languages, autopct='%1.1f%%', startangle=90)
plt.title("Programming Language Usage (Crowded Example)")
plt.show()
```

**Why avoid it?**  
- Hard to compare slice sizes visually  
- Cluttered and confusing  
- No clear insight  
**Better alternatives:** bar charts or horizontal bar charts

---

## Summary of Useful Pie Chart Parameters

| Parameter     | Use                                                |
|---------------|-----------------------------------------------------|
| `labels`      | Label each slice                                    |
| `colors`      | Customize slice colors (names or hex)              |
| `explode`     | Pull out slices for emphasis                        |
| `shadow`      | Adds depth-like shadow                              |
| `startangle`  | Rotates pie to start from a different angle         |
| `autopct`     | Shows percentage text on slices                     |
| `wedgeprops`  | Customize slice edge, fill, width, etc.             |

---

**Assignment:**  
Create a pie chart showing the market share of mobile OS (Android, iOS, others). Then recreate the same using a horizontal bar chart and observe which is easier to understand.

---
 
 ## Day 25 - Stack Plots in Matplotlib

 # Stack Plots in Matplotlib

## Let's Start with a Pie Chart

Before we understand what a stack plot is, let’s visualize some simple data  

Imagine you surveyed how a group of students spends their after-school time:

```python
import matplotlib.pyplot as plt

activities = ['Studying', 'Playing', 'Watching TV', 'Sleeping']
time_spent = [3, 2, 2, 5]  # hours in a day

colors = ['skyblue', 'lightgreen', 'gold', 'lightcoral']

plt.figure(figsize=(6,6))
plt.pie(time_spent, labels=activities, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title("After School Activities")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
```

### Interpretation:

- **Studying**: 3 hours
- **Playing**: 2 hours
- **Watching TV**: 2 hours
- **Sleeping**: 5 hours

This pie chart shows how a single student spends time **in one day**.

---

## What is a Stack Plot?

Now, let’s imagine you surveyed **multiple days**, and you want to track how the time spent on each activity changes over a week.

A **Stack Plot** is a type of area chart that helps visualize **multiple quantities over time**, stacked on top of each other. It's especially useful to see **how individual parts contribute to a whole over time**.

### Use Cases:
- Time spent on different activities over days
- Distribution of tasks by team members over a project timeline
- Website traffic sources over a week

---

## Stack Plot Example

```python
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]  # Days of the week
studying = [3, 4, 3, 5, 4, 3, 4]
playing = [2, 2, 1, 1, 2, 3, 2]
watching_tv = [2, 1, 2, 2, 1, 1, 1]
sleeping = [5, 5, 6, 5, 6, 5, 5]

labels = ['Studying', 'Playing', 'Watching TV', 'Sleeping']
colors = ['skyblue', 'lightgreen', 'gold', 'lightcoral']

plt.figure(figsize=(10,6))
plt.stackplot(days, studying, playing, watching_tv, sleeping,
              labels=labels, colors=colors, alpha=0.8)

plt.legend(loc='upper left')  # Location of the legend
plt.title('Weekly Activity Tracker')
plt.xlabel('Day')
plt.ylabel('Hours')
plt.grid(True)
plt.show()
```

---

## Key Parameters in `stackplot()`

| Parameter | Description |
|----------|-------------|
| `x` | The x-axis data (like days) |
| `*args` | Multiple y-values (like studying, playing, etc.) |
| `labels` | Labels for the legend |
| `colors` | List of colors for each stack |
| `alpha` | Transparency level (0 to 1) |
| `loc` (in `legend`) | Position of the legend (`'upper left'`, `'best'`, etc.) |

---

## Summary

- Use **pie charts** for a snapshot in time.
- Use **stack plots** to see how data changes over time while still showing parts of a whole.
- Customize your plot using parameters like `colors`, `labels`, `alpha`, and `legend`.

Stack plots are a great way to **tell a story over time**.

## Quick quiz
Try making a stackplot with your own weekly schedule!

 ## Day 26 - Histograms in Matplotlib

 # Histograms in Matplotlib

A **histogram** is a type of plot that shows the distribution of a dataset. It’s especially useful for visualizing the **frequency of numerical data** within specified ranges (called *bins*).

---

## Why and When to Use Histograms?

Use histograms when:
- You want to **understand the distribution** of a numerical dataset (e.g. age, salary, views).
- You want to **detect skewness**, outliers, or **understand spread**.
- You’re **binning continuous data** into intervals.

Examples include:
- Analyzing the age of your YouTube viewers
- Understanding test scores distribution
- Checking if data is normally distributed

---

## Understanding the `bins` Argument

The `bins` argument controls how the data is grouped:
- If an **integer**, it defines the number of equal-width bins.
- If a **list**, it defines custom bin **edges**, allowing you to control the range and width of each bin.

```python
plt.hist(data, bins=10)  # 10 equal-width bins
plt.hist(data, bins=[10, 20, 30, 40, 60, 100])  # Custom age bins
```

---

## `edgecolor` for Better Visibility

The `edgecolor` parameter adds borders to the bars, improving clarity:

```python
plt.hist(data, bins=10, edgecolor='black')
```

---

## Example: Age Distribution of YouTube Viewers

Here is age data for some viewers:

```python
import matplotlib.pyplot as plt
import numpy as np

ages = [
    34, 28, 36, 45, 27, 27, 45, 37, 25, 35,
    25, 25, 32, 10, 12, 24, 19, 33, 20, 15,
    44, 27, 30, 15, 24, 31, 18, 33, 23, 27,
    23, 48, 29, 19, 38, 17, 32, 10, 16, 31,
    37, 31, 28, 26, 15, 22, 25, 40, 33, 12,
    33, 26, 23, 36, 40, 39, 21, 26, 33, 39,
    25, 28, 18, 18, 38, 43, 29, 40, 33, 23,
    33, 45, 29, 45, 3, 38, 30, 27, 30, 10,
    27, 33, 44, 24, 21, 24, 39, 33, 24, 35,
    30, 39, 22, 26, 26, 15, 32, 32, 30, 27
]

bins = [10, 20, 30, 40, 50, 60, 70]

plt.hist(ages, bins=bins, edgecolor='black')
plt.title('Age Distribution of YouTube Viewers')
plt.xlabel('Age Group')
plt.ylabel('Number of Viewers')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
```

---

## Adding a Vertical Line: `axvline`

Use `axvline` to mark a specific value like the **average age** or a **threshold**.

```python
plt.hist(ages, bins=bins, edgecolor='black')
plt.axvline(np.mean(ages), color='red', linestyle='--', linewidth=2, label='Average Age')
plt.legend()
plt.title('Age Distribution with Mean Line')
plt.show()
```
---

## Summary

| Parameter | Purpose |
|----------|---------|
| `bins` | Number or custom edges of bins |
| `edgecolor` | Color around each bar | 
| `axvline` | Vertical reference line | 
 
 ## Day 27 - Scatterplots in Matplotlib

 # Scatter Plot in Matplotlib

Scatter plots are used to show the relationship between two variables. Let's assume we are plotting the **study hours vs. exam scores** for a group of students.

## 1. Basic Scatter Plot

```python
import matplotlib.pyplot as plt

# Sample data
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9]
exam_scores = [40, 45, 50, 55, 60, 65, 75, 85, 90]

plt.scatter(study_hours, exam_scores)
plt.title('Study Hours vs Exam Score')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.grid(True)
plt.show()
```

> This shows a simple scatter plot. You can notice a general upward trend — more study hours lead to better scores.

---

## 2. Adding Color and Size

```python
# Size of points based on score (bigger score -> bigger point)
sizes = [score * 2 for score in exam_scores]
colors = ['red' if score < 60 else 'green' for score in exam_scores]

plt.scatter(study_hours, exam_scores, s=sizes, c=colors)
plt.title('Colored & Sized Scatter Plot')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.grid(True)
plt.show()
```

> Points are colored based on performance and scaled in size by score. Red means low score, green means good.

---

## 3. Using a Colormap

```python
import numpy as np

# Also works with Numpy Arrays
scores_normalized = np.array(exam_scores)

plt.scatter(study_hours, exam_scores, c=scores_normalized, cmap='viridis')
plt.colorbar(label='Score')
plt.title('Scatter Plot with Colormap')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.grid(True)
plt.show()
```
> Google: https://matplotlib.org/stable/users/explain/colors/colormaps.html
> 
> `cmap` adds gradient coloring based on the score. `colorbar` helps understand what the colors represent.

---

## 4. Adding Annotations

```python
plt.scatter(study_hours, exam_scores)

# Add labels
for i in range(len(study_hours)):
    plt.annotate(f'Student {i+1}', (study_hours[i], exam_scores[i]))

plt.title('Scatter Plot with Annotations')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.grid(True)
plt.show()
```

> Annotations help identify individual points, which is useful in small datasets.

---

## 5. Multiple Groups in One Plot

```python
# Assume two groups: Class A and Class B
class_a_hours = [2, 4, 6, 8]
class_a_scores = [45, 55, 65, 85]

class_b_hours = [1, 3, 5, 7, 9]
class_b_scores = [40, 50, 60, 70, 90]

plt.scatter(class_a_hours, class_a_scores, label='Class A', color='blue')
plt.scatter(class_b_hours, class_b_scores, label='Class B', color='orange')

plt.title('Scatter Plot: Class A vs Class B')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.legend()
plt.grid(True)
plt.show()
```

> When comparing two datasets, use different colors and a legend for clarity.

 ## Day 28 - Sub plots in Matplotlib

 # Subplots in Matplotlib

Subplots allow you to show **multiple plots in a single figure**, side-by-side or in a grid layout. This is helpful when comparing different datasets or aspects of the same data.

---

## 1. Basic Subplot (1 row, 2 columns)

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [i * 2 for i in x]
y2 = [i ** 2 for i in x]

# Create a figure with 1 row and 2 columns
plt.subplot(1, 2, 1)  # (rows, cols, plot_no)
plt.plot(x, y1)
plt.title('Double of x')

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title('Square of x')

plt.tight_layout()
plt.show()
```

> `plt.subplot(1, 2, 1)` means 1 row, 2 columns, and we're plotting in the 1st subplot.

---

## 2. 2×2 Grid of Subplots

```python
# More variations of x
y3 = [i ** 0.5 for i in x]
y4 = [10 - i for i in x]

plt.figure(figsize=(8, 6))  # Optional: make it bigger

plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title('x * 2')

plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.title('x squared')

plt.subplot(2, 2, 3)
plt.plot(x, y3)
plt.title('sqrt(x)')

plt.subplot(2, 2, 4)
plt.plot(x, y4)
plt.title('10 - x')

plt.tight_layout()
plt.show()
```

> This lays out 4 plots in a 2x2 grid. `plt.tight_layout()` avoids overlapping titles and labels.

---

## 3. Using `plt.subplots()` for Clean Code

```python
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].plot(x, y1)
axs[0].set_title('x * 2')

axs[1].plot(x, y2)
axs[1].set_title('x squared')
 
fig.suptitle('Simple Comparison Plots', fontsize=14)
fig.tight_layout()
fig.subplots_adjust(top=0.85)  # So title doesn't overlap
fig.savefig('my_plots.png')    # Save as image

plt.show()
```

### So to summarize:

- axs is for working on individual plots
- fig is for settings that apply to the whole figure

> `plt.subplots()` returns a figure and a list/array of axes objects. This is more flexible and cleaner, especially for loops or advanced customizations.

---

## 4. Looping Over Subplots

```python
fig, axs = plt.subplots(2, 2, figsize=(8, 6))
ys = [y1, y2, y3, y4]
titles = ['x * 2', 'x squared', 'sqrt(x)', '10 - x']

for i in range(2):
    for j in range(2):
        idx = i * 2 + j
        axs[i, j].plot(x, ys[idx])
        axs[i, j].set_title(titles[idx])

plt.tight_layout()
plt.show()
```

> This approach works well when dealing with dynamic or repetitive data series.
 
 ## Day 29 - Intro to Seaborn

 # Introduction to Seaborn
 
**Seaborn** is a Python library built on top of Matplotlib that makes it **easier** and **prettier** to create complex, beautiful visualizations.

---

## Why Seaborn?

- Matplotlib is powerful but very **low-level**.
- Seaborn adds **high-level** features like **automatic styling, themes, color palettes**, and **dataframe integration**.
- Seaborn comes with built in Datasets
- Makes complex plots (like **boxplots**, **violin plots**, **heatmaps**, **pairplots**) **very easy**.

In short:  
- Less code  
- Better-looking graphs  
- Easy handling of DataFrames (like from pandas)

---

## Basic Setup

```python
# Install Seaborn if you don't have it
!pip install seaborn

# Import Seaborn
import seaborn as sns
import matplotlib.pyplot as plt
```

---

## Seaborn Themes

Seaborn automatically makes your plots look good, but you can even control the overall "theme."

```python
sns.set_theme(style="darkgrid")  # Options: whitegrid, dark, white, ticks
```

Example:

```python
import numpy as np

x = np.array([0, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 60])
y = np.sin(x)

sns.lineplot(x=x, y=y)
plt.title('Beautiful Line Plot')
plt.show()
```

---

## Summary 

- Seaborn makes complex, attractive, and statistical plots simple and ready for professional reports.

- Matplotlib is important to know for fine-tuning or customization, but Seaborn should be your first choice for day-to-day plotting.

- In real-world Data Science projects, Seaborn saves hours of manual work by offering higher-level, smarter defaults.

## Day 30 - Seaborn plots

# Basic Plot Types in Seaborn  

- **Seaborn** comes with **built-in example datasets**.
- These are small real-world datasets like restaurant tips, flight passenger counts, iris flower measurements, etc.
- They are mainly used for **practice**, **examples**, and **learning** plotting techniques without needing to manually download any data.

You can **load** these datasets directly into a **pandas DataFrame** using `sns.load_dataset()`.

---

## How to See All Available Datasets

```python
import seaborn as sns

print(sns.get_dataset_names())
```

This will list dataset names like: `tips`, `flights`, `iris`, `diamonds`, `penguins`, `titanic`, etc.

---

## How to Load a Dataset

```python
tips = sns.load_dataset('tips')
print(tips.head())
```

- This loads the **"tips"** dataset (restaurant bills and tips).
- It returns a **pandas DataFrame** ready for analysis or plotting.

---

## Why Seaborn Provides Datasets

- To **quickly test** different types of plots
- To **learn plotting** without needing your own data at first
- To create **examples** and **tutorials** easily
- To show real-world messy data handling (missing values, categorical data, etc.)

---
Now lets look into some plots we can create usign Seaborn
 
## 1. Line Plot

```python
tips = sns.load_dataset('tips')

sns.lineplot(x="total_bill", y="tip", data=tips)
plt.title('Line Plot Example')
plt.show()
```

---

## 2. Scatter Plot

```python
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="time")
plt.title('Scatter Plot with Color by Time')
plt.show()
```

---

## 3. Bar Plot

```python
sns.barplot(x="day", y="total_bill", data=tips)
plt.title('Average Bill per Day')
plt.show()
```

---

## 4. Box Plot

Boxplots show distributions, medians, and outliers in one simple plot.

```python
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title('Boxplot of Total Bill per Day')
plt.show()
```

---

## 5. Heatmap (Correlation Matrix)

```python
flights = sns.load_dataset('flights')
pivot_table = flights.pivot("month", "year", "passengers")

sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu")
plt.title('Heatmap of Passengers')
plt.show()
```

---

## Working with Pandas DataFrames

One of the biggest strengths of Seaborn:

```python
import pandas as pd

df = pd.DataFrame({
    "age": [22, 25, 47, 52, 46, 56, 55, 60, 34, 43],
    "salary": [25000, 27000, 52000, 60000, 58000, 62000, 61000, 65000, 38000, 45000],
    "gender": ["M", "F", "M", "F", "F", "M", "M", "F", "F", "M"]
})

sns.scatterplot(x="age", y="salary", hue="gender", data=df)
plt.title('Salary vs Age Scatter Plot')
plt.show()
```

---

## Summary

| Feature         | Matplotlib | Seaborn |
|-----------------|------------|---------|
| Default Styles  | Basic       | Beautiful |
| Syntax Level    | Low         | High    |
| Works with DataFrames | Manual | Easy   |
| Plotting Complex Graphs | Tedious | Very Easy |

---

## Final Words

- **Seaborn** makes data visualization **faster, prettier, and smarter**.
- You should still know Matplotlib basics (for fine-tuning plots).
- In real-world Data Science, we usually **start with Seaborn**, and **customize with Matplotlib**.

---
 
 ## Day 31 - Data Collection Techniques

check PPT

## Day 32 - Introduction to web scraping

Automated processto extract data from websites.
Always check if apis are provided by websites, then do not do web scraping.

HTML basics for web scraping

div, p, h1, h2, a, img, table


## Day 33 - HTML for Webscraping

HTML basics for web scraping

div, p, h1, h2, a, img, table, imd

id - uniquely identifiers
class - property of an element
multiple classes can be used in elements

# Tools used for web scraping

requests - to download content from webpage
BeautifulSoup - to parse and extract data from HTML
Selenium - For websites that load data dynamically with JavaScript

Python provides powerful libraries to make web scraping easy.


## Day 34 - requests module for Data Collection

requests - python library for web scraping

https://quotes.toscrape.com
https://books.toscrape.com

1. What is requests?
requests is a Python library used to send HTTP requests easily.
It allows you to fetch the content of a webpage programmatically.
It is commonly used as the first step before parsing HTML with BeautifulSoup.
2. Installing requests
To install requests, run:

pip install requests

3. Sending a Basic GET Request
Example
import requests
 
url = "https://example.com"
response = requests.get(url)
 
# Print the HTML content
print(response.text)

Key points:

url: The website you want to fetch.
response.text: The HTML content of the page as a string.
4. Checking the Response Status
Always check if the request was successful:

print(response.status_code)

Common Status Codes
200: OK (Success)
404: Not Found
403: Forbidden
500: Internal Server Error
Good practice:

if response.status_code == 200:
    print("Page fetched successfully!")
else:
    print("Failed to fetch the page.")

5. Important Response Properties
Property	Description
response.text	HTML content as Unicode text
response.content	Raw bytes of the response
response.status_code	HTTP status code
response.headers	Metadata like content-type, server info
6. Adding Headers to Mimic a Browser
Sometimes websites block automated requests. Adding a User-Agent header helps the request look like it is coming from a real browser.

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
 
response = requests.get(url, headers=headers)

7. Handling Connection Errors
Wrap your request in a try-except block to handle errors gracefully:

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

8. Best Practices for Fetching Pages
Always check the HTTP status code.
Use proper headers to mimic a browser.
Set a timeout to avoid hanging indefinitely.
Respect the website by not making too many rapid requests.
9. Summary
requests makes it simple to fetch web pages using Python.
It is the starting point for most web scraping workflows.
Combining requests with BeautifulSoup allows for powerful data extraction.

## Day 34 Using Beautiful Soup for Data Collection

Helps to parse files to collect data

Using Beautiful Soup for Data Collection
1. What is BeautifulSoup?
BeautifulSoup is a Python library used to parse HTML and XML documents.
It creates a parse tree from page content, making it easy to extract data.
It is often used with requests to scrape websites.
2. Installing BeautifulSoup
Install both beautifulsoup4 and a parser like lxml:

pip install beautifulsoup4 lxml

3. Creating a BeautifulSoup Object
Example
from bs4 import BeautifulSoup
import requests
 
url = "https://example.com"
response = requests.get(url)
 
soup = BeautifulSoup(response.text, "lxml")

response.text: HTML content.
"lxml": A fast and powerful parser (you can also use "html.parser").
4. Understanding the HTML Structure
BeautifulSoup treats the page like a tree.
You can search and navigate through tags, classes, ids, and attributes.

Example HTML:

<html>
  <body>
    <h1>Title</h1>
    <p class="description">This is a paragraph.</p>
    <a href="/page">Read more</a>
  </body>
</html>

5. Common Methods in BeautifulSoup
5.1 Accessing Elements
Access the first occurrence of a tag:
soup.h1

Get the text inside a tag:
soup.h1.text

5.2 find() Method
Finds the first matching element:
soup.find("p")

Find a tag with specific attributes:
soup.find("p", class_="description")

5.3 find_all() Method
Finds all matching elements:
soup.find_all("a")

5.4 Using select() and select_one()
Select elements using CSS selectors.
soup.select_one("p.description")

soup.select("a")

6. Extracting Attributes
Get the value of an attribute, such as href from an <a> tag:

link = soup.find("a")
print(link["href"])

Or using .get():

print(link.get("href"))

7. Traversing the Tree
Access parent elements:
soup.p.parent

Access children elements:
list(soup.body.children)

Find the next sibling:
soup.h1.find_next_sibling()

8. Handling Missing Elements Safely
Always check if an element exists before accessing it:

title_tag = soup.find("h1")
if title_tag:
    print(title_tag.text)
else:
    print("Title not found")

9. Summary
BeautifulSoup helps parse and navigate HTML easily.
Use .find(), .find_all(), .select(), and .select_one() to locate data.
Always inspect the website's structure before writing scraping logic.
Combine BeautifulSoup with requests for full scraping workflows.

## Day 35 - Intro to Databases
Introduction to Databases
What is a Database?
A Database is an organized collection of structured information or data, typically stored electronically in a computer system. Its a way to store data in a format that is easily accessible

Example: Think of a library where books are organized by topic, author, and title – that's essentially what a database does with data.

Why Do We Need Databases?
To store, manage, and retrieve large amounts of data efficiently.
To prevent data duplication and maintain data integrity.
To allow multiple users to access and manipulate data simultaneously.
What is SQL?
SQL (Structured Query Language) is the standard programming language used to communicate with and manipulate databases.

Common operations using SQL:

INSERT – Add new records (CREATE)

SELECT – Retrieve data (READ)

UPDATE – Modify existing data (UPDATE)

DELETE – Remove records (DELETE)

These operations are usually referred to as CRUD Operations. CRUD stands for Create, Read, Update, and Delete — the four basic operations used to manage data in a database.

Comparison with Excel
Databases and Excel may seem similar at first, but they work differently under the hood.

In Excel, a sheet is like a table in a database.
Each row in the sheet is similar to a record (or entry) in a database table.
Each column in Excel corresponds to a field (or attribute) in a table.
Excel stores all data in one file, whereas a database can contain multiple related tables.
In databases, you can define strict data types and rules, which Excel doesn't enforce.
Unlike Excel, databases allow complex querying, relationships between tables, and secure multi-user access.
Think of a database as a more powerful, structured, and scalable version of Excel for data management.

Relational vs Non-relational Databases
Relational databases store data in structured tables with predefined schemas and relationships between tables (e.g., MySQL, PostgreSQL). Non-relational databases (NoSQL) use flexible formats like documents, key-value pairs, or graphs, and don’t require a fixed schema (e.g., MongoDB, Firebase). Relational is ideal for structured data and complex queries, while non-relational is better for scalability and unstructured data.

Feature	Relational (SQL)	Non-relational (NoSQL)
Structure	Tables (rows & cols)	Documents, Key-Value
Language	SQL	Varies (Mongo Query, etc.)
Schema	Fixed schema	Flexible schema
Examples	MySQL, PostgreSQL	MongoDB, Firebase
What is DBMS?
A Database Management System (DBMS) is software that interacts with users, applications, and the database itself to capture and analyze data. It allows users to create, read, update, and delete data in a structured way.

Examples: MySQL, PostgreSQL, Oracle Database, SQLite.
Functions: Data storage, retrieval, security, backup, and recovery.
What is MySQL?
MySQL is an open-source relational database management system (RDBMS) that uses SQL.

Widely used in web development
High performance and reliability
Powers platforms like WordPress, Facebook (early days), and YouTube
Real-World Use Cases
E-commerce websites to store customer orders and product listings
Banking systems to handle transactions securely
Social networks to manage user data, messages, and posts
Summary
Databases are essential for structured data storage and retrieval.

SQL is the language used to interact with relational databases.

MySQL is a popular and powerful SQL-based database system.

Understanding databases is a must-have skill for any developer or data analyst.

## Day 36 - Install My SQL

MySQL install steps

## Day 37 - Create a Database

create database Deepak
show databases;

## Day 38 - Create a Table

CREATE TABLE students(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL DEFAULT 'No Name',
age INT,
email VARCHAR(100) UNIQUE,
admission_date DATE
);

select * from students;
shows date in table
id, name, age, email, admission_date

Data Types
INT, VARCHAR(n), TEXT, DATE, DATETIME, BOOLEAN

Constraints
Primary Key, Not Null, Default, Unique, Auto_Increment, Foreign KEY

DESCRIBE students
id	int	NO	PRI		auto_increment
name	varchar(100)	NO		No Name	
age	int	YES			
email	varchar(100)	YES	UNI		
admission_date	date	YES			

## Day 39 - Modify a Table

RENAME TABLE students to cwh_students;

show tables;
DROP table cwh_students;

Alter table cwh_students RENAME COLUMN admission_date TO adm_dt;

ALTER TABLE cwh_students DROP COLUMN adm_dt;
ALTER TABLE cwh_students ADD COLUMN is_passed BOOL default True;
Alter table cwh_students MODIFY COLUMN name varchar(50) default("");
Alter table cwh_students MODIFY COLUMN name varchar(50) AFTER is_passed;

Most of the above are generally not done and mostly we fetch data from tables

## Day 40 - Inserting Data into a Table

-- CREATE DATABASE schooldb;
-- USE schooldb;

CREATE TABLE student(
id INT PRIMARY KEY,
name VARCHAR(100),
age INT,
grade VARCHAR(10),
dob DATE 
);


INSERT INTO student (id,name,age,grade,dob)
VALUES(2, "XYZ", 38, "10th", "1999-02-13");

select * from student;

Insert multiple values
INSERT into student (id,name,age,grade,dob) values
(12, "XYZ", 38, "10th", "1999-02-13"),
(22, "XYZ", 38, "10th", "1999-02-13"),
(32, "XYZ", 38, "10th", "1999-02-13"),
(42, "XYZ", 38, "10th", "1999-02-13");

## Day 41 - Selecting Data from a Table

SELECT * FROM student;
SELECT name, grade FROM student;
SELECT * FROM student WHERE age > 16;

SELECT * FROM student WHERE name LIKE '%z'
SELECT * FROM student WHERE name LIKE 'A%'

NULL means missing value

SELECT * FROM student WHERE name = NULL ----- does not work
SELECT * FROM student WHERE name IS NOT NULL

Combine conditions
SELECT * from student where grade = '9th' OR grade = '12th'

SELECT * from student where (grade = '10th' or grade = '11th') and age > 16

Sorting
SELECT * FROM student order by age DESC ----- Use ASC for ascending


## Day 42 - Updating Data in a Table
UPDATE student SET grade = '11th' where id=1;

UPDATE student SET grade = '11th' where id=1;
UPDATE student SET name = 'Deepak' where id=1;
UPDATE student SET age = 39 where id=1;

UPDATE student SET age = age + 2 where age=38;

## Day 43 - Deleting data from table

DELETE FROM student where id = 32

DELETE FROM student ---- deletes all items in table

DROP table student; ----- deletes table

## Day 44 - transactions

There are ccases where if we put a wrong condition for delete, then all our data can be deleted. So, in these scenarios 
Auto Commit - By default
Commit 
Rollback

So, we will use a transaction with a group of queries or sql statements
Transaction are atomic, consistent. isolated and Durable (ACID)

select @@autocommit -- checks if its enabled 
SET autocommit = 0 to disable

Then we need to do the following
select @@autocommit;
SET autocommit = 0;
select * from student;
START TRANSACTION;
UPDATE student set age = age+1 where id =2
COMMIT;

INSERT into student (id,name,age,grade,dob) values
(52, "Shyam", 25, "12th", "1995-02-13");

START TRANSACTION;
UPDATE student set age = age+1 where id =2
ROLLBACK;


use transactions if we want to delete or update any important data, need to be very careful with this.

## Day 45 - Getting current Date and Time

select current_date;
select current_time;
select now();
select current_timestamp()

ALTER TABLE student ADD COLUMN date_joined DATETIME DEFAULT (NOW())

INSERT into student (id,name,age,grade,dob) values
(52, "Shyam", 25, "12th", "1995-02-13");

## Day 46 - Constraints

Rules applied to table columns to enforce data integrity

1. NOT NULL
2. UNIQUE
3. DEFAULT
4. CHECK
5. NAMED Constraints

## Day 47 - Foreign keys

CREATE database school;
USE school;
CREATE TABLE classes(
class_id INT AUTO_INCREMENT PRIMARY KEY,
class_name VARCHAR(50) NOT NULL
);

CREATE TABLE students(
student_id INT AUTO_INCREMENT PRIMARY KEY,
student_name VARCHAR(100) NOT NULL,
class_id INT,
FOREIGN KEY (class_id)  REFERENCES classes(class_id)
ON UPDATE CASCADE
ON DELETE SET NULL
);

Insert into classes (class_name) values('Mathematics'),('Science'),('History');
Insert into students (student_name, class_id) values
('Alice', 1), ('Bob', 2), ('Charlie', 1);

View relationship between tables
show create table students;

output
students	CREATE TABLE `students` (
   `student_id` int NOT NULL AUTO_INCREMENT,
   `student_name` varchar(100) NOT NULL,
   `class_id` int DEFAULT NULL,
   PRIMARY KEY (`student_id`),
   KEY `class_id` (`class_id`),
   CONSTRAINT `students_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `classes` (`class_id`) ON DELETE SET NULL ON UPDATE CASCADE
 ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

 ## Day 48 - Joins in MySQL

 Inner (intersection)
 Left (Whole left table)
 right (Whole right table)
 Cross (Both left and right table)

 ## Day 49 - Union in MySQL


CREATE TABLE marks(
id INT AUTO_INCREMENT PRIMARY KEY,
subject VARCHAR(100) NOT NULL,
student_id INT,
FOREIGN KEY (student_id)  REFERENCES students(student_id)
ON UPDATE CASCADE
ON DELETE SET NULL,
score INT
);

Insert into marks (subject, score) values
('Math',92),('English',95),('Science',94), ('Math',82),('English',99),('Science',99);

select student_id from students
union
select student_id from marks;

Union removes duplicates
Union all shows duplicates

## Day 49 - Functions in MySQL

select CONCAT(student_name, ' ', class_id) as student_details from students;

# student_details
'Alice 1'
'Bob 2'
'Charlie 1'

select length(student_name) as len from students;

# len
'5'
'3'
'7'

select ROUND(DATEDIFF(NOW(), hire_date)/365, 0) as years from employees -- 0 is for decimal place

## Day 50 - views

Virtual table

select name, age, grade, ROUND(DATEDIFF(NOW(), date_joined)/365, 0) as years from student

save this query as a virtual table and perform operations like select operation. View can be updated with new column. stores references and not real data.

create or replace view deep as select name, age, grade, ROUND(DATEDIFF(NOW(), date_joined)/365, 0) as years from student;

select * from deep;

## Day 51 - indexes

Data structure which helps data retrieval faster

Create index in a table column so that retrieval of data is faster

read operations are faster but write is slow


create index idx_name_city on users(name, city)


drop index idx on employees
show index from employees

## Day 52 - Subqueries

Query inside another query

select * from employees

select first_name, last_name from employees
where salary > (select avg(salary) from employees)

select first_name, last_name from employees e
where salary >(
    select avg(salary) from employees where department=e.department
)

select * from employees -- check the exact salary based on department to get a sense of what/why we got the output in the above step


## Day 53 - Group By

select * from student;

select grade, count(*) as total from student group by grade;

# grade, total
'10th', '4'
'11th', '1'
NULL, '1'
'12th', '1'

group by also works with rollup

## Day 54 - Stored Procedures, Delimiter

select * from employees;
select first_name from employees;

; is the demiliter and for procedure, we need to change Delimiter

delimiter //

create procedure list_employees()

begin
select * from employees;
select first_name from employees;
end//

delimiter;

call list_employees()

How to give argument in SP?

create procedure get_emp_by_id(IN emp_id INT)

begin
select * from employees where employee_id = emp_id;
select first_name from employees;
end//

delimiter;

call get_emp_by_id(3)

DROP PROCEDURE IF EXISTS get_emp_by_id;


## Day 55 - Intro to Probability

Probability means Chance

Used for modeling Uncertainity

Probability of tossing a fair coin = Favourable outcome/Possible outcome

Experimental outcome = Data is used to calculate

Theoritical probability = Based on known possible outcomes Ex - Probability of getting heads in a fair coin = 0.5

Event.
SampleSpace

## Day 56 - Types of Experiments in Probability

1. Deterministic
2. Probabilistic or random


## Day 57 - Probability practice set 1

1. you roll a far six-sided die. What is the probability of getting and even number?

f(o)/p(o) = 3/6 = 1/2 = 0.5

2. 2 coins are tossed. Find the sample space associated with this random Experimental

4 = 2 ^n

3. Two six sided dice are rolled. Find probability that the sum is 7

No. of cases = 6^n = 36
(1,6)(2,5)(3,4)(4,3)(5,2)(6,1)

P = 6/36 = 1/6

4. A bag contains 3 red, 2 blue and 5 green balls. Find P(red), P(blue), P(green)

P(red) = 3/3+2+5 = 3/10
P(blue) = 2/10
P(green) = 5/10

5. A card is drawn at random from a deck of 52 cards. Find the probability of 1. getting a heart 2. getting a face card

1. P(heart) = 13/52

2. P(face card) = 4*3/52 = 12/52

## Day 58 - Basic rules of probability

Experiment
outcome
Probability
P(AUB)
P(A intrersection (and) B)
Sample space - All outcomes in an experiment
Event - subset of sample space
Mutually Exclusive Events
Independent Events
Certain Event
Impossible Event
Exhaustive Event - Tossing a die - sample space = {1,2,3,4,5,6} Event (Even) = {2,4,6}

2. The complement rule

P(A complement) = 1 - P(A)

3. Addition Rules

P(A or B) = P(A) + P(B) - P(A and B)

for mutually exclusive Events

P(A or B) = P(A) + P(B)

4. Multiplication rule

P(A and B) = P(A) * P(B) - For independent Events

For Dependent events - P(A and B) = P(A)*P(B|A) -> Probability of B given A has occurred


5. Independent vs Dependent Events

6. Mutually Exclusive Events


## Day 59 - Practice questions on probability


## Day 60 - Conditional Probability

P(B/A) = Probability of B given A has already occurred

P(A/B) = P(A intersection B)/P(B)

Law of Total Probability - B1, B2 - mutually exclusive and Exhaustive

P(A) = PB1 * PA/B1 + PB2 * PA/B2 + ...

Law of Total Probability comes from law of multiplication and Addition



## Day 61 - Baye's Theorem

P(A/B) = (PB/A * PA)/PB

## Day 62 - Probability distributions

Finding pattern in data
There is a pattern to how data is spread

1. Discrete Probability Distribution - Finite outcomes Ex - Binomial Distribution

2. Continuous Probability Distribution - Infinite values Ex - Normal Distribution

## Day 63 - Uniform Distribution

Every outcome is equally likely


Ex - rolling a die (discrete uniform)
outcomes {1,2,3,4,5,6}
P1 = 1/6, P2=1/6....

Probability Mass Function

Continuous version

Probability Density Functiuon


## Day 64 - Binomial Distribution

Discrete distribution

Probability Mass Function

## Day 65 - Normal Distribution

Most widely used

Mean

Standard Deviation

Its a continuous probability distribution and hence PDF needs to be calculated

68-95-99.7

## Day 66 - Central Limit Theorem

Heart of Statistics


Mean
Standard Deviation

## Day 67 - Machine learning

Subset of AI
Helps in creating systems which can learn from data without explicit programming and improve over a period of time

Email -> ML System -> Spam/Heatmap

ML Algos -> Supervised, Unsupervised, Reinforcement learning

Libraries - Scikit-Learn, TensorFlow, Keras, PyTorch, Pandas/NumPy

## Day 68 - How Machines Learn

Machines learn from data and improves over a period of time

Ex - spam or not spam email

imp models

Neural networks

Random Forest

Decision Trees

Support Vector Machines

Naive Bayes



## Day 69 - Installing Scikit-Learn

pip install scikit-learn

classification, Regression, Clustering, Dimensionality Reduction etc. 

## Day 70 - First model using Scikit-learn

from sklearn.tree import DecisionTreeClassifier

features = [[150, 0],
           [170,0],
           [130,1],
            [120,1]]

labels = ["apple", "apple", "orange", "orange"]

clf = DecisionTreeClassifier()

clf = clf.fit(features, labels)


prediction = clf.predict([[150, 1], [34,0]])

print(f"The fruit is {prediction[0], prediction[1]}")

# Output

The fruit is ('orange', 'apple')

## Day 71 - Using different ML Models

How to club different ML models in the same pipeline

Decision Tree plotting

from sklearn.tree import plot_tree

import matplotlib.pyplot as plt

plt.figure(figsize=(11, 6))

plot_tree(clf, feature_names=["weight", "color"], class_names=["apple", "orange"], filled=True)

Output 

Based on weight and labels the Decision tree is shown, refer the notebook

Now, lets replace DecisionTree with RandomForest Classifier

We can also use NaiveBayes classifier

## Day 72 - History of Machine Learning

1939/50 - Alan Turing - can Machines think? Did Turing test and wrote a paper

1957 - Frank Roosevelt - made perceptron -> first algo which learns from data

1980s - Comeback of ML - Perceptron, Artificial NN

1986 - Researchers bring back NN, inspired by how brain works

1997 - IBM's Deep Blue defeated Garry Kasparov, then ppl said how much can machine think and how long it can go?

1998 - Amnesh Dataset, hand written data, compute and hardware were a limitation

2006 - Deep learning saw handwriting and identified

2017 - Transformer

2018 - Google Bard

2020 - GPT 3

2022 - Chat GPT

Supervised, Unsupervised and Reinforcement learning

## Day 73 - Supervised Learning

Going to school - Kids see photo and learn animals and everything around

These are called labeled examples - then kids figure out what is what. - Supervised learning

Example - Spam email identification

Supervised Algos - 

linear regression

logistic regression

Decision Trees

Support Vector Machines

Naive Bayes

Random Forest

# Regression vs Classifier

When we want to predict a value, we do it using Regressor (value predictkarne wala) - Price of a house based on features and with 1000 records, we get house rates

Identify Color and Identify label (cat or dog) - Classifier

Example of supervised algo - Doctor predicts cancer from a number of Xrays

User labels a product review: "This is positive"

A bank labels a loan application: "This one defaulted"

More labeled examples they see, the better they get.

# If we do not have labels and just data, what happens?

## Day 74 - Unsupervised Learning

Data without any labels

We have to recognize based on a pile of Data

There is no supervision

Ex- grouping photos of a unique person.

Algos - K -Means Clustering, Hierarchical Clustering, Principal Component Analysis

It's all about finding similar items

Used when-

1. We do not have labeled data

2. We want to discover hidden patterns

3. We want to explore before making decisions.

## Day 75 - Reinforcement Learning

Learning based on available environment. Like playing a game. Get a reward when things work fine.

Humans are an example of reinforcement learning.

Depends on which actions will fetch rewards

Ex - Agent playing chess to identify strategies, reward is the score agent gets, env is chess

Self-driving cars.

Robotics.

Finance.

Games AIs.

## Day 76 - Which ML Technique to Choose

1. Recognizingthe animals

you have 10,000 images of animals. Each one is labeled as cat or dog.

2. Recognizing the Crowded

you have customer data but no labels. you do not know who buys what or why. you just have behavior logs.

3. The Game Players

Reinforcement learning (Trial and Error)


## Day 76 - Solving real world ML Problems

Practical sklearn

1. How will any work relatedto ML be used in your organization? Big Picture

2. Get the data - raw data (pdf, word, excel etc.), extract features and labels,

3. Explore and Visualize the data

4. Prepare the Data - clean, transform and format the data. Handle missing values, normalize features, and split
the data into training and testing sets.

5. Select a model and train it

6. Fine-tune your model

7. Present your solution

8. Launch, Monitor and Maintain


## Day 77 - Datasets for ML

openml.org has datasets

uci ml repository - iris dataset


## Day 78 - Training ML Algo on iris dataset

Usescikitlearn, import randomclassifier model

from sklearn.ensemble import RandomForestClassifier

Exercise done for training and test data in file quick_trainiris

## Day 79 - Measuring Accuracy of Predictions

It can be done using scikitlearn libraries.

This can be checked for multiple algorithms

from sklearn.ensemble import RandomForestClassifier

from sklearn.tree import DecisionTreeClassifier

from sklearn.naive_bayes import GaussianNB

count = 0
for i in range(0, len(actual)):
    if actual[i] == predictions[i]:
        count = count + 1
print((count*100)/len(actual))

file accuracypredictions

## Day 80 - Predicting Gurgaon city house prices

Features

distance_airport, carpet_area, type, no_of malls, no_of_rooms

Label - can be placed in any column in csv datasheet

Price

housing.csv file has details

## Day 81 - Steps for house prices problem

1. Look at the bigger picture. If the price of the house we want to purchase makes any sense or not.

2. Get the Data - write a program to automate this

3. Explore and visualize the data

4. Prepare the data

5. select a model and train it

6. Fine tune your model

7. Present and Launch your model

Questions

1. Supervised, unsupervised or reinforcement - Supervised (features are given, we need to predict labels)

2. Classification or Regression - Regression (as we have 1 variable to predict based on the features)

## Day 82 - Measuring Errors (RMSE & MAE)

Models would always have some errors and would not be able to predict with 100% accuracy

80% data - Training

20% data - Testing - we get value from model and can compare with Actual value

Testing helps us understand the error rates

M - A = Deviation or Error

Total Error = Summation(M-A) does not give proper data as errors might cancel out but that does not mean there is no error.

To get the errors, we have 2 ways -

1. RMSE (Root Mean Square Error) - get sq root, mean and square

2. MAE (Mean Absolute Error) = mod makes all values positive and hence errors do not cancel out

Ex - Actual value vector and predicted value vector - The difference gives error

## Day 83 - Analyzing the Data (EDA)










