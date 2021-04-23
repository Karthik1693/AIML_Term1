{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (<ipython-input-12-c9ec3ae40ed3>, line 9)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-12-c9ec3ae40ed3>\"\u001b[1;36m, line \u001b[1;32m9\u001b[0m\n\u001b[1;33m    input_word = \"abc\"\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "##################################################################################################################                                                                                                              #\n",
    "#Author: Karthikeyan Mohan\n",
    "#Student-ID : C0806321\n",
    "##################################################################################################################\n",
    "\n",
    "#def ceaser_cypher():\n",
    "\n",
    "#Get the input word\n",
    "    input_word = \"abc\"\n",
    "\n",
    "#Get the input number\n",
    "    input_number = 5 \n",
    "\n",
    "#Convet the word to char\n",
    "    input_letter = list(input_word)\n",
    "\n",
    "#normalise to number between 1 to 26\n",
    "    value_to_add = input_number % 26\n",
    "\n",
    "#Logic to handle to numbers and character\n",
    "    for i in range(0,len(input_letter)):\n",
    "        ascii_value = ord(input_letter[i])\n",
    "\n",
    "    #Handle lower case    \n",
    "        if ascii_value >= 97 and ascii_value <= 122:\n",
    "            ascii_value = value_to_add+ascii_value \n",
    "            if ascii_value >= 123 :\n",
    "                ascii_value = (ascii_value-123) + 97\n",
    "    #Handle upper case \n",
    "        if ascii_value >= 65 and ascii_value <= 90 :\n",
    "            ascii_value = value_to_add+ascii_value\n",
    "        if ascii_value >= 91 :\n",
    "            ascii_value = (ascii_value-91) + 65\n",
    "    \n",
    "    #Print the result\n",
    "    print(chr(ascii_value),end ='') \n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
