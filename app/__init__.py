# !!START
from flask import Flask, render_template, redirect
from .config import Config
from .tweets import tweets
from random import choice
from .forms.form import NewTweetForm
from datetime import date

app = Flask(__name__)

app.config.from_object(Config)



@app.route("/")
def randomTweet():
    tweet = choice(tweets)
    print(tweet)
    return render_template("index.html", tweet=tweet)

@app.route('/feed')
def feed():
    # tweets = tweets.query.all()
    print(tweets)
    return render_template('feed.html', tweets=tweets)

@app.route('/new', methods=['GET', 'POST'])
def add_tweet():
    form = NewTweetForm()

    if form.validate_on_submit():
        new_tweet = {
            'id': len(tweets) + 1,
            'author': form.author.data,
            'date': date.today(),
            'tweet': form.tweet.data,
            'likes': 0
        }
        print(new_tweet)
        tweets.append(new_tweet)

        return redirect('/feed')
    
    if form.errors:
        return form.errors

    return render_template('new_tweet.html', form=form)


# @jokes_router.route('/new', methods=['GET', 'POST'])
# def add_joke():
#     form = NewJokeForm()

#     # users = User.query.all()
#     # form.user.choices = users

#     if form.validate_on_submit():
#         new_joke = {
#             'jokeid': len(jokes) + 1,
#             'joke': form.data['joke'],
#             'punchline': form.data['punchline'],
#             'rating': form.data['rating']
#         }
#         print(new_joke)
#         jokes.append(new_joke)

#         return redirect("/jokes/all")

#     if form.errors:
#         return form.errors

#     #handle form submission stuff here

#     return render_template("joke_form.html", form=form)
