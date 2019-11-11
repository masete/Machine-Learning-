
"""
Urls class , to handel request urls,
"""



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
        app.add_url_rule('/backgroundtask', view_func=BackgroundController.as_view('get_background'), methods=["POST"],
                         strict_slashes=False)
        app.add_url_rule('/backgroundtask', view_func=BackgroundController.as_view('post_background'), methods=["GET"],
                         strict_slashes=False)


        app.add_url_rule('/status/<string:task_id>/', view_func=StatusController.as_view('status'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/result', view_func=ResultController.as_view('result'), methods=["POST"],
                         strict_slashes=False)

