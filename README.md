# Program watch_next.py 
The program uses natural language processing to 
return which movie a user should watch next if they have watched *Planet Hulk*.
I have used the library spaCy for NLP in Python as it has a special advanced
language model "en_core_web_md" for finding similarities and differences between words. 
This project hugely utilises it's method similarity. 
The program uses a function which takes the description of the film last watched,
*Planet Hulk* (but could be changed to other movies), and returns the title of the
most similar movie for the user to watch next. 

#### The database
The database of potential movies to watch next is stored in movies.txt,
it is small and needs more data added to it.
In the future, I would edit this project so it doesn't use text files as databases
as there are much harder to handle than a SQL database. I would transfer it to SQLite.

#### File semantic.py
This is background research and practice on using spaCy before I created watch_next.py
program. 
