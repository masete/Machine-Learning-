
"""
Urls class , to handel request urls,
"""

from dar.views import ResultController
from dar.views import StatusController
from dar.views import QuestionAnswerController
from dar.views import IndexController


class Urls:
    """
    Class to generate urls via static method generate
    """

    @staticmethod
    def generate(app):
        """
        Generate urls on the app context
        It takes no argument
        :param: app: takes in the app variable
        :return: urls
        """

        """Ride offers routes"""
        app.add_url_rule('/', view_func=IndexController.as_view('index'), methods=['GET','POST'],
                         strict_slashes=False)
        app.add_url_rule('/question/answer/', view_func=QuestionAnswerController.as_view('question_answer'), methods=["POST, GET"],
                         strict_slashes=False)

        app.add_url_rule('/status/<string:task_id>/', view_func=StatusController.as_view('status'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/result/', view_func=ResultController.as_view('result'), methods=["POST"],
                         strict_slashes=False)

