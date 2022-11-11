Reading, and tasks for 3.11.2020

Must read - Vector Auto Regressions
===================================

Vector Autoregressions - James H. Stock and Mark W. Watson
https://pubs.aeaweb.org/doi/pdfplus/10.1257/jep.15.4.101

Why:
- good prose and well structured
- attachment to macroeconomist job tasks
- low enough on technical detail
- prominent journal

Extra reading
=============

Christofer Sims:
- Christopher A. Sims – Prize Lecture. <https://www.nobelprize.org/prizes/economic-sciences/2011/sims/lecture/> 

VAR and extentions (SVAR, BVAR, VECM):
- https://www.r-econometrics.com/timeseries/

Some play with notation (table with some acronyms and formulas):
- https://www.mathworks.com/help/econ/introduction-to-vector-autoregressive-var-models.html

Questions
=========

1. Large econometric models (3.11.2020)

- What were the examples of large structural econometrics models in 1960s and 1970s?
  - https://en.wikipedia.org/wiki/Klein%E2%80%93Goldberger_model
  - https://fairmodel.econ.yale.edu/main.htm 
- Provide links to specific models found on internet (team 1 vs team 2 vs EP challenge).
- What is the structure of these models? (EP - bring "white book")
- Why these models were useful and what is their failure (or "failure")?
- What was next big macroeconometric invention after VARs?
- What are other streams of macroeconometric modelling other than VARs?
- Does all macroeconomic modelling consist of econometrics?

2. Sims (3.11.2020)

- What is the most cited article of Christofer Sims in relation to VARs?
- What are key propositions of this article?
- How can one compare citations by article and article popularity? 
- Is Sims foundational article popular?

3. What is reproducible research? (later)
- What is reproducible research?
- Is there a lot of research 
- What is the difference between reproducible and replicable?
- What are researcher's motivations?
- What are scientific journal 
- Will there be more reprodicible research in economics
 
Books
=====

Heavyweight technical references
--------------------------------

1\. James Hamilton. Time Series Analysis. 1994.

2\. [Helmut Lütkepohl. New Introduction to Multiple Time Series Analysis. 2005.](https://bit.ly/3VTOmYQ)

  - Search for "inflation" and "investment" examples in Lütkepohl. What relationships are being investigated?
  - What is the role http://www.jmulti.de/ in Lütkepohl textbook and further software developement?

How do Google citations of these foundational textbooks compare? Can you explain the relationship?

  - https://scholar.google.com/citations?user=wWvHiHAAAAAJ
  - https://scholar.google.com/citations?user=FkpHoiYAAAAJ

Open source book
----------------

3\. John H. Cochrane. Time Series for Macroeconomics and Finance.
https://www.johnhcochrane.com/s/time_series_book.pdf

Courses
=======

- [Laura Mayoral 2021 course outline](http://mayoral.iae-csic.org/timeseries2021/timeseries_2021.htm)
- [Sample Lutkepohl-based course](https://www.vwl.uni-mannheim.de/media/Lehrstuehle/vwl/Trenkler/outline_mts.pdf)
 
Libraries
---------

Statmodels - VAR
https://www.statsmodels.org/dev/vector_ar.html


Hands-on project ideas (VAR)
----------------------------

1. Replicate and extend Gretl VAR example in Python statmodels
  - link: http://www.learneconometrics.com/class/5263/notes/gretl/Estimating%20a%20VAR_gretl.pdf
  - good: simple, traceable, has hansl code, potentially has a data file
  - caution: just two variables, not a big research, not plug-and-play extenible

2. Sample VAR in MATLAB:
  - link: https://www.mathworks.com/help/econ/var-model-case-study.html
  - good: has MATLAB code
  - caution: no data, doubtful model specification, not a research  
  
3. Replicate Cho and Moreno (2006) as seen in https://www.eviews.com/StructVAR/structvar.pdf.

4. Do empirical excercises in Stock and Watson textbook:
  - good: it is a textbook (supposed one can learn from it), data file provided on website
  - caution: no correct answer to check with in emprical excercises
  - link: https://www.ssc.wisc.edu/~mchinn/stock-watson-econometrics-3e-lowres.pdf
  - link 2 ("companion"): https://www.econometrics-with-r.org/14-ittsraf.html
  - problem sets:
    - E14.1 - E14.6 - US GDP
    - E14.7 - "Can you beat the market?" 

5. Live code session in R (not recommended)
  - https://www.youtube.com/watch?v=mJFZySoNfM0
  - https://github.com/hegerty/ECON343/blob/main/CAVAR.R

6. Helmut Lütkepohl textbook, dataset E1, chapter 2 (German data).

7. Review tasks set out in 1-6. Write out criteria what makes a good hands-on project
   for you:  
  - 
  -
  - 
  - 
  - 

8. Given criteria set out in 7 propose your replacition or excercise that your 
   team will do next. Pick something small that you are able to complete fast:
   - team 1
   - team 2 

More topics:

- What is reproducible research?
- National accounts, Flow of Funds
- Exchange rate modelling
- Macroeconomics model archive (DSGE)
- Reading what analysts write + replicating data charts
  - tg
  - IMF Article 4
  - other

<!--

Noted:
- https://web.pdx.edu/~crkl/ec571/ec571.htm
- https://www.econ.cam.ac.uk/people-files/emeritus/mhp1/GVAR/GVAR.html
- https://kevinkotze.github.io/ts-7-tut/
- https://www.mathworks.com/help/econ/modeling-the-united-states-economy.html
- Estimating large-scale factor models for economic activity in Germany: Do they outperform simpler models?

---

- Can anyone volunteer to show own / most favourite work?
  - keep it simple - explain to a 11th grader
  - how to replicate
  - what are success criteria in this research
  - what real-life question does this help to answer?

-->
