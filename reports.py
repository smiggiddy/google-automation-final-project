#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import date


def generate_report(filename, title, additional_info):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  empty_line = Spacer(1,20)

  report.build([report_title, empty_line, report_info, empty_line])
# today_date = date.today()

# generate("/home/smig/tmp/processed.pdf", f"Processed updated on: {today_date}", report_table)
