# CSCI41-Sure

<div align="center">
<h1>🚂 TirrianTrain Project Setup Guide</h1>
<p>Welcome to the TirrianTrain project repository! This guide will help you get the application running locally for development.</p>
</div>

<!-- Add a stylish separator -->

<h2>1. 🛠️ Prerequisites</h2>
<p>Before you begin, ensure you have the following installed on your system:</p>
<ul>
<li><strong>Python</strong> (3.10 or higher recommended)</li>
<li><strong>pip</strong> (Python package installer)</li>
<li>A MariaDB/MySQL server instance (as Django uses the MySQL backend for MariaDB)</li>
</ul>

<h2>2. 🐍 Environment Setup</h2>
<p>It is highly recommended to use a virtual environment to isolate project dependencies.</p>

<h3>2.1. Create and Activate Virtual Environment</h3>
<pre><code># Create the environment (name it 'venv')
python -m venv venv

Activate the environment

For Windows (Command Prompt):

venv\Scripts\activate

For Linux/macOS:

source venv/bin/activate
</code></pre>

<h2>3. 💾 Install Dependencies</h2>
<p>Once your virtual environment is active, install all required dependencies using the provided <code>requirements.txt</code> file.</p>
<p><strong>Command:</strong></p>
<pre><code>pip install -r requirements.txt
</code></pre>

<h2>4. 🗄️ Database Configuration</h2>
<p>You need to create the database that Django will connect to. The project is configured to use the name <code>tirrianTrain</code>.</p>

<h3>4.1. Create the Database</h3>
<p>Access your MariaDB/MySQL command line client or management tool (like phpMyAdmin or MySQL Workbench) and run the following SQL command:</p>
<p><strong>SQL Command:</strong></p>
<pre><code>CREATE DATABASE tirrianTrain;
</code></pre>

<h3>4.2. Update Environment Variables</h3>
<p>Ensure you have a <strong><code>.env</code></strong> file in the root directory (and added to your <code>.gitignore</code>) containing your database connection details, including the credentials for a user who has access to the <code>tirrianTrain</code> database.</p>

<h2>5. ✨ Initialize the Project</h2>
<p>After setting up the database and installing dependencies, you must apply the initial migrations to create the necessary tables.</p>

<h3>5.1. Run Migrations</h3>
<pre><code>python manage.py migrate
</code></pre>

<h3>5.2. Create a Superuser</h3>
<p>To access the Django Admin interface, create an administrator account:</p>
<pre><code>python manage.py createsuperuser
</code></pre>

<h2>6. ▶️ Run the Application</h2>
<p>You are now ready to start the local development server!</p>
<pre><code>python manage.py runserver
</code></pre>
