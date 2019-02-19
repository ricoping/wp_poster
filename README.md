# wp_poster
<p>
You can login wordpress and fill text body and excerpt automatically.
</p>
<p>
This doesn't post an article automatically, so you can check before it goes on public and modify a litle bit.
 </p>
 
## How to use
<p>
You need to change:
</p>
wp_post.py
~~~
WP_USER = "your_user_name"
WP_PASS = "your_passwd"
WP_DOMAIN = "http://example.com"
~~~
and
~~~
import wp_post
text_body = """
Python is an interpreted, high-level, general-purpose programming language. 

Created by Guido van Rossum and first released in 1991, 

Python has a design philosophy that emphasizes code readability, notably using significant whitespace.
"""

excerpt_text = "Python is an interpreted, high-level, general-purpose programming language."
wp_post = wordpress(text_body, excerpt_text)
~~~
