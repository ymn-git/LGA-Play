class User:
    def __init__(
        self,
        id: int = None,
        email: str = None,
        username: str = "",
        password: str = "",
        is_active: bool = True,
        is_admin: bool = False,
        user_id: int = None,
        user_email: str = None,
    ):
        self.id = id if id is not None else user_id
        self.user_id = self.id
        self.email = email if email is not None else user_email
        self.user_email = self.email
        self.username = username
        self.password = password
        self.is_active = is_active
        self.is_admin = is_admin


Users = User
