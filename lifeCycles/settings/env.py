import os
import dotenv

def load_dotenv():
    dotenv.load_dotenv(
        os.path.join(os.path.dirname(__file__), '.env')
    )

def set_django_settings_module(value='lifeCycles.settings.development'):
    load_dotenv()
    os.environ['DJANGO_SETTINGS_MODULE'] = os.getenv('DJANGO_SETTINGS_MODULE', value)