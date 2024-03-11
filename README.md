
📗 Table of Contents
Attrition Meter
🛠 Built With
Tech Stack
Key Features
💻 Getting Started
Prerequisites
Setup
Install
Usage
👥 Authors
🔭 Future Features
🤝 Contributing
⭐️ Show your support
🙏 Acknowledgments
📝 License
<!-- PROJECT DESCRIPTION -->
Attrition Application <a name="about-project">
Attrition Application is a data application that allows users to interact with a machine learning model, view data visualizations on the data and see the values of their input saved for future use.

Features
- Gender-- Whether the customer is a male or a female
- SeniorCitizen -- Whether a customer is a senior citizen or not
- Partner -- Whether the customer has a partner or not
- Dependents -- Whether the customer has dependents or not
- Tenure -- Number of months the customer has stayed with the company
- Phone Service -- Whether the customer has a phone service or not
- MultipleLines -- Whether the customer has multiple lines or not
- InternetService -- Customer's internet service provider (DSL, Fiber Optic, No)
- OnlineSecurity -- Whether the customer has online security or not (Yes, No, No Internet)
- OnlineBackup -- Whether the customer has online backup or not (Yes, No, No Internet)
- DeviceProtection -- Whether the customer has device protection or not (Yes, No, No internet service)
- TechSupport -- Whether the customer has tech support or not (Yes, No, No internet)
- StreamingTV -- Whether the customer has streaming TV or not (Yes, No, No internet service)
- StreamingMovies -- Whether the customer has streaming movies or not (Yes, No, No Internet service)
- Contract -- The contract term of the customer (Month-to-Month, One year, Two year)
- PaperlessBilling -- Whether the customer has paperless billing or not (Yes, No)
- Payment Method -- The customer's payment method
- MonthlyCharges -- The amount charged to the customer monthly

🛠 Built With <a name="built-with">
Streamlit <a name="streamlit">
<details> <summary>GUI</summary>

<ul> <li><a href="">Streamlit</a></li> </ul>
</details>

<details> <summary>Database</summary>

<ul> <li><a href="">Microsoft SQL Server</a></li> </ul>
</details>

<details> <summary>Language</summary>

<ul> <li><a href="">Python</a></li> </ul>
</details>

<details> <summary>Model</summary>

<ul> <li><a href="">Sklearn</a></li> </ul>
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- Features -->
Key Features <a name="key-features">
A data application that presents visualizations on both the exploratory data and the KPIs
A predicitons page to predict by specifying the model you want to use
View proprietory data loaded in real-time form the remote server
Predictions are save for further analysis in the future and users can view the history of their prediction input values
<p align="right">(<a href="#readme-top">back to top</a>)</p>
image

<!-- GETTING STARTED -->
💻 Getting Started <a name="getting-started">
To get a local copy up and running, follow these steps.

Prerequisites
In order to run this project you need:

Python
Streamlit
Setup
Clone this repository to your desired folder:

  cd my-folder
  git clone https://github.com/analystdee/attrition-application.git
Change into the cloned repository

  cd Attrition-Meter
  
Create a virtual environment


python -m venv env

Activate the virtual environment

    virtual_env/Scripts/activate
Install
Here, you need to recursively install the packages in the requirements.txt file using the command below

   pip install -r requirements.txt
Usage
To run the project, execute the following command:

    streamlit run main.py

A webpage opens up to view the app
Login to the app with username=khadija and password:123
Finally test a prediction by clicking on the predicitons page
Note: Users may not be able to access the View Data page as the secrets file is not checked into git
<!-- AUTHORS -->
👥 Authors <a name="authors">
🕵🏽‍♀️ khadija ahmed

GitHub: [My GitHub Profile](https://github.com/analystdee)
LinkedIn: [My Linked in Profile](www.linkedin.com/in/khadija-abdallah)
<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- FUTURE FEATURES -->
🔭 Future Features <a name="future-features">
Add a front end application for users
<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- CONTRIBUTING -->
🤝 Contributing <a name="contributing">
Contributions, issues, and feature requests are welcome!

Feel free to check the issues page.

<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- SUPPORT -->
⭐️ Show your support <a name="support">
If you like this project kindly show some love, give it a 🌟 STAR 🌟

<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- ACKNOWLEDGEMENTS -->
🙏 Acknowledgments <a name="acknowledgements">
I would like to thank all the free available resource made available online and AZUBI AFRICA for equipping me 
with necessary data analytics knowledge.

<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- LICENSE -->
📝 License <a name="license">
This project is MIT licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>