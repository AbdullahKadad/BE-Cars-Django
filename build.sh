# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt



# Create a superuser
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('root', 'root@example.com', '1234')" | python manage.py shell