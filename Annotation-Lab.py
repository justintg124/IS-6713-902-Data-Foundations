{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Python: Annotation\n",
    "\n",
    "Blank notebook to be used for class exercises.\n",
    "\n",
    "Name: Justin Gould\n",
    "\n",
    "qbu192\n",
    "\n",
    "AI Statement: You must choose one of the following two statements:\n",
    "\n",
    "“I did not use generative AI for this assignment.”\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 1\n",
    "\n",
    "Complete the Sentiment Annotation Survey on Canvas. \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 2\n",
    "\n",
    "Judge the annotations in following Data:\n",
    "\n",
    "sentiment.txt\n",
    "\n",
    "You are the judge. Look over the annotations and come up with the following:\n",
    "- What is your judgment for the correct entity + sentiment annotation?\n",
    "- How would you amend the annotation guidelines to solicit more consistent annotations?\n",
    "\n",
    "While judging the annotations, keep track of them below:\n",
    "\n",
    "1. Your judgement for the first tweet here\n",
    "2. Your judgement for the second tweet here\n",
    "3. ....\n",
    "\n",
    "\n",
    "How many of your judgements match the majority view?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## judgements: \n",
    "1. Target: ISIS Class: Negative\n",
    "2. Target: U.S. Senate Class: Neutral\n",
    "3. Target: Camp David Class: Neutral\n",
    "4. Target: Sean Spicer Class: Positive\n",
    "5. Target: Triumph Class: Positive why: this is typically a positive verb\n",
    "6. Target: Fake News Media Class: Negative\n",
    "7. Target: Cincinnati Class: Neutral\n",
    "8. Target: Ivanka Class: Ivanka\n",
    "9. Target: ISIS Class: Negative\n",
    "10. Target: Emmanuael Macron Class: Positive\n",
    "11. Target: Condolences Class Negative\n",
    "12. Target: Thank you Class: Positive\n",
    "13. Target: Putin Class: Neutral\n",
    "14. Target: President Trump Class: Positive\n",
    "15. Target: Congress Class: Neutral\n",
    "16. Target: V.A. Class: Nuetral\n",
    "17. Target: Joint Base Andrews Class: Neutral\n",
    "18. Target: USA Class: Positive\n",
    "19. Target: America Class: Positive\n",
    "20. Target: Tremendous Class: Positive\n",
    "\n",
    "How many of your judgements match the majority view?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 3\n",
    "\n",
    "Manually calculate Cohen's kappa for the tables in the slides and put your answers below:\n",
    "\n",
    "Answers here"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.0\n"
     ]
    }
   ],
   "source": [
    "# WRITE CODE HERE\n",
    "\n",
    "po=50/100\n",
    "\n",
    "p_a_puppy=50/100\n",
    "p_b_puppy=50/100\n",
    "p_a_chicken=50/100\n",
    "p_b_chicken=50/100\n",
    "\n",
    "pe=p_a_puppy*p_b_puppy+p_a_chicken*p_b_chicken\n",
    "\n",
    "kappa=(po-pe)/(1-pe)\n",
    "print(kappa)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 4\n",
    "\n",
    "Write code to calculate and print the cohen's kappa between rater1 and rater2.\n",
    "\n",
    "Hint: You will need to create the confusion matrix (matrix of how many times each rater agrees for each item)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "rater1 = ['yes','no','yes','yes','yes','yes','no','yes','yes']\n",
    "rater2 = ['yes','no','no','yes','yes','yes','yes','yes','yes']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# WRITE CODE HERE\n",
    "r1_yes_r2_yes=0\n",
    "r1_no_r2_no=0\n",
    "r1_yes_r2_no=0\n",
    "r1_no_r2_yes=0\n",
    "\n",
    "for r1, r2 in zip(rater1,rater2):\n",
    "    if r1=='yes' and r2=='yes':\n",
    "        r1_yes_r2_yes+=1\n",
    "    elif r1=='no'and r2=='no':\n",
    "        r1_no_r2_no+=1\n",
    "    elif r1=='yes' and r2=='no':\n",
    "        r1_yes_r2_no+=1\n",
    "    else:\n",
    "        r1_no_r2_yes+=1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6 1 1 1\n"
     ]
    }
   ],
   "source": [
    "# WRITE CODE HERE\n",
    "print(r1_yes_r2_yes, r1_no_r2_no, r1_yes_r2_no,r1_no_r2_yes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.7777777777777778 0.654320987654321\n",
      "0.35714285714285715\n"
     ]
    }
   ],
   "source": [
    "# WRITE CODE HERE\n",
    "po=(r1_yes_r2_yes+r1_no_r2_no)/(r1_yes_r2_yes+r1_no_r2_no+r1_yes_r2_no+r1_no_r2_yes)\n",
    "\n",
    "p_r1_yes=(r1_yes_r2_yes+r1_yes_r2_no)/(r1_yes_r2_yes+r1_no_r2_no+r1_yes_r2_no+r1_no_r2_yes)\n",
    "p_r1_no=(r1_no_r2_no+r1_no_r2_yes)/(r1_yes_r2_yes+r1_no_r2_no+r1_yes_r2_no+r1_no_r2_yes)\n",
    "p_r2_yes=(r1_yes_r2_yes+r1_no_r2_yes)/(r1_yes_r2_yes+r1_no_r2_no+r1_yes_r2_no+r1_no_r2_yes)\n",
    "p_r2_no=(r1_no_r2_no+r1_yes_r2_no)/(r1_yes_r2_yes+r1_no_r2_no+r1_yes_r2_no+r1_no_r2_yes)\n",
    "\n",
    "pe=p_r1_yes*p_r2_yes + p_r1_no*p_r2_no\n",
    "print(po,pe)\n",
    "kappa=(po-pe) / (1-pe)\n",
    "\n",
    "print(kappa)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "counts ={}\n",
    "for r1, r2 in zip(rater1, rater2):\n",
    "    counts['r1_'+r1+'_r2_'+r2]=counts.get('r1_'+r1+'_r2_'+r2,0)+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'r1_yes_r2_yes': 6, 'r1_no_r2_no': 1, 'r1_yes_r2_no': 1, 'r1_no_r2_yes': 1}"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "counts"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
