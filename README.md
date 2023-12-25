<h1>Sentiment Analysis for Positive and Negative Reviews</h1>

<p>This script analyzes the sentiment of a given sentence by comparing it to a collection of positive and negative reviews. It first loads and parses the positive and negative reviews from text files, then computes the sentiment of each word in the sentence by counting the occurrences of the word in the positive and negative reviews. Finally, it calculates the overall sentiment of the sentence by averaging the sentiment scores of its words.</p>

<h2>How to use</h2>

<ol>
  <li>Execute the following command: <code>python Neg_and_pos_reviews.py</code></li>
  <li>Enter a sentence to analyze, and the script will determine whether the sentence is positive, negative, or neutral.</li>
</ol>



<h2>Example</h2>

<code>python Neg_and_pos_reviews.py</code>
<p>Enter a sentence: <code>This is very good</code> </p>
<p>This sentence is positive, sentriment = <code>0.8</code></p>
