"""API endpoints for how.users"""

from djoser.views import UserViewSet as BaseUVS
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from how.permissions import IsAccountOwner


# Create your views here.
class UserViewSet(BaseUVS):
    """
    API endpoints for managing user accounts.

    ## Overview

    API endpoints are to manage user registration, authentication, and profile operations.
    Custom endpoints and extra actions have been added to support additional user-related features.

    ## Endpoints

    - **List Users**
    `GET /api/users`
    Retrieves a list of all user accounts.

    - **Create User (Registration)**
    `POST /api/users`
    Registers a new user. Requires user details such as username, email, and password.

    - **Retrieve User**
    `GET /api/users/{id}`
    Retrieves detailed information for the user account identified by `id`.

    - **Update User**
    `PUT /api/users/{id}`
    Fully updates the user account with the provided data.

    - **Partial Update User**
    `PATCH /api/users/{id}`
    Partially updates the user account fields.

    - **Delete User**
    `DELETE /api/users/{id}`
    Deletes the user account identified by `id`.

    ## Query Parameters

    - **search:**
    Filter users by username, first name, or last name (e.g., `?search=john`).

    - **ordering:**
    Order users by a specific field (e.g., `?ordering=-date_joined` for the most recent first).

    ## Permissions

    - **Authenticated Users:**
    Can view their own profile details.

    - **Admin/Staff Users:**
    Can list, retrieve, update, or delete any user account.

    *Note: Some endpoints (like registration) might be public while others require authentication.*

    ## Extra Actions

    This viewset extends functionality beyond the standard endpoints with additional custom actions:

    - **Join:**
    Allows users to join our platform's instructor team.
    `POST /api/users/{id}/join`
    *Request:* No body is required.
    *Response:* Returns a confirmation message.

    - **Approve:**
    Allows admins to approve join requests to our platform's instructor team.
    `POST /api/users/{id}/approve`
    *Request:* No body is required.
    *Response:* Returns a confirmation message.

    ## Example API Requests

    **List Users:**

    ```bash
    curl -X GET /api/users \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Register a New User:**

    ```bash
    curl -X POST /api/users \\
        -H "Content-Type: application/json" \\
        -d '{
                "username": "johndoe",
                "email": "john@example.com",
                "password": "securepassword"
            }'
    ```

    **Set User Password:**
    
    ```bash
    curl -X POST /api/users/1/set_password \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "old_password": "oldpassword",
                "new_password": "newsecurepassword"
            }'
    ```
    """

    lookup_field = "pk"
    search_fields = ["username", "first_name", "last_name"]
    ordering_fields = ["username", "date_joined", "last_login"]
    filterset_fields = ["username", "is_instructor"]

    def get_permissions(self):
        """Add permissions for new actions"""

        match self.action:
            case "approve":
                self.permission_classes = [IsAuthenticated, IsAdminUser]

            case "join":
                self.permission_classes = [IsAuthenticated, IsAccountOwner]

        return super().get_permissions()

    @action(methods=["post"], detail=True)
    def approve(self, request: Request, pk: int) -> Response:
        """Approve user request to be an instructor"""

        user = self.get_object()
        user.is_instructor = not user.is_instructor
        user.save()

        return Response(
            {
                "details": f"User '{user}' request {'approved' if user.is_instructor else 'rejected'}"
            },
            status=status.HTTP_200_OK,
        )

    @action(methods=["post"], detail=True)
    def join(self, request: Request, pk: int) -> Response:
        """Join our platform and become an instructor"""

        user = self.get_object()
        user.is_instructor = False if user.is_instructor is None else None
        user.save()

        return Response(
            {
                "details": (
                    "Your request to join our instructors team is sent, pending approval"
                    if user.is_instructor is False
                    else (
                        "You left our instructors team"
                        if user.is_instructor
                        else "You dismissed your request to join our instructors team"
                    )
                )
            },
            status=status.HTTP_200_OK,
        )
