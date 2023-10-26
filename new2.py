# coding: GBK
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

def chooselesson(username,password,driver,lesson_id,teacher_id,mode):

    username1 = driver.find_element(By.ID, 'username')
    username1.send_keys(username)
    password1 = driver.find_element(By.ID, 'password')
    password1.send_keys(password)

    element = driver.find_element(By.ID, 'submit-button')
    element.click()

    tr = driver.find_element(By.TAG_NAME, 'tr')
    tr.click()
    button= driver.find_element(By.TAG_NAME, 'button')
    button.click()
    time.sleep(2)
    if mode!='0':
        while(1):
            current_time = time.strftime("%H%M", time.localtime())
            print("��ǰʱ��"+current_time+" Ŀ��ʱ��"+mode)
            if current_time == mode:
                break
        
    driver.refresh()
    driver.get('http://xk.autoisp.shu.edu.cn/CourseSelectionStudent/FuzzyQuery')
    time.sleep(20)
    element = driver.find_element(By.NAME, 'CID')
    element.send_keys(lesson_id)
    element = driver.find_element(By.NAME, 'TeachNo')
    element.send_keys(teacher_id)
    
    if mode!='0':
            element = driver.find_element(By.ID, 'QueryAction')
            element.click() 
            element = driver.find_element(By.NAME, 'checkclass')
            element.click()    
            element = driver.find_element(By.ID, 'CourseCheckAction')
            element.click()   
            print('ѡ�γɹ�')
    else:      
        times=0
        while(1):
            
            element = driver.find_element(By.ID, 'QueryAction')
            element.click()        
            # time.sleep(20)
            element = driver.find_element(By.CLASS_NAME, 'red')
            # time.sleep(20)
            if element.text == '��������':
                time.sleep(1)
                times+=1
                print('������������{}�γ���'.format(times))
                continue
            else:
                element = driver.find_element(By.NAME, 'checkclass')
                element.click()    
                element = driver.find_element(By.ID, 'CourseCheckAction')
                element.click()    

                print('ѡ�γɹ�')
                break

def save_data_to_txt(username, password, lesson_id, teacher_id, mode):
    with open('user_data.txt', 'w') as file:
        file.write(f"Username: {username}\n")
        file.write(f"Password: {password}\n")
        file.write(f"Lesson ID: {lesson_id}\n")
        file.write(f"Teacher ID: {teacher_id}\n")
        file.write(f"Mode: {mode}\n")

def load_data_from_txt():
    try:
        with open('user_data.txt', 'r') as file:
            data = file.readlines()
            username = data[0].split(': ')[1].strip()
            password = data[1].split(': ')[1].strip()
            lesson_id = data[2].split(': ')[1].strip()
            teacher_id = data[3].split(': ')[1].strip()
            mode = data[4].split(': ')[1].strip()
            return username, password, lesson_id, teacher_id, mode
    except FileNotFoundError:
        print("δ�ҵ��û������ļ�")
        return None, None, None, None, None


if os.path.exists('user_data.txt'):
    load_option = input("��⵽�����û������ļ� 'user_data.txt', ����1�������ݣ�0�������� ")
    if load_option.lower() == '1':
        username, password, lesson_id, teacher_id, mode = load_data_from_txt()
        if username is not None:
            print(f"���ļ����ص����ݣ�\nѧ��: {username}\n����: {password}\n�γ̺�: {lesson_id}\n��ʦ��: {teacher_id}\nģʽ: {mode}")
    else:
        username=input("������ѧ��")
        password=input("����������")    
        lesson_id=input("������γ̺�")
        teacher_id=input("�������ʦ��")
        mode=input("��������ֶ׵����Σ������뿪ʼʱ�䣬����˵�����0800���˵������ 0830����������0")
        flag=input("�Ƿ񱣴��û����ݣ�����1���棬0������") 
        if flag=='1':
            save_data_to_txt(username, password, lesson_id, teacher_id, mode)
            print("�����ѱ��浽�ļ� 'user_data.txt'")
else:
    username=input("������ѧ��")
    password=input("����������")    
    lesson_id=input("������γ̺�")
    teacher_id=input("�������ʦ��")
    mode=input("��������ֶ׵����Σ������뿪ʼʱ�䣬����˵�����0800���˵������ 0830����������0")
    
    flag=input("�Ƿ񱣴��û����ݣ�����1���棬0������") 
    if flag=='1':
        save_data_to_txt(username, password, lesson_id, teacher_id, mode)
        print("�����ѱ��浽�ļ� 'user_data.txt'")


driver = webdriver.Edge()
driver.get('http://xk.autoisp.shu.edu.cn')
chooselesson(username,password,driver,lesson_id,teacher_id,mode)
