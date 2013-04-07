pathsearch
==========

**File path search using solr search engine**

search front-end web for searching file path with given search key using fastest search engine (solr).

I use solr search engine for search key in string or text if large number of entry. 

1.First We stored table in database (mysql -u username -p password databasename < filename)

2. schema entry for table field.
3. data-config.xml change according to database.
4.solr indexing of given database/table
4. total 387710 indexing done by solr
5. make query syntax

In django 

create new app search and write view to send query to solr server .
response data display in table. 

for highlighting-

solr provide highlighting option to highlight search key.But it highlight word
If key present in any word then it highlight that word. 

Before use change database setting in settings.py and data-config.xml

In given code I have used 

database name - test 
database table - path
username - root
password- fasttrack

Also change solr url with core in settings.py - 

e.g   http://127.0.0.1:8983/solr/PATH/    (as in my code)

PATH is core in which all search database indexing and schema present.

PATH folder - solr-4.2.1/example/solr/PATH/  <br />
schema file - solr-4.2.1/example/solr/PATH/conf/schema.xml  <br />
data-config file - solr-4.2.1/example/solr/PATH/conf/data-config.xml <br />


