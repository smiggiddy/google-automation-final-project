#!/usr/bin/env python3
import os
import reports
import json
import run
from datetime import date
import emails

#  ‘/tmp/processed.pdf'

def directory_files():
  """Turns fruit data into a list of lists."""
  #TODO - add folder location and email
  keys = ['name','weight','description']
  fruit_info = {}
  fruit_list = []
  for file in os.listdir('supplier-data/descriptions/'):
      line_count = 0
      #print("start of loop")
      with open('supplier-data/descriptions/' + file, mode='r') as fruit:
          #print("opening file")
          for line in fruit.readlines():
              #print("second for loop")
              if line_count < 2:
                  fruit_info[keys[line_count]] = line.strip()
                  line_count +=1
          #print("after for loop")
          fruit_list.append([fruit_info['name'],fruit_info['weight']])
  return fruit_list



def main():
    #presents report for requested data
    today_date = date.today()
    report_data = directory_files()
    space = "\n"
    paragraph_data = ""
    for line in report_data:
        paragraph_data += "<br/> Name: {} <br/>Weight: {}<br/><br/>".format(line[0], line[1])

    #print(paragraph_data)


    reports.generate_report("/tmp/processed.pdf", f"Processed updated on: {today_date}", paragraph_data)

    send the email from generated reports
    e_msg_email = emails.generate("automation@example.com","student-03-d4e234470c42@example.com",
        "Upload Completed - Online Fruit Store",
        "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
        "/tmp/processed.pdf"
        )
    emails.send(e_msg_email)

if __name__ == '__main__':
   main()
