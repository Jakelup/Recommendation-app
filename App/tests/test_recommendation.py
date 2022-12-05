import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from App.main import create_app
from App.database import create_db
from App.models import  Recommendation
from App.controllers import (
    get_all_recommendations,
    get_staff_by_recommendation,
    create_recommendation,
    submit_recommendation,
)


from wsgi import app
LOGGER = logging.getLogger(__name__)


class RecommendationUnitTests(unittest.TestCase):

    def test_create_recommendation(self):
        date = datetime.now()
        recommendation= Recommendation(staffId= "819000111",studentId= "816000111",body= "recommendation" ,date=date)
        assert recommendation.body == "recommendation"