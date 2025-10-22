### ![Alt text](https://github.com/Sly-ai/ALX-Capstone-Project/blob/main/Images/ERD%20for%20Smart%20Task%20Management%20APP.png)

### 

### 

### **API Endpoints**

#### **Users App**

* `POST /api/users/register/` → Register new user

* `POST /api/users/login/` → Login and get token

* `POST /api/users/logout/` → Logout

#### **Tasks App**

* `GET /api/tasks/` → List all tasks for logged-in user

* `POST /api/tasks/` → Create new task

* `GET /api/tasks/<id>/` → Retrieve specific task

* `PUT /api/tasks/<id>/` → Update task

* `DELETE /api/tasks/<id>/` → Delete task

* `GET /api/tasks/categories/` → List categories

* `POST /api/tasks/categories/` → Add new category

