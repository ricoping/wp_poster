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
<blockquote>
WP_USER = "your_user_name"<br/>
WP_PASS = "your_passwd"<br/>
WP_DOMAIN = "http://example.com"<br/>
</blockquote>
and<br/>
<blockquote>
import wp_post<br/>
text_body = """<br/>
Python is an interpreted, high-level, general-purpose programming language. <br/>
<br/>
Created by Guido van Rossum and first released in 1991, <br/>
<br/>
Python has a design philosophy that emphasizes code readability, notably using significant whitespace.<br/>
"""<br/>
<br/>
excerpt_text = "Python is an interpreted, high-level, general-purpose programming language."<br/>
wp_post = wordpress(text_body, excerpt_text)<br/>
</blockquote>
