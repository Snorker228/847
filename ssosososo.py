#1. Метод GET
import requests

def get_all_students():
    """
    Возвращает список всех студентов.
    """
    url = "http://127.0.0.1:80/students"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_student_by_id(student_id):
    """
    Возвращает информацию о конкретном студенте.
    
    Args:
        student_id (int): Номер студента.
    """
    url = f"http://127.0.0.1:80/students/{student_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

#2. Метод POST

import requests

def add_new_student(student_data):
    url = "http://127.0.0.1:80/students"
    response = requests.post(url, json=student_data)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

#3. Метод PUT

import requests

def update_student_info(student_id, updated_data):
    url = f"http://127.0.0.1:80/students/{student_id}"
    response = requests.put(url, json=updated_data)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

#4. Метод DELETE

import requests

def delete_student(student_id):
    url = f"http://127.0.0.1:80/students/{student_id}"
    response = requests.delete(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

#5. 