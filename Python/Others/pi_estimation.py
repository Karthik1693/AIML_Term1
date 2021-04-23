{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.141592653589793\n"
     ]
    }
   ],
   "source": [
    "import math \n",
    "\n",
    "#Factorial function\n",
    "def fact(n):\n",
    "    if n==0:\n",
    "        return 1\n",
    "    else:\n",
    "        recur = fact(n-1)\n",
    "        fact_result = n * recur\n",
    "        return fact_result\n",
    "\n",
    "#Estimating_PI Value (3.14)    \n",
    "def estimate_pi():\n",
    "    \n",
    "    flag = 0\n",
    "    k = 0\n",
    "    constant = 2 * math.sqrt(2) / 9801\n",
    "    \n",
    "    while True:\n",
    "        value_1 = fact(4*k) * (1103+ 26390*k)\n",
    "        denonimator = fact(k)**4 * 396**(4*k)\n",
    "        result = constant * value_1 / denonimator\n",
    "        flag = flag + result\n",
    "        \n",
    "        if abs(result) < 1e-15:\n",
    "            break\n",
    "        k = k+1\n",
    "        \n",
    "    result = 1 / flag\n",
    "    return result\n",
    "    \n",
    "print (estimate_pi())\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "input_list: [3, 5, 6, 7, 8, 9]\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "def binary_search(input_list,search_number):\n",
    "\n",
    "    print('input_list:',input_list)\n",
    "    higher_index = len(input_list) \n",
    "    lower_index = 0\n",
    "\n",
    "\n",
    "    for i in range(higher_index):\n",
    "        mid_index = int(lower_index +(higher_index-lower_index )/2)   \n",
    "\n",
    "        if input_list[mid_index] < search_number:\n",
    "            lower_index = mid_index + 1\n",
    "\n",
    "        if input_list[mid_index] > search_number:\n",
    "            higher_index = mid_index - 1 \n",
    "\n",
    "        if input_list[mid_index] == search_number: \n",
    "            #return \"Number\",search_number,\"indetified at the index -\",mid_index,\"in the iteration\",i+1,\".\"\n",
    "            return True\n",
    "            break\n",
    "            \n",
    "    return False\n",
    "result = binary_search([3,5,6,7,8,9],3)\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bcd"
     ]
    }
   ],
   "source": [
    "def ceaser_cypher(input_word,input_number):\n",
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
    "            if ascii_value >= 91 :\n",
    "                ascii_value = (ascii_value-91) + 65\n",
    "    \n",
    "    #Print the result\n",
    "        print(chr(ascii_value),end ='')  \n",
    "ceaser_cypher(\"abc\",1)"
   ]
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
