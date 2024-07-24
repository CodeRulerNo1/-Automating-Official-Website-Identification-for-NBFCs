# -Automating-Official-Website-Identification-for-NBFCs
Required Libraries:
1.)pandas (py -m pip install pandas)
2.)googlesearch (py -m pip install googlesearch)
3.)os

In main.py, use find_websites function which requires 1 parameteer which denotes the path of the excel file.
A file named Output.xlsx will be produced which gives out the required information with website name.

Project Overview: Automating Official Website Identification for NBFCs
Objective:
The primary goal of this project is to develop a program that automates the process of
identifying and storing the official websites of Non-Banking Financial Companies (NBFCs)
listed in an Excel file. This solution aims to enhance efficiency and accuracy in collating web
presence information for a large number of NBFCs.
Process:
1. Data Extraction: The program will read the input Excel file and extract the necessary
details for each NBFC.
2. Web Search Automation: For each NBFC, the program will perform an automated
Google search to identify the official website.
3. Validation and Storage:
- If an official website is found, it will be stored in the database.
- If no official website is found, the program will proceed to the next NBFC.
4. Output Generation: The final output will be a new Excel file containing the list of NBFCs
along with their official websites.
Output Details:
The output Excel file will include the following columns:
- Regional Office
- NBFC Name
- Address
- Email ID
- Official Website
Key Requirements:
- Efficiency: The code should be optimized to handle large datasets efficiently, ensuring
quick processing for up to 10,000 NBFCs.
- Scalability: The solution should be designed to work with any generalized Excel file
containing the specified columns.
- Accuracy: The program should implement robust mechanisms to accurately identify official
websites, minimizing false positives and negatives.
Additional Notes:
- The program should include error handling to manage potential issues such as missing
data, connectivity problems, and search engine limitations.
- The solution should provide a progress indicator to inform users of the ongoing process,
especially when dealing with large datasets.
- Comprehensive documentation should be provided to guide users on how to operate the
program and interpret the results.
