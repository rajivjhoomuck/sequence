The Technical Sequence
======================

The workforce of the future will demand scientists, engineers,
programmers, architects, and data scientists with a deep understanding
of math, physics, and computer science. Today, some kids go to schools where
there are good classes in these topics, but most don't. I am going to
help to fix this problem by introducing a new approach to how these
ideas are taught and creating a set of free course materials to
support that approach.

These topics are deep and difficult to master, but they are closely
related and mutually reinforcing.  It is my opinion that they should
be taught as one integrated sequence of learning experiences -- each
idea and technique stacking neatly on the ideas and techniques that came before.

These materials assume that the student can type with reasonable speed
and can solve problems using algebra. At the end the student will have
a working knowledge of:

* Math through linear algebra and vector calculus
* Python programming
* Basic algorithms and data structures (probably in C++)
* Physics that an engineer would know at the end of the first year of university
* Probability and statistics
* Basic data science and machine learning techniques

There will be 36 workbooks for this sequence. The workbooks are to be
printed out and given to the student. The student is expected to write
in the books with a pencil: there is no substitute for pencil and
paper when you are learning to solve deep problems.

There will be a collection of lecture videos to accompany the
workbooks. The videos will be freely available on the internet. In the
meantime, this sequence will utilize the great videos created by Khan
Academy.

I hope that each student has a mentor who will answer their questions
and evaluate their progress. It is my hope that the comprehensive
nature of the materials will make the job of the mentor
pretty easy.

To this end, there will be a system that generates a test and its
answer key for each workbook. Mentors will need to join the mentor
network to access this system.  It is hoped that mentors will also use
this system to suggest improvements to the materals.

Learning these ideas is a journey, and everyone will travel at
different speeds. Not everyone will make it to through to the
end. This sequence is designed to accommodate that reality. That said,
we have tried to design the workbooks so that each one will take about
40 hours of work for the average student to consume.

Where I live, schools are open about 180 days per year. Thus, if
students work for two hours per day, they will consume 9 workbooks per
year.  Working for four years, the average student should be able to complete all 36
workbooks.

The first version of the workbooks, videos, and tests will be in
American English, as that is the language that I speak. I hope that in
time I will have translations into every major language on the planet.

Teaching to the Tests
-----------------------

In order to prove the validity of this approach, we will make a point
of preparing the student to pass several nationally and
internationally normed tests. In particular, if you have
worked through all the workbooks, you should be able to pass the
following tests:

* AP Calculus BC
* AP Physics C: Mechanics
* AP Physics C: Electricity and Magnetism
* AP Statistics

Politically, it is hoped that this will also make the sequence easier to
adopt in schools.

Markup
------

As Python is the language of choice, and Python documentation uses
reStructuredText for markup, documents designed to be read on the web,
such as this one, will be created in
`ReStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_,
not Markdown.

The workbooks themselves will be written in
`LaTeX <https://www.latex-project.org>`_. The workbooks are designed to printed onto paper. In commiting to
LaTeX instead of something like reStructuredText, we giving up nice
web rendering in return for a lot of control over page layout. I am
comfortable with this compromise.

Building the books
------------------

You will need to have installed git, Python 3, and LaTeX.

(On a Mac, you should install Xcode (from the app store and it includes git) and `brew <https://brew.sh>`_. Then::

  brew install python
  brew cask install mactex-no-gui

Clone the github repository::
  
  git clone https://github.com/TheKontinua/sequence.git

You will also need some fonts from the `Google Font Collection <https://fonts.google.com/>`_ :

* Marcellus Regular
* Marcellus SC Regular
* OpenSans Bold
* OpenSans Bold Italic
* OpenSans Semi Bold
  
In the ``Build`` directory, there are three python scripts called
``build_workbook.py``, ``gather_resources.py`` and ``clean.py``. The first
time you run any of these, the file ``Build/user.cfg`` will be
created.  In this file, you can specify where ``pdflatex`` is installed
on your system.  You can also specify your default paper size (``A4``
or ``Letter``).

To build a PDF of Workbook 5 for your default paper size::

  python3 build_workbook.py 5

Intermediate files will be created in directory
``Build/Intermediate``. You can ignore that directory entirely.  The final pdf will
appear in as ``Build/workbook-05-en_US.pdf``

To build all the books::

  python3 build_workbook.py all

To build a compressed tarball with all the digital resources the student will need (including an html page will all the video links) for Workbook 5::

  python3 gather_resources.py 5

A file called ``Build/resources-05-en_US.tgz`` will appear.

To delete all the pdfs and tgz files in ``Build`` and the entire ``Intermediate`` directory::

  python3 clean.py

If you have unusual needs (strange paper size, strange location for lualatex), edit \
your ``Build/user.cfg`` file.

Programming Language and Software
---------------------------------

This sequence uses Python, and there are compromises there.  If we were
teaching to the current AP Computer Science A test, we would use
Java. However, given the exploratory nature of the programming the
student will be doing, Python and its extensive libraries are the
obvious choice.

Julia, which is a more elegant and efficient language, would also be a
good choice, but at this time Python is a more desireable skill in
industry. We will use Python.

For simple problems, the student will use a speadsheet. We are not
specifying which spreadsheet program the student must use, but the
book will use Google Sheets.

For data structures, we will probably write some code in C++. No one
loves C++, but it makes you think deeply about memory management and the heap vs.
the stack. Finally whenever a team needs code that is small, fast, and portable, C++ 
is usually the language we use.

The student can do this sequence using only open source software. This
lowers the cost of software to zero, and empowers the student by
inviting them to explore the foundational code they rely upon.

Philosophy
----------

The ideas covered by this sequence are really powerful. I think the learner's sense of 
empowerment will motivate them, if we don't abuse it by spending a lot of time on history 
and philosophy.  Instead, each chapter says "Here is an idea, and here is an example of 
how to use it."

We plan to have a mentor's guide that will include the history and
philosophy behind the ideas, which can be shared with the students
that care.

This is **not** a project-based approach. We teach an idea and give
the student a chance to solve a problem with it.  We do not assume
that the student has access to a lab.  We do not assume that there is
a teacher available to help the student set up an experiment.

Once again, this course is not for everybody. It assumes the student
is curious and willing to struggle a little to satisfy that curiosity.

More
----

Check out the `Outline <ProjectDocs/outline.rst>`_. 
