from flask import request, jsonify, url_for
from flask.views import MethodView


class QuestionAnswerController(MethodView):
    def post(self):
        cu = CallJournalUrls()

        """Start the background tasks."""
        question = request.json['question']
        keywords = cu.process_question(question)

        # use a chord here
        callback = Answer.answer_question.subtask(kwargs={'keywords': keywords})
        header = [
            CallJournalUrls.get_doaj_articles.subtask(args=(keywords, )),
            CallJournalUrls.get_Crossref_articles.subtask(args=(keywords, )),
            CallJournalUrls.get_CORE_articles.subtask(args=(keywords, ))
        ]

        task = chord(header)(callback)

        return jsonify(
            {}), 202, {
                   'Location': url_for(
                       'taskstatus', task_id=task.id, _external=True, _scheme='https')}