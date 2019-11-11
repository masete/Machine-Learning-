from flask import jsonify


class Status:

    def task(self, task_id):
        """Check on the status of the background tasks."""
        # remember answer_question is the callback so we use its task id
        task = Answer.answer_question.AsyncResult(task_id)
        response_data = {'task_status': task.status, 'task_id': task.id}

        if task.status == 'SUCCESS':
            response_data['results'] = task.get()
        return jsonify(response_data)