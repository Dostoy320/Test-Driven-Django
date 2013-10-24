
Working Through
===============
*Test-Driven Web Development with Python*
========================================

Using the [online version][tddp] of the book.

#### Day 1 (Chapter 1&2):
* Python3, PIP-1.4.1, and Selenium 2.35.0 installed.
  (already had Django 1.5.4 installed)
* created the first test: *functional_tests.py*
* created a Django project called **superlists**
* initialized the Test-Driven-Django repository
* learned a bit of Markdown from [Daring Fireball][df]

#### Day 2 (Chapter 3):
* Started a Django app called **lists**
* Created 2 unit tests:
    * check if root url resolves to the homepage
    * check if the homepage contains html and title content
* Edited urls.py to point root to lists.views.home_page
* Added home_page() to views.py, returns HttpResponse() with the desired content.
* created command line alias pmt="python3 manage.py test"















[tddp]: http://chimera.labs.oreilly.com/books/1234000000754 "Test Driven Site"
[df]: http://daringfireball.net/projects/markdown/syntax