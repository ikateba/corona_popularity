# corona_popularity

## How the application works
The application make use of the news api that's provided by the end point  url = ('http://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=*')
 <p> You can register and get apiKey to use instead of the star, currently you can use the one given in codes to fetch articles as well.   

## How to Run the application

<p>Make sure you have installed hadoop, hbase and python3. 
<p>Create table 'corona' in hbase by using shell command:  create 'corona', 'frequency'
<p>Then run the news.py program like any other python programs
<p>Finally, Submit the news_app.py to hadoop by command "spark-submit news_app.py". 
<p>Scan the table 'corona' on hbase shell to see new records.  
           
           
 ## How to use the Apache Kafka
 <p>You have to install kafka-python client using command "pip install kafka-python"
 <p> The Kafka consumer is already in news.py, so the only thing needed is to run the producer.py normally and the news will be printed on screen as they are received by the consumer.
