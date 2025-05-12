# URL Shortener Project

A simple URL shortener built with Flask that allows users to shorten long URLs and manage them.

## Features
- Shorten long URLs
- Redirect to the original URL via the shortened URL
- Manage and delete URLs
- Analytics page to track URL usage

## Prerequisites
- [Docker](https://www.docker.com/) installed on your system
- (Optional) Python 3.9+ and `pip3` if running locally without Docker

---

## Run the Project

### Using Docker
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/colot025/url-shortener.git
   cd url-shortener

2. **Build the Docker Image**:
   ```bash
   docker build --no-cache -t url-shortener-app .

3. **Run the Docker Container**:
   ```bash
   docker run -d -p 5000:5000 --name url-shortener url-shortener-app

4. **Access the Application**:
   Open your browser and navigate to [http://localhost:5000](http://localhost:5000).

5. **Use the App to Shorten URLs**:
   - Type or paste the link you want to shorten in the "Original URL" field and then click "Submit" to generate your shorten url.
   - If you would like to use a create a custom name for the shorten url, add a custom short ID and click "Submit".
   - After generating a shortened URL, click the **View Analytics** button.
   - You will be redirected to a page displaying:
      - Total views count.
   - Click the **Regenerate Link** button for an existing shortened URL.
   - The application will generate a new shortened URL for the same original link.
   - Use the new link as needed.

---

### Running Locally
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/colot025/url-shortener.git
   cd url-shortener
   ```

2. **Install Dependencies**:
   install the required packages:
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python3 main.py
   ```

4. **Access the Application**:
   Open your browser and navigate to [http://localhost:5000](http://localhost:5000).

5. **Use the App to Shorten URLs**:
   - Type or paste the link you want to shorten in the "Original   URL" field and then click "Submit" to generate your shorten url.
   - If you would like to use a create a custom name for the shorten url, add a custom short ID and click "Submit".
   - After generating a shortened URL, click the **View Analytics** button.
   - You will be redirected to a page displaying:
      - Total views count.
   - Click the **Regenerate Link** button for an existing shortened URL.
   - The application will generate a new shortened URL for the same original link.
   - Use the new link as needed.

---

## Testing the Project

### Running Unit Tests
To run the unit tests, execute:
```bash
python3 -m unittest test_shortener_app.py 
```

Ensure all tests pass before deployment.

### Testing with Docker
1. **Run the Tests in the Docker Container**:
   ```bash
   docker exec url-shortener python3 -m unittest test_shortener_app.py 
   ```

2. **View Logs**:
   If a test fails, check the container logs:
   ```bash
   docker logs url-shortener
   ```

## Resources

The following resources were utilized in the development of this project:

- [Flask Documentation](https://flask.palletsprojects.com/) - Official documentation for Flask, used as the core web framework.
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/) - Used for styling the front-end UI components.
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/) - For database interactions and ORM.
- [Docker Documentation](https://docs.docker.com/) - Referenced for containerization setup and deployment.
- [Python 3.9 Documentation](https://docs.python.org/3.9/) - To reference Python's standard library and syntax.
- [unittest.TestCase.debug](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug) - For debugging unit tests in Python.
- Various Stack Overflow discussions and Q&A for resolving specific coding challenges.

