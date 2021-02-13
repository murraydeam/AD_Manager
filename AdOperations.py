import adClient
import csv

# CSV for Adding new Users
global csv 
#User will selelcta  file from the UI as the CSV
csv = ""

def csv_add(csv):

  with open('sample.csv', mode='r') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      for row in csv_reader:
          username = row['username']
          employee_id = row['employee_id']
          official_name = row['official_name']
          print(username, employee_id, official_name)
          adClient.create_user(username, employee_id, official_name, active=True)

def csv_delete(csv):

  with open('sample.csv', mode='r') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      for row in csv_reader:
          username = row['username']
          employee_id = row['employee_id']
          official_name = row['official_name']
          print(username, employee_id, official_name)
          adClient.manage_user(username, mode='delete')
