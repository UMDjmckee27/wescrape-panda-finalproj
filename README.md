Web scraping is an extremely efficient way to extract data from websites automatically. It offers a consolidated way to collect information from a web page without manual copying & pasting. Packages like Requests facilitate the request and obtaining of HTML content from websites, while Beautiful Soup parses this HTML data. This enables users to navigate and extract specific information much more simply. NumPy and Pandas complement the scraping process by allowing for data manipulation, analysis, and storage. NumPy is a package for numerical computing in Python and it aids in handling arrays and mathematical operations. It's often useful when dealing with scraped data in a structured format such as tables or graphs. Pandas are essentially built on top of NumPy. They offer powerful data structures like DataFrames, simplifying the organization and analysis of the scraped data. These packages make gathering or "scraping" data from web pages much simpler, and organizing large amounts of data more feasible.

This program scrapes the website chosen which in this case is a wikipedia article ranking the highest networths in the world. It obtains the url and then sends a request using the request module to basically obtain the website. Once it has the chosen site, it parses through the data using BeautifulSoup. Once this takes place, the program finds the specified table on this wikipedia page (note that if you wish to use a different website with a different url you have to inspect element on said page and get the necessary table/graph/image elements, filling them in for "class & wikibody", "tbody", and "tr/td"). After finding the specified data on the page which is the 2023 networths table, the rows and various coloumns of the table are given variable names which then iterate through the page finding "td" and "tr" which are the html elements for the rows and data within those rows. The data thats obtained is then appended to a list (list of lists). After all of the desired data is extracted, some lines are present to smoothly transition the data into a numpy array. *However if you just want to input it straight into the .csv you can comment these lines out*. The data within the numpy array is then put into a df or DataFrame from pandas package, and converted into a .csv file with all of the corresponding data present. Thanks for using :)

References: 

https://www.geeksforgeeks.org/python-web-scraping-tutorial/
https://stackoverflow.com/questions/46582882/attributeerror-nonetype-object-has-no-attribute-find
https://www.youtube.com/watch?v=8JJ101D3knE
https://chat.openai.com/
https://blog.finxter.com/fixed-valueerror-setting-an-array-element-with-a-sequence/
