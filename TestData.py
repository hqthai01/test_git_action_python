import json
import yaml
import sys
import os

test_resource_path = os.path.dirname(__file__).replace('Scripts', 'Resources')
sys.path.append(test_resource_path)

data = json.load(open(test_resource_path +"\\TestData.json", 'r', encoding='utf-8'))
yaml_data = yaml.load(open(test_resource_path +"\\TestData.yaml", 'r', encoding='utf-8'), Loader=yaml.FullLoader)

Login_Title = data['LoginPage']['Login_Title']
Login_Failed_Message = data['LoginPage']['Login_Failed_Message']
Login_UserName = data['LoginPage']['Login_UserName']
Login_Password = data['LoginPage']['Login_Password']
Login_UserName_Failed = data['LoginPage']['Login_UserName_Failed']
Login_Password_Failed = data['LoginPage']['Login_Password_Failed']

Login_Title_YAML = yaml_data['LoginPage']['Login_Title']
Login_Failed_Message_YAML = yaml_data['LoginPage']['Login_Failed_Message']
Login_UserName_YAML = yaml_data['LoginPage']['Login_UserName']
Login_Password_YAML = yaml_data['LoginPage']['Login_Password']
Login_UserName_Failed_YAML = yaml_data['LoginPage']['Login_UserName_Failed']
Login_Password_Failed_YAML = yaml_data['LoginPage']['Login_Password_Failed']

MSHP_Title = yaml_data['MSHP_Page']['MSHP_Title']
MSHP_Menu_QLSP = yaml_data['MSHP_Page']['MSHP_Menu_QLSP']
MSHP_Menu_QLSP_SP = yaml_data['MSHP_Page']['MSHP_Menu_QLSP_SP']
MSHP_Menu_QLSP_NCC = yaml_data['MSHP_Page']['MSHP_Menu_QLSP_NCC']
MSHP_Menu_QLSP_KM = yaml_data['MSHP_Page']['MSHP_Menu_QLSP_KM']
MSHP_Menu_QLSP_HH = yaml_data['MSHP_Page']['MSHP_Menu_QLSP_HH']
MSHP_Menu_QLSP_TTK = yaml_data['MSHP_Page']['MSHP_Menu_QLSP_TTK']
MSHP_Menu_QLSP_DGCCH = yaml_data['MSHP_Page']['MSHP_Menu_QLSP_DGCCH']
MSHP_Menu_QLSP_KKK = yaml_data['MSHP_Page']['MSHP_Menu_QLSP_KKK']