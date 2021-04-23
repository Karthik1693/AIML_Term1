{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Restarting with windowsapi reloader\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\karth\\anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py:3426: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, request\n",
    "import jsonify\n",
    "import requests\n",
    "import pickle\n",
    "import numpy as np\n",
    "import sklearn\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "app = Flask(__name__)\n",
    "#model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))\n",
    "@app.route('/',methods=['GET'])\n",
    "def Home():\n",
    "    return render_template('index.html')\n",
    "if __name__==\"__main__\":\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting jsonify\n",
      "  Downloading jsonify-0.5.tar.gz (1.0 kB)\n",
      "Building wheels for collected packages: jsonify\n",
      "  Building wheel for jsonify (setup.py): started\n",
      "  Building wheel for jsonify (setup.py): finished with status 'done'\n",
      "  Created wheel for jsonify: filename=jsonify-0.5-py3-none-any.whl size=1566 sha256=7eed8135173acd623f6543d8afa6bc80b0b7c095312bf94aa1c9c42797ee3319\n",
      "  Stored in directory: c:\\users\\karth\\appdata\\local\\pip\\cache\\wheels\\ee\\c6\\ef\\643adfbd90fefe0640cb6ba3b20995a2f50ccc2c57f55b190f\n",
      "Successfully built jsonifyNote: you may need to restart the kernel to use updated packages.\n",
      "Installing collected packages: jsonify\n",
      "Successfully installed jsonify-0.5\n",
      "\n"
     ]
    }
   ],
   "source": [
    "pip install jsonify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, request\n",
    "import jsonify\n",
    "import requests\n",
    "import pickle\n",
    "import numpy as np\n",
    "import sklearn\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "app = Flask(__name__)\n",
    "model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))\n",
    "@app.route('/',methods=['GET'])\n",
    "def Home():\n",
    "    return render_template('index.html')\n",
    "\n",
    "\n",
    "standard_to = StandardScaler()\n",
    "@app.route(\"/predict\", methods=['POST'])\n",
    "def predict():\n",
    "    Fuel_Type_Diesel=0\n",
    "    if request.method == 'POST':\n",
    "        Year = int(request.form['Year'])\n",
    "        Present_Price=float(request.form['Present_Price'])\n",
    "        Kms_Driven=int(request.form['Kms_Driven'])\n",
    "        Kms_Driven2=np.log(Kms_Driven)\n",
    "        Owner=int(request.form['Owner'])\n",
    "        Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']\n",
    "        if(Fuel_Type_Petrol=='Petrol'):\n",
    "                Fuel_Type_Petrol=1\n",
    "                Fuel_Type_Diesel=0\n",
    "        else:\n",
    "            Fuel_Type_Petrol=0\n",
    "            Fuel_Type_Diesel=1\n",
    "        Year=2020-Year\n",
    "        Seller_Type_Individual=request.form['Seller_Type_Individual']\n",
    "        if(Seller_Type_Individual=='Individual'):\n",
    "            Seller_Type_Individual=1\n",
    "        else:\n",
    "            Seller_Type_Individual=0\t\n",
    "        Transmission_Mannual=request.form['Transmission_Mannual']\n",
    "        if(Transmission_Mannual=='Mannual'):\n",
    "            Transmission_Mannual=1\n",
    "        else:\n",
    "            Transmission_Mannual=0\n",
    "        prediction=model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])\n",
    "        output=round(prediction[0],2)\n",
    "        if output<0:\n",
    "            return render_template('index.html',prediction_texts=\"Sorry you cannot sell this car\")\n",
    "        else:\n",
    "            return render_template('index.html',prediction_text=\"You Can Sell The Car at {}\".format(output))\n",
    "    else:\n",
    "        return render_template('index.html')\n",
    "\n",
    "if __name__==\"__main__\":\n",
    "    app.run(debug=True)"
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
