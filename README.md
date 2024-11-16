# Literally just a python script to create a plaintext table

Why? Because sometimes you might need to include a table in your txt file but you have no easy way to generate one

works on my computer running python3.7

Example Usage:

Pretend we wanted to recreate this table in plaintext:

![Screenshot 2024-11-16 at 1 36 38 PM](https://github.com/user-attachments/assets/2229c7e5-5686-4cf9-b271-33b8127e55ab)

We would first call on the script including a comma-separated string of header titles \n
` 
python3 create_table.py "Age,Education,Marital Status, Gender, Political Party"
`

Then we just enter in the data each time the script asks us for it \n
`
Column values for Age: 49,25,31,45,59,29,54,42,34,53,35,21
Column values for Education: Bachelors,HS-grad,HS-grad,Bachelors,HS-grad,HS-grad,HS-grad,Bachelors,HS-grad,HS-grad,HS-grad,HS-grad
...
`

Then we get the table we want!
` 
---------------------------------------------------------------
|Age |Education |Marital Status     | Gender | Political Party |
---------------------------------------------------------------
|49  |Bachelors |Married-civ-spouse |Male    |Green            |
---------------------------------------------------------------
|25  |HS-grad   |Never-married      |Male    |Conservative     |
---------------------------------------------------------------
|31  |HS-grad   |Never-married      |Female  |Liberal          |
---------------------------------------------------------------
|45  |Bachelors |Married-civ-spouse |Male    |Green            |
---------------------------------------------------------------
|59  |HS-grad   |Divorced           |Female  |Liberal          |
---------------------------------------------------------------
|29  |HS-grad   |Never-married      |Male    |Conservative     |
---------------------------------------------------------------
|54  |HS-grad   |Divorced           |Female  |Liberal          |
---------------------------------------------------------------
|42  |Bachelors |Married-civ-spouse |Male    |Conservative     |
---------------------------------------------------------------
|34  |HS-grad   |Never-married      |Female  |Liberal          |
---------------------------------------------------------------
|53  |HS-grad   |Divorced           |Female  |Green            |
---------------------------------------------------------------
|35  |HS-grad   |Never-married      |Female  |Conservative     |
---------------------------------------------------------------
|21  |HS-grad   |Never-married      |Male    |Green            |
---------------------------------------------------------------
` 
