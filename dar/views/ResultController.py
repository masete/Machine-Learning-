from flask import request, render_template
import wikipedia


class ReturnAnswer:
    def result(self):
        """Return an answer to the user."""
        question = request.json['replies']['question']
        answer = request.json['results']

        try:
            summary_policy = wikipedia.summary(request.json['replies']['policy'])
        except (DisambiguationError, HTTPTimeOutError, PageError, RedirectError):
            summary_policy = ''

        try:
            summary_consequence = wikipedia.summary(
                request.json['replies']['phenomenon'])
        except (DisambiguationError, HTTPTimeOutError, PageError, RedirectError):
            summary_consequence = ''

        return render_template(
            'answer.html',
            question=question,
            answer=answer,
            summary_policy=summary_policy,
            summary_consequence=summary_consequence)

