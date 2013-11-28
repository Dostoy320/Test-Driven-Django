
Working Through
===============
*Test-Driven Web Development with Python*
========================================

Using the [online version][tddp] of the book.

#### Day 1 (Chapter 1 & 2):
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

#### Day 3 (Chapter 4 & 5):
* Added code to *functional_tests.py* :
    * check if input box and placeholder text exists
    * import the selenium method "Keys" to enter a value into the box
    * check if a table containing that entered value exists
* Created the first template: *home.html* , which contains the input box and table.
* Altered *views.py* to render *home.html* rather than send a HttpResponse
* Slowly built *home.html* while running *tests.py* unittests.
* The change from canned HttpResponse to an .html template was the first look
at refactoring in a TDD environment.  Even though the refactoring was VERY basic, 
it's easy to see how well the tests back up the code.  If you break something while
refactoring, you'll know soon enough.
* Admired some nice flowcharts at the end of chapter 4

#### Day 4 (Chapter 5):
* Added code to home.html and views.py to handle a POST request
    * gave form method="POST"
    * views.home_page includes a POST.get when rendering the html
* The functional test (FT) checks for entered items on the list.
* Adding a second item creates two problems:
    * The test fails because the second item ends up replacing the first. (No persistence)
    * Duplicate code appears in the FT as we test for each item.
* Duplicate code is replaced with a helper method.  The method name doesn't contain "test"
and therefore is not run during the test, but rather called by one of the tests.
* Stumbled across the book [Code Complete][cc].
* Set up sqlite3 database by naming it in settings.py and running syncdb
* I'm suffering from some glitch that runs 400+ unit tests. Frustrating.
* Next up: Chapter 6!












[tddp]: http://chimera.labs.oreilly.com/books/1234000000754 "Test Driven Site"
[df]: http://daringfireball.net/projects/markdown/syntax
[cc]: http://www.amazon.com/Code-Complete-Practical-Handbook-Construction/dp/0735619670/ref=lh_ni_t?ie=UTF8&psc=1&smid=ATVPDKIKX0DER