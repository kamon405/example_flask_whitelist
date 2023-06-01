from flask import Flask, request, abort

app = Flask(__name__)

# Define your list of allowed users
allowed_users = ['user1', 'user2', 'user3']

@app.route('/dashboard', methods=['GET'])
def dashboard():
    # Extract username from query parameters
    username = request.args.get('username')

    # If the user is not in the allowed list, return a 403 Forbidden response
    if username not in allowed_users:
        abort(403)

    # Otherwise, continue processing the request
    return "Welcome to the dashboard, " + username

if __name__ == '__main__':
    app.run()
