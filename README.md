# pres_speeches
Analysis of Trump and Obama speeches on 2017-Jan-11

I was struck by the contrast in the speeches of President Obama and President Elect Trump as shown on the news on 2017-Jan-11.I wondered how the words hey used differed.

I grabbed all of the text of Trump's speech from [this BBC report](http://www.bbc.co.uk/news/world-us-canada-38536671) and removed all the reporter's questions and other speakers' words. I did leave in his reponses questions. This makes it longer. It may also make the text analysis skewed. 

This resulted in [this file][trump.txt]

Similarly, I grabbed all of President Obama's speech from this [LA Times article](http://www.latimes.com/politics/la-pol-obama-farewell-speech-transcript-20170110-story.html)

Since it was just a speech I didn'd need to remove anything other than some captions from the embeded videos.

Trump's text was 6,336 words long.
Obama's test was 4,264 words long. 

I created [Speech Words](speech_words.py) to do a simple word frequency analysis. I used a simple stop word list to screen out a few common words. 

Obama used the following words as a percentage of the full text.

Our	2.46% (his most used word of all - 105 times)
We	1.64% 
I	0.77%

This contrasts with Trump's frequency 

Our	0.38% 
We	1.18%
I	3.52% (his most used word of all - 233 times)

So, Obama's use of 'our' was almost 7 times the frequency of Trump's use.
And, Trump's use of 'I' was almost 5 times the frequency of Obama's use.

Make of this what you will!