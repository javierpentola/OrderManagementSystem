# OrderManagement_System

### **Project Documentation: Order Management System**

---

#### **Project Overview**

**Project Name:** Order Management System

**Technologies Used:**
- **HTML:** For creating the structure and content of the web pages.
- **CSS:** For styling the web pages to make them visually appealing. Specifically, we used the XP.css library to give the application a retro Windows XP look.
- **JavaScript:** For adding interactivity to the frontend.
- **Python:** The main programming language used for backend development.
- **Flask:** A lightweight web framework for Python that we used to create the web application, define routes, handle requests, and connect to the database.
- **SQLite:** A lightweight database used to store the orders.

**Description:** This project is a web application designed to manage orders with two main views:
1. **Client View:** Where customers place their orders.
2. **Company View:** Where the company can see and manage all orders.

---

### **Technologies Usage**

1. **HTML:**
   - **Usage:** HTML was used to create the structure of the web pages. Each view (client and company) has its own HTML file.
   - **Files:** `index.html` for the client view and `empresa.html` for the company view.

2. **CSS:**
   - **Usage:** CSS was used for styling the HTML elements to make the application visually appealing. The XP.css library was used to give the application a classic Windows XP look and feel.
   - **Files:** `styles.css`, with a link to the XP.css library in the HTML files.

3. **JavaScript:**
   - **Usage:** JavaScript was used to add interactivity to the web pages, such as form validation and dynamic updates.
   - **Files:** `scripts.js`.

4. **Python:**
   - **Usage:** Python was the main programming language for backend development. It was used to write the application logic, handle requests, and process data.
   - **Files:** `app.py` and `models.py`.

5. **Flask:**
   - **Usage:** Flask was used as the web framework to build the web application. It helped in defining routes, handling HTTP requests, rendering templates, and connecting to the database.
   - **Key Components:**
     - **Routes:** Defined in `app.py` to map URLs to functions.
     - **Templates:** HTML files rendered by Flask using the `render_template` function.
     - **Database:** Connected using SQLAlchemy, a Flask extension for ORM.

6. **SQLite:**
   - **Usage:** SQLite was used as the database to store order data. It is a lightweight, file-based database that is ideal for small to medium-sized applications.
   - **Files:** `database.db` (the database file).

---

### **Setup and Usage Instructions**

To use the project after downloading the code, follow these steps:

1. **Clone the Repository:**
   - Use `git clone` to clone the repository to your local machine.

2. **Navigate to the Project Directory:**
   - Change your working directory to the project folder.
   ```bash
   cd Order_manager_with_Flask
   ```

3. **Create and Activate a Virtual Environment:**
   - Create a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   ```

4. **Install Dependencies:**
   - Install the required Python packages using `pip`.
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```

5. **Run the Application:**
   - Start the Flask development server.
   ```bash
   flask run
   ```

6. **Access the Application:**
   - Open a web browser and go to `http://127.0.0.1:5000` for the client view.
   - To access the company view, go to `http://127.0.0.1:5000/empresa`.

7. **Viewing the Database:**
   - The database file (`database.db`) is located in the project directory. You can use tools like DB Browser for SQLite or the SQLite command line to view and manage the database contents.
