import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
# Create your tests here.


@pytest.mark.django_db
class TestCasesForLinkAndTextCreationAndRetrieval:
  def setup_method(self):
    """Setting up test data and client"""
    self.client = APIClient()
    self.user = get_user_model().objects.create_user(username="chuks", password="mypassword123")
    self.client.force_authenticate(user=self.user)
    self.create_endpoint = "/api/v1/"


  # Test Cases for Link/Text Creation: Ensure that users can successfully store links or text properly.
  def test_valid_text_creation(self):
    """Test creating a valid text entry."""
    text_example = {"body": "This is an example text for testing"}
    response = self.client.post(self.create_endpoint, text_example, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["body"] == text_example["body"]


    # Verify if the text was saved in the database
    from contents.models import Content
    saved_text = Content.objects.get(id=response.data["id"])
    assert saved_text.body == text_example["body"]
    assert saved_text.owner == self.user


  # Test Cases for Retrieve Saved Links or Texts : Ensure users can fetch their saved content.
  def test_auth_user_retrives_saved_text(self):
    """Test checking if authenticated user can retrieve saved text."""
    text_example = {"body": "This is an example text for testing"}
    response = self.client.get(self.create_endpoint, data=text_example, format="json",)

    assert response.status_code == status.HTTP_200_OK

