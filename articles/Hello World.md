# Hello World

---

Today, it seems that any developer that is anybody has their own personal site. Of course, not wanting to be left out; I had to do the same. I also thought it would be nice for me to have a place to collect my ramblings, assorted writings, resume, contact information, etc.

The main problem with any personal project is actually summoning the herculean will to finish the bloody thing; somehow I managed to accomplish this.

I started off investigating multiple Static Site Generators, eventually giving up and realizing the scope of my design would not require anything nearly that complicated. Sensing an opportunity to refresh my Python skills; I realized with only two packages I could build a script that would accomplish all my needs quickly and simply.

```python
from jinja2 import Environment, FileSystemLoader
import markdown
```

With those two lines I was pretty much 70% of the way there (Maybe one day I will have the patience and lack of better judgement to write my own Markdown parser, but not today)

One can of monster and 100+ lines of Python later (which most certainly can be cut down and cleaned up which I intend on doing) I was able to service all of my needs easily. I'm sure with time it will expand as the old feature creature creeps up on me and I decide that my personal blog needs to support a chatroom or whatever.

Working with pure HTML with Jinja2 templating was a refreshing change of pace. The developers who insist on using React for something as simple as a recipe blog should follow my inspiring example and return to simpler methods of site design.

To conlude this initial post, this small project illustrated three things to me:

- I should have been using Emmet abbreviations with VSCode. To think, I was manually typing in HTML like some kind of simpleton!
- Design is one hard thing to get right
- The way boolean values are capitalized in Python irritates me an irrational amount
