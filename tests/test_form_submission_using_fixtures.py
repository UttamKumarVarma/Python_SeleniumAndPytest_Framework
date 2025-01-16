import pytest

from page_objects.FormSubmissionHomePage import SubmissionHomepage
from utilities.BaseClass import BaseClass


class TestFormSubmission(BaseClass):

    def test_form_submission(self, get_data):
        form_submission = SubmissionHomepage(self.driver)

        form_submission.go_to_home_page()

        form_submission.enter_name(get_data["user_name"])

        form_submission.enter_password(get_data["password"])

        form_submission.click_on_submit_button()



    @pytest.fixture(params = [{"user_name":"uttam", "password":"varma"},{"user_name":"nithin", "password":"varma"},{"user_name":"raju", "password":"varma"}])
    def get_data(self, request):
        return request.param
