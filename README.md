# text_filtering_on_keywords
This is a code that can be used to filter projects or applications with a particular theme, given by keywords. You need to type your server, your database, your query and the name of the theme keywords that you want to search the projects for. The advantage of this code over SQL query is that you can make it as an executable file or web graphic interface, thereby useful for multiple themes search and can be delegated to people without knowledge of SQL.

This code is used to import data from a SQL server, clean and filter it based on a list of keywords.

## How to use

Replace 'YOUR SERVER' and 'YOUR DATABASE' with the appropriate values for your server and database.

Replace 'YOUR QUERY' with the desired SQL query to retrieve the data from the server. Alternatively, you can import data from an Excel or CSV file by uncommenting and using the appropriate pandas function (e.g. df = pd.read_excel('Example.xlsx')).

Replace 'YOUR KEYWORD1' and 'YOUR KEYWORD2' with the desired keywords to search for in the data.

Run the code. The resulting data will be saved to an Excel file called 'filtering text on keywords.xlsx'.

## Notes

The data should have columns named 'Title', 'Summary', and 'Keywords'.

The data will be cleaned by removing punctuation, tokenizing, removing stop words, and lemmatizing.

The resulting data will only include rows that contain at least one of the keywords in the 'found words' column.
