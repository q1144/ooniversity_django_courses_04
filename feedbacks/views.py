# -*- coding: utf-8 -*-
from django.contrib import messages


from django.core.urlresolvers import reverse_lazy

from django.core.mail import mail_admins

from django.views.generic.edit import CreateView


from feedbacks.models import Feedback


from feedbacks.forms import FeedbackForm


class FeedbackView(CreateView):

    model = Feedback
    success_url = reverse_lazy('feedback')
    template_name = "feedback.html"
    form_class = FeedbackForm

    def form_valid(self, form):
        app = form.save()
        mail_admins(app.subject, app.message, fail_silently=False)
        messages.success(self.request, "Thank you for your feedback! We will keep in touch with you very soon!")
        return super(FeedbackView, self).form_valid(form)