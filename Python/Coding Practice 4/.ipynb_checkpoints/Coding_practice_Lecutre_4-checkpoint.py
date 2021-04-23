{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 164,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Hi Jon snow !! You are invited to the party.\n",
      "\n",
      "Hi Sheldon Cooper !! You are invited to the party.\n",
      "\n",
      "Hi Alexis Rose !! You are invited to the party.\n"
     ]
    }
   ],
   "source": [
    "#3.4 Guest list\n",
    "guest_list = ['Jon snow','Sheldon Cooper','Alexis Rose']\n",
    "for i in guest_list:\n",
    "    print(\"\\nHi\",i,\"!! You are invited to the party.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Unfortunately Sheldon Cooper is not able to make it to the party.\n",
      "\n",
      "Hi Jon snow !! You are invited to the party.\n",
      "\n",
      "Hi Steven Smith !! You are invited to the party.\n",
      "\n",
      "Hi Alexis Rose !! You are invited to the party.\n"
     ]
    }
   ],
   "source": [
    "#3.5 Changing guest list\n",
    "guest_list = ['Jon snow','Sheldon Cooper','Alexis Rose']\n",
    "print(\"Unfortunately\",guest_list[1],\"is not able to make it to the party.\")\n",
    "guest_list =  ['Jon snow','Steven Smith','Alexis Rose']\n",
    "for i in guest_list:\n",
    "    print(\"\\nHi\",i,\"!! You are invited to the party.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "We have got one more table to accomadate 3 more people\n",
      "\n",
      "Hi Alysa Healy !! You are invited to the party.\n",
      "\n",
      "Hi Jon snow !! You are invited to the party.\n",
      "\n",
      "Hi Ellse Perry !! You are invited to the party.\n",
      "\n",
      "Hi Steven Smith !! You are invited to the party.\n",
      "\n",
      "Hi Alexis Rose !! You are invited to the party.\n",
      "\n",
      "Hi MS Dhoni !! You are invited to the party.\n"
     ]
    }
   ],
   "source": [
    "#3.6 More guests\n",
    "\n",
    "print(\"We have got one more table to accomadate 3 more people\")\n",
    "guest_list =  ['Jon snow','Steven Smith','Alexis Rose']\n",
    "guest_list.insert(0,\"Alysa Healy\")\n",
    "guest_list.insert(2,\"Ellse Perry\")\n",
    "guest_list.append(\"MS Dhoni\")\n",
    "\n",
    "for i in guest_list:\n",
    "    print(\"\\nHi\",i,\"!! You are invited to the party.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sorry to inform you all that we have space only for 2 person\n",
      "---------------------------------------------------------------\n",
      "\n",
      "Hi Alysa Healy !! You are invited to the party.\n",
      "\n",
      "Hi Jon snow !! You are invited to the party.\n"
     ]
    }
   ],
   "source": [
    "#3.7 Shrinking guest list\n",
    "print(\"Sorry to inform you all that we have space only for 2 person\")\n",
    "print(\"---------------------------------------------------------------\")\n",
    "for i in range(2,len(guest_list)):\n",
    "        print(\"\\nApologies!!\",guest_list.pop(),\"we are not able to acccomodate you.\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Hi Alysa Healy !! You are invited to the party.\n",
      "\n",
      "Hi Jon snow !! You are invited to the party.\n"
     ]
    }
   ],
   "source": [
    "for i in guest_list:\n",
    "    print(\"\\nHi\",i,\"!! You are invited to the party.\")  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 175,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "for i in range(0,len(guest_list)):\n",
    "    del guest_list[0]\n",
    "guest_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 198,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Actual List: ['Kulu-Manali', 'Toronto', 'Los Vegas', 'Paris', 'Fiji']\n",
      "Sorted list: ['Fiji', 'Kulu-Manali', 'Los Vegas', 'Paris', 'Toronto']\n",
      "Actual List: ['Kulu-Manali', 'Toronto', 'Los Vegas', 'Paris', 'Fiji']\n",
      "Sorted list in Descending: ['Toronto', 'Paris', 'Los Vegas', 'Kulu-Manali', 'Fiji']\n",
      "Actual List: ['Kulu-Manali', 'Toronto', 'Los Vegas', 'Paris', 'Fiji']\n",
      "Actual List after using reverse: ['Fiji', 'Paris', 'Los Vegas', 'Toronto', 'Kulu-Manali']\n",
      "Actual List changing it back orginal order: ['Kulu-Manali', 'Toronto', 'Los Vegas', 'Paris', 'Fiji']\n",
      "Actual List after using sort(): ['Fiji', 'Kulu-Manali', 'Los Vegas', 'Paris', 'Toronto']\n",
      "Actual List changing it back orginal order: ['Toronto', 'Paris', 'Los Vegas', 'Kulu-Manali', 'Fiji']\n"
     ]
    }
   ],
   "source": [
    "#3.8 Seeing the world\n",
    "\n",
    "places_list = [\"Kulu-Manali\",\"Toronto\",\"Los Vegas\",\"Paris\",\"Fiji\"]\n",
    "\n",
    "print(\"Actual List:\",places_list)\n",
    "print(\"Sorted list:\",sorted(places_list))\n",
    "print(\"Actual List:\",places_list)\n",
    "print(\"Sorted list in Descending:\",sorted(places_list,reverse=True))\n",
    "print(\"Actual List:\",places_list)\n",
    "\n",
    "places_list.reverse()\n",
    "print(\"Actual List after using reverse:\",places_list)\n",
    "places_list.reverse()\n",
    "print(\"Actual List changing it back orginal order:\",places_list)\n",
    "\n",
    "places_list.sort()\n",
    "print(\"Actual List after using sort():\",places_list)\n",
    "places_list.sort(reverse=True)\n",
    "print(\"Actual List changing it back orginal order:\",places_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 199,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No. of people invited for dinner: 0\n"
     ]
    }
   ],
   "source": [
    "#3.9 Dinner Guest\n",
    "print(\"No. of people invited for dinner:\",len(guest_list))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 227,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Japan', 'China', 'Canada', 'Germany', 'Pakistan']\n",
      "['Japan', 'China', 'Canada', 'Germany', 'Pakistan', 'India']\n",
      "0\n",
      "['Japan', 'China', 'Australia', 'Canada', 'Germany', 'Pakistan', 'India']\n",
      "['Japan', 'China', 'Australia', 'Canada', 'Germany', 'Pakistan']\n",
      "['Japan', 'China', 'Canada', 'Germany', 'Pakistan']\n",
      "['Canada', 'China', 'Germany', 'Japan', 'Pakistan']\n",
      "['Pakistan', 'Japan', 'Germany', 'China', 'Canada']\n"
     ]
    }
   ],
   "source": [
    "#3.10 Every function\n",
    "country_list = [\"Japan\",\"China\",\"Canada\",\"Germany\",\"Pakistan\"]\n",
    "print(country_list)\n",
    "country_list.append(\"India\")\n",
    "print(country_list)\n",
    "print(country_list.index(\"Japan\"))\n",
    "country_list.insert(2,\"Australia\")\n",
    "print(country_list)\n",
    "country_list.pop()\n",
    "print(country_list)\n",
    "del country_list[2]\n",
    "print(country_list)\n",
    "country_list.sort()\n",
    "print(country_list)\n",
    "country_list.reverse()\n",
    "print(country_list)"
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
