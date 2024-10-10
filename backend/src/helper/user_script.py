from data_struct import user_var_struct

def get_user(db, username:str):
    if username in db:
        user_dict = db[username]
        return user_var_struct.UserInDB(**user_dict)

