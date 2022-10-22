from flask import Blueprint

api_page = Blueprint('Api', __name__)


@api_page.route('/endpoint1', methods=['GET'])
def getAdsData():
    return 'welcome to test \n'
