# Answers

1. What’s your proudest achievement? It can be a personal project or something
   you’ve worked on professionally. Just a short paragraph is fine, but I’d
   love to know why you’re proud of it.

    My proudest achievement was when I was working in one of my previous companies, we were using aws as the cloud provider to host our applications and to run our batch and big data jobs. We used to get around $20000 USD per month as bill. I did some analysis and some reading and went though our existing architecture and identified places where cost could be reduces and implemented those things in 2 months and after that we were able to save $5000 USD every month in aws bills. And I got appreciation for the work I did.
    This is one of my proudest achievement I can think of that occurred recently.

2. What's a personal project you're currently working on? This could be a
   coding side project, hobby, or otherwise real world project you're working
   on.

    I started to learn flutter few months back and did a course on Udemy. Recently I though of making a moview review app using flutter.
    I started designing the app last month and I have been working on architecting the app and worked on couple of backend APIs for the app to use. Just started working on the app whenever I get time and am learning along with it.

3. Tell us about a technical book or article you read recently, why you liked
   it, and why we should read it.

    Sometime back I wanted to learn terraform and started with an online course. But I couldnt complete even 25% of it. I had been searching for a good resource to learn terraform, which is when I came across the Terraform Up and Running book.
    I started the book and completed it with in a week. It was very simply writted with nice explanations and easy to do demos with best practices highlighted throughout and specifically it had a chapter on testing the terraform infrastructure code written using terratest.
    I felt, the book was very beginner friendly and it should be the first resource a developer who wants to know terraform should read.

4. Tell us about one of your favorite products (physical or software) and one
   specific aspect that makes it truly great.

   Again, my answer would be terraform (I have become a big fan). It is a very nice and extendable tool. Its so cool when I came across it first it felt like magic. Writing code to create infrastructure sure felt like magic.
   It is cloud agnostic and extremely customizable. We can write our own providers to do the tasks which we require to.
   The concept of modules which enables developers to share terraform code is another aspect that make terraform great.
   
5. In this repo is a `data.json` file. It contains an imaginary example set
   of data a customer might need to migrate from one system to another. It's a
   JSON encoded array of objects. The customer understands some of the data
   might be bad and wants to know which records are invalid so they can ensure
   the new system will only have valid data. Write a program that will read
   in the data and mark any records:

   1. That are a duplicate of another record
   2. `name` field is null, missing, or blank
   3. `address` field is null, missing, or blank
   4. `zip` is null, missing, or an invalid U.S. zipcode

   Each record has an ID but that should only be used to identify a record,
   not for validity or duplication testing (eg, two records may be identical
   but have different IDs).

The output of the program should list the IDs of each invalid or duplicate
record, one per line. In the case of duplicates, mark both.

Example:

```
123ba
439a2
99abc
bac34
```

  ## Run

  To run the solution

  ```bash
  $ python solution.py
  ```

  To run unit tests

  ```bash
  $ pip install -r requirements.txt
  $ pytest --cov-config=.coveragerc --cov-report term --cov=. test.py
  ```

  or in docker

  ```bash
  $ docker build -t challenge-solution:latest .
  $ docker run challenge-solution:latest
  ```
