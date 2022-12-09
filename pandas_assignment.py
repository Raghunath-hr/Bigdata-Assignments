"""
ASSIGNMENT

Q1) Load CSV in pandas dataframe
>>>		first you need to import pandas
		then you can load csv file with "read_csv" function 

ex:-

import pandas as pd

import_csv_file = pd.read_csv("path/to/import/file")

Q2) Check datatype of column in pandas dataframe
>>>		.dtype - with using this attribute you can know the datatype of the 	
			perticular column.
		.dtypes - will display the datatype for all the cloumns in the 				datatframe

		syntax: DataFrameName['ColumnName'].dtype

ex:-

import pandas as pd

data = {
	"name":["raghu", "rajesh", "mahesh"],
	"age":[12, 14, 34],
	"education":['pg', 'ug', 'doctor']
}

df = pd.DataFrame(data)

df['age'].dtype  #knowing the datatype for the age column

Q3) Select rows in pandas dataframe based on condition
>>>		we can select rows based on perticular column value using ['<', '>', 
			'=', '!=', '<=', '>='] operators


ex:-

import pandas as pd

data = {
	"name":['raghu', 'rajesh', 'mahesh'],
	"age":[12,14,34]
	"education":['pg', 'ug', 'doctor']
}

#create dataframe
df = pd.DataFrame(data, columns = ['name', 'age', 'education'])

#selecting rows based on condition
sort_result = df[df['age']<30]

#using "loc[]" method
sort_result = df.loc[df['age']<30]

Q4) Rename columns in dataframe
>>>		*using rename() method

data = {
	"name":['raghu', 'rajesh', 'mahesh'],
	"age":[12,14,34]
	"education":['pg', 'ug', 'doctor']
}

df = pd.DataFrame(data)

data.rename(columns = {'name':'NAME'}, inplace = True)
	#here inplace=True works as changing the original dataframe

		*by assigning new column names

data.columns = ['NAME', 'AGE', 'EDUCATION']

Q5) Drop columns in pandas dataframe
>>>		*drop() method

data = {
	"Fruits":['apple', 'banana', 'mango']
	"Vegitables":['potato', 'kukumber', 'tomato']
	"Trees":['coconut', 'mango', 'black walnut']
	"Rivers":['Ganga', 'Godavari', 'Narmada']
}

df = pd.dataFrame(data)
df.drop(['Fruits'], axis=1)

		*remove columns based on index

df.drop(df.colums[[1,2]], axis=1, inplace=True)

		*using iloc[] and drop() method

df.drop(df.iloc[:, 1:3], inplace=True, axis=1) #removing columns vegitables and trees
											
		*using loc[] and drop() method

df.drop(df.loc[:, 'Vegitables':'Rivers'].columns, axis=1)

		*using iterative way

for col in df.columns:
	if 'e' in col:
		del df[col]

		*using pop() method

df.pop('Fruits')

Q6) Find unique values in a column of pandas dataframe
>>>		* unique() method

data = {
	"name":['raj', 'chintu', 'raj']
}

df = pd.DataFrame(data)

df.name.unique()

Q7) Number of missing valus in each column of pandas DataFrame
>>>		* isnull().sum() Method

#consider we have list of tuples and have to create dataframe with columns and indices

students = [('Ankit', 22, 'Up', 'Geu'),
           ('Ankita', np.NaN, 'Delhi', np.NaN),
           ('Rahul', 16, 'Tokyo', 'Abes'),
           ('Simran', 41, 'Delhi', 'Gehu'),
           ('Shaurya', np.NaN, 'Delhi', 'Geu'),
           ('Shivangi', 35, 'Mumbai', np.NaN ),
           ('Swapnil', 35, np.NaN, 'Geu'),
           (np.NaN, 35, 'Uk', 'Geu'),
           ('Jeet', 35, 'Guj', 'Gehu'),
           (np.NaN, np.NaN, np.NaN, np.NaN)
            ]

df = pd.DataFrame(students, columns=['name', 'age', 'place', 'college'],
					index = ['a','b','c','d','e','f','g','h','i','j','k'])

print(df)
#the boolean dataframe
print("\nshow the bollean dataframe: \n\n", df.isnull())

#count total NaN values in each column
print("\nTotal null values in each column as: \n\n", details.isnull().sum())


Q8) Fill missing values in pandas with specific values
>>>		* ffil() method :-By default this method replaces missing values along 			   the row. The NaN is replaced with the values from the previous 	
			row of that cell.


students = [('Ankit', 22, 'Up', 'Geu'),
           ('Ankita', np.NaN, 'Delhi', np.NaN),
           ('Rahul', 16, 'Tokyo', 'Abes'),
           ('Simran', 41, 'Delhi', 'Gehu'),
           ('Shaurya', np.NaN, 'Delhi', 'Geu'),
           ('Shivangi', 35, 'Mumbai', np.NaN ),
           ('Swapnil', 35, np.NaN, 'Geu'),
           (np.NaN, 35, 'Uk', 'Geu'),
           ('Jeet', 35, 'Guj', 'Gehu'),
           (np.NaN, np.NaN, np.NaN, np.NaN)
            ]

df = pd.DataFrame(students, columns=['N','A','P','C'],
					index=['1','2','3','4','5','6','7','8','9','10'])

print(df) 
print("\nBoolean Dayaframe: \n\n", df.isnull())

df2 = df.ffil() #replacing NaN with previous row values
df3 = df.ffil(axis=1) #replacing values with previous column values
df4 = df['A'].fillna(90) #replacing nan values with 90
df5 = df['A'].fillna(100, inplace=True) #modification in original dataframe
df6 = df['N'].fillna('Jayram', inplace=True)

print(df)


Q9) Concatenate two pandas dataframe
>>>		* concat() method

df1 = pd.DataFrame(np.random.randint(25, size=(4,4)),
					index=['a','b','c','d'],
					columns=['1','2','3','4'])
df2 = pd.DataFrame(np.random.randint(25, size=(4,4)),
					index=['e','f','g','h'],
					columns=['1','2','3','4'])

df3 = pd.DataFrame(np.random.randint(25, size=(4,4)),
					index=['Q','W','E','R'],
					columns=['11','12','13','14'])
df4 = pd.DataFrame(np.random.randint(25, size=(4,4)),
					index=['Q','W','E','R'],
					columns=['15','16','17','18'])


vertical_concat = pd.concat([df1,df2])
print(horizontal_concat)
horizontal_concat = pd.concat([df3,df4], axis=1)
print(vertical_concat)


Q10) Merge pandas dataframe on a specific column
>>>		* DataFrame.merge()

df1 = pd.DataFrame({'Name':['Raju', 'Rani', 'Geeta', 'Sita', 'Sohit'],
                    'Marks':[80, 90, 75, 88, 59]})
  
# creating another dataframe with different data
df2 = pd.DataFrame({'Name':['Raju', 'Divya', 'Geeta', 'Sita'],
                    'Grade':['A', 'A', 'B', 'A'],
                    'Rank':[3, 1, 4, 2 ],
                    'Gender':['Male', 'Female', 'Female', 'Female']})

print(df1,"\n\n", df2)

df3 = df1.merge(df2)
print(df3)


Q11) Group data in pandas
>>>		*groupby() method is used to group data in pandas, we can pass 
			multiple column names.

Q12) Pivot pandas dataframe
>>>		the pivot() function is used to reshape a given dataframe organized by 
			given index/column values.


df = pd.DataFrame({
		'fff':['one','one','one','two','two','two'],
		'bbb':['p','q','r','p','q','r'],
		'baa':[2.2,3.3,4.4,5.6,6.7,7.9],
		'zzz':['h','i','j','k','l','m']
	})

print(df,"\n\n")

df1 = df.pivot(index='fff',columns='bbb',values='baa')
print(df1)

Q13) Change the datatype of column in pandas DataFrame
>>>		* astype() method
		consider above same example where column 'baa' has datatype of float
		lets change it to int

df2 = df.baa.astype(int)
print(df2.dtypes)

Q14) Sort pandas DataFrame by specific column
>>>		* sort_values() method:-this method sorts dataframe in ascending or 			descending order or passed column

#list of tuples
students = [('Ankit', 22, 'Up', 'Geu'),
           ('Ankita', 31, 'Delhi', 'Gehu'),
           ('Rahul', 16, 'Tokyo', 'Abes'),
           ('Simran', 41, 'Delhi', 'Gehu'),
           ('Shaurya', 33, 'Delhi', 'Geu'),
           ('Harshita', 35, 'Mumbai', 'Bhu' ),
           ('Swapnil', 35, 'Mp', 'Geu'),
           ('Priya', 35, 'Uk', 'Geu'),
           ('Jeet', 35, 'Guj', 'Gehu'),
           ('Ananya', 35, 'Up', 'Bhu')
            ]

df = pd.DataFrame(students, columns=['Name','Age','City','Education'],
							index=['a','b','c','d','e','f','g','h','i','j'])


print(df)
print("\n\n\n")
sorted_dataframe = df.sort_values(by='Name')
# print(sorted_dataframe)

#if dulicates are in Name column then we can sort using two columns

sorted_dataframe2 = df.sort_values(by = ['Age'])
# print(sorted_dataframe2)

#sort by descending order use (ascending=False)
sorted_dataframe3 = df.sort_values(by = ['Age'], ascending=False)
print(sorted_dataframe3)


Q15) Create copy of pandas DataFrame
>>>		* DataFrame.copy() this method is used to cpy the dataframe

Q16) Filter rows of pandas dataframe by multiple conditions
>>>		
"""

"""
#create DataFrame
import pandas as pd
	
df = pd.DataFrame({'team': ['A', 'A', 'B', 'B', 'C'],
                   'points': [25, 12, 15, 14, 19],
                   'assists': [5, 7, 7, 9, 12],
                   'rebounds': [11, 8, 10, 6, 6]})

print(df)

#filtering using 'and'(&)

# print(df[(df.points>15) & (df.assists<9)])
# print(df[(df.team=='A') & (df.rebounds==11)])
# print(df[(df.team=='C') & (df.assists==12)])

#filtering using 'or'(|)
print(df[(df.points==25) | (df.points==10)])

#Filter on multiple conditions using list

test_filter_list = [11,6]

print(df[df.rebounds.isin(test_filter_list)])

"""

"""
# Q17) Calculate mean of column in pandas DataFrame
>>>		* mean() method

import pandas as pd
df = pd.DataFrame({'team': ['A', 'A', 'B', 'B', 'C'],
                   'points': [25, 12, 15, 14, 19],
                   'assists': [5, 7, 7, 9, 12],
                   'rebounds': [11, 8, 10, 6, 6]})

print(df['points'].mean())

Q18) Calculate standerd deviation in pandas DataFrame
>>>		* std() method is used to calculate standerd deviation

import pandas as pd
df = pd.DataFrame({'team': ['A', 'A', 'B', 'B', 'C'],
                   'points': [25, 12, 15, 14, 19],
                   'assists': [5, 7, 7, 9, 12],
                   'rebounds': [11, 8, 10, 6, 6]})

print(df['points'].std())

Q19) Calculate correlation between two columns in pandas dataframe
>>>		

import pandas as pd
df = pd.DataFrame({'team': ['A', 'A', 'B', 'B', 'C'],
                   'points': [25, 12, 15, 14, 19],
                   'assists': [5, 7, 7, 9, 12],
                   'rebounds': [11, 8, 10, 6, 6]})


#consider we have to find correlation between columns points & rebounds

col1, col2 = 'points', 'rebounds'

find_correlation = df[col].corr(df[col2])
print(find_correlation)

Q20) select specif column in pandas dataframe using thier lables
>>>	

import pandas as pd
df = pd.DataFrame({'team': ['A', 'A', 'B', 'B', 'C'],
                   'points': [25, 12, 15, 14, 19],
                   'assists': [5, 7, 7, 9, 12],
                   'rebounds': [11, 8, 10, 6, 6]})

#selecting columns with their names
df_column = df['team']
df_coulmn2 = df['points']	
df_column3 = df['assists']


Q21) select specific rowns in pandas dataframe with thier lables
>>>		* loc['index_name'] method

import pandas as pd
df = pd.DataFrame({'team': ['A', 'A', 'B', 'B', 'C'],
                   'points': [25, 12, 15, 14, 19],
                   'assists': [5, 7, 7, 9, 12],
                   'rebounds': [11, 8, 10, 6, 6]})


row_index = df.set_index('team', inplace=True)
select_row = df.loc['points','team']
print(select_row)

Q22) Sort DataFrame by specific column
>>>		* sort_values() method:-this method sorts dataframe in ascending or 			descending order or passed column

#list of tuples
students = [('Ankit', 22, 'Up', 'Geu'),
           ('Ankita', 31, 'Delhi', 'Gehu'),
           ('Rahul', 16, 'Tokyo', 'Abes'),
           ('Simran', 41, 'Delhi', 'Gehu'),
           ('Shaurya', 33, 'Delhi', 'Geu'),
           ('Harshita', 35, 'Mumbai', 'Bhu' ),
           ('Swapnil', 35, 'Mp', 'Geu'),
           ('Priya', 35, 'Uk', 'Geu'),
           ('Jeet', 35, 'Guj', 'Gehu'),
           ('Ananya', 35, 'Up', 'Bhu')
            ]

df = pd.DataFrame(students, columns=['Name','Age','City','Education'],
							index=['a','b','c','d','e','f','g','h','i','j'])


print(df)
print("\n\n\n")
sorted_dataframe = df.sort_values(by='Name')
# print(sorted_dataframe)

#if dulicates are in Name column then we can sort using two columns

sorted_dataframe2 = df.sort_values(by = ['Age'])
# print(sorted_dataframe2)

#sort by descending order use (ascending=False)
sorted_dataframe3 = df.sort_values(by = ['Age'], ascending=False)
print(sorted_dataframe3)


Q23) Create new column in pandas DataFrame based on values of another column
>>>		* apply() method is used to create new column based on existing one

import pandas as pd
df = pd.DataFrame({'team': ['A', 'A', 'B', 'B', 'C'],
                   'points': [25, 12, 15, 14, 19],
                   'assists': [5, 7, 7, 9, 12],
                   'rebounds': [11, 8, 10, 6, 6]})

col1, col2 = 'points','rebounds'
find_correlation = df[col1].corr(df[col2])
print(round(find_correlation))

df['test_column'] = df.apply((lambda row: row.points + 10),axis=1)
df['new_column'] = df.apply((lambda row: row.team + "$"), axis=1)
print(df)

Q24) Remove duplicated from DataFrame
>>>		* drop_duplicates() method is used to reove duplicated from df
import pandas as pd

boxes = {'Color': ['Green','Green','Green','Blue','Blue','Red','Red','Red'],
         'Shape': ['Rectangle','Rectangle','Square','Rectangle','Square','Square','Square','Rectangle']
        }
df = pd.DataFrame(boxes, columns = ['Color', 'Shape'])

print(df)
print("----------------------------")
df_after_removing_dupli = df.drop_duplicates() #removes duplicated from df
print(df_after_removing_dupli)
print('------------------------------')
#if you want remove duplicated only from specific column
#you need to use subset=['column_name']

remove_dupli_from_column = df.drop_duplicates(subset=['Color'])
print(remove_dupli_from_column)



Q25) Difference between .loc[] and .iloc[] method
>>>		loc :- loc method selects rows and columns with specific lables(names)
		iloc :- iloc method selects rows and columns at spesific integer positions(index values)


"""






