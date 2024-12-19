from flask import Flask, render_template, request, redirect, url_for
from compatible_test import calculate_flames_percentage, calculate_compatibility

app = Flask(__name__)

# Simulated database
users = [
    {"id": 1, "name": "Hritik","age_group": "26-35", "preference": "Outdoor activities","hobby": "Sleeping", "is_admin": True},
    {"id": 2, "name": "Alice", "is_admin": False},
    {"id": 3, "name": "Bob", "is_admin": False},
]



@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Get details from the dropdown form
        new_user_name = request.form.get('name')
        new_user_age_group = request.form.get('age_group')
        new_user_hobby = request.form.get('hobby')
        new_user_preference = request.form.get('preference')

        # Simulate adding a new user
        user_id = len(users) + 1
        users.append({
            "id": user_id,
            "name": new_user_name,
            "age_group": new_user_age_group,
            "hobby": new_user_hobby,
            "preference": new_user_preference,
            "is_admin": False
        })
        return redirect(url_for('index'))

    # Dropdown options for rendering
    hobbies = ["Reading", "Gaming", "Dancing", "Cooking", "Hiking","Sleeping"]
    preferences = ["Quiet places", "Crowded places", "Outdoor activities", "Art and culture"]
    age_groups = ["18-25", "26-35", "36-45", "46+"]
    
    return render_template('add_user.html', hobbies=hobbies, preferences=preferences, age_groups=age_groups)


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        admin_id = request.form.get('admin_id')
        user_id = request.form.get('user_id')

        admin = next((u for u in users if u['id'] == int(admin_id) and u['is_admin']), None)
        user = next((u for u in users if u['id'] == int(user_id)), None)

        if not admin or not user:
            return "Invalid selection. Only admins can test compatibility."
        # print(admin)
        # print(f"check",admin['name'],type(admin['name']))
        compatibility = calculate_compatibility(admin, user)
        flames = calculate_flames_percentage(admin['name'], user['name'])
        return render_template('result.html', admin=admin, user=user, compatibility=compatibility, flames=flames)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
