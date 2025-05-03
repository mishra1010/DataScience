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

 