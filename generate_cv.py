"""
CV Generator for Francesco Colicino
Using ReportLab to create a professional PDF resume
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Page dimensions
PAGE_WIDTH, PAGE_HEIGHT = A4

# Colors
DARK_RED = HexColor("#8B0000")
LIGHT_GRAY = HexColor("#666666")
DARK_GRAY = HexColor("#333333")

# Margins
LEFT_MARGIN = 2 * cm
RIGHT_MARGIN = 2 * cm
TOP_MARGIN = 2 * cm

def draw_header(c, y_position):
    """Draw the header section with photo, name and title"""
    # Photo dimensions
    photo_width = 3.5 * cm
    photo_height = 3.3 * cm
    photo_x = LEFT_MARGIN
    photo_y = y_position - photo_height + 30

    # Draw photo
    c.drawImage("photo.jpg", photo_x, photo_y, width=photo_width, height=photo_height, preserveAspectRatio=True, mask='auto')

    # Text starts after the photo
    text_x = LEFT_MARGIN + photo_width + 0.5 * cm

    # Name
    c.setFont("Helvetica", 32)
    c.setFillColor(DARK_GRAY)
    c.drawString(text_x, y_position, "Francesco")

    c.setFont("Helvetica-Bold", 32)
    c.drawString(text_x + 160, y_position, "Colicino")

    # Title
    y_position -= 25
    c.setFont("Helvetica", 11)
    c.setFillColor(DARK_RED)
    c.drawString(text_x, y_position, "DATA SCIENTIST")

    # Contact info
    y_position -= 20
    c.setFont("Helvetica", 10)
    c.setFillColor(DARK_GRAY)
    c.drawString(text_x, y_position, "☎ 3341133931  |  ✉ colicino.francesco@gmail.com")

    # Summary
    y_position -= 30
    c.setFont("Helvetica-Oblique", 10)
    c.setFillColor(LIGHT_GRAY)
    summary = "I have been working as a Data Scientist for over 4 years with special focus on time series analysis and"
    c.drawString(LEFT_MARGIN, y_position, summary)
    y_position -= 14
    c.drawString(LEFT_MARGIN, y_position, "forecasting. My daily tools are R and Python.")

    return y_position - 30

def draw_section_header(c, y_position, title):
    """Draw a section header with colored first letters"""
    c.setFont("Helvetica-Bold", 16)
    
    # Draw colored part (first 3 letters)
    c.setFillColor(DARK_RED)
    colored_part = title[:3]
    c.drawString(LEFT_MARGIN, y_position, colored_part)
    
    # Draw rest of title
    c.setFillColor(DARK_GRAY)
    rest_part = title[3:]
    colored_width = c.stringWidth(colored_part, "Helvetica-Bold", 16)
    c.drawString(LEFT_MARGIN + colored_width, y_position, rest_part)
    
    # Draw line
    y_position -= 5
    c.setStrokeColor(LIGHT_GRAY)
    c.setLineWidth(0.5)
    title_width = c.stringWidth(title, "Helvetica-Bold", 16)
    c.line(LEFT_MARGIN + title_width + 10, y_position, PAGE_WIDTH - RIGHT_MARGIN, y_position)
    
    return y_position - 20

def draw_employment(c, y_position):
    """Draw employment section"""
    y_position = draw_section_header(c, y_position, "Employment")
    
    # Job 1 - FOORBAN
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(DARK_GRAY)
    c.drawString(LEFT_MARGIN, y_position, "Data Scientist")
    
    c.setFont("Helvetica", 10)
    c.setFillColor(LIGHT_GRAY)
    c.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, y_position, "Milan")
    
    y_position -= 15
    c.setFont("Helvetica", 10)
    c.setFillColor(DARK_GRAY)
    c.drawString(LEFT_MARGIN, y_position, "FOORBAN")
    c.setFillColor(LIGHT_GRAY)
    c.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, y_position, "Dic 2026 -> Present")
    
    # Bullet points
    y_position -= 18
    bullets = [
        "Softwares and Tools: Python, SQL"
    ]
    
    c.setFont("Helvetica", 9)
    c.setFillColor(DARK_GRAY)
    for bullet in bullets:
        c.drawString(LEFT_MARGIN + 10, y_position, "•  " + bullet)
        y_position -= 14

    # Job 2 - COOP
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(DARK_GRAY)
    c.drawString(LEFT_MARGIN, y_position, "Data Scientist")
    
    c.setFont("Helvetica", 10)
    c.setFillColor(LIGHT_GRAY)
    c.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, y_position, "Milan")
    
    y_position -= 15
    c.setFont("Helvetica", 10)
    c.setFillColor(DARK_GRAY)
    c.drawString(LEFT_MARGIN, y_position, "COOP CONSORZIO NORD OVEST")
    c.setFillColor(LIGHT_GRAY)
    c.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, y_position, "Oct 2021 -> Nov 2025")
    
    # Bullet points
    y_position -= 18
    bullets = [
        "CRM Analysis, customer segmentation with marketing goals;",
        "A/B tests and inference on promos;",
        "Bayesian analysis with PyMC",
        "Forecast of churn customers through prediction model;",
        "Time series analysis and forecast on sales and stock data;",
        "Softwares and Tools: R, Python, SQL"
    ]
    
    c.setFont("Helvetica", 9)
    c.setFillColor(DARK_GRAY)
    for bullet in bullets:
        c.drawString(LEFT_MARGIN + 10, y_position, "•  " + bullet)
        y_position -= 14
    
    # Job 3 - BV-TECH
    y_position -= 10
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(DARK_GRAY)
    c.drawString(LEFT_MARGIN, y_position, "Data Scientist")
    
    c.setFont("Helvetica", 10)
    c.setFillColor(LIGHT_GRAY)
    c.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, y_position, "Milan")
    
    y_position -= 15
    c.setFont("Helvetica", 10)
    c.setFillColor(DARK_GRAY)
    c.drawString(LEFT_MARGIN, y_position, "BV-TECH")
    c.setFillColor(LIGHT_GRAY)
    c.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, y_position, "Nov 2020 -> Nov 2021")
    
    y_position -= 18
    bullets2 = [
        "Extraction and manipulation (ETL) of data in SAS;",
        "Data visualization through Microstrategy dashboards;",
        "Software and Tools: SAS, SQL, Microstrategy"
    ]
    
    c.setFont("Helvetica", 9)
    c.setFillColor(DARK_GRAY)
    for bullet in bullets2:
        c.drawString(LEFT_MARGIN + 10, y_position, "•  " + bullet)
        y_position -= 14
    
    return y_position - 15

def draw_education(c, y_position):
    """Draw education section"""
    y_position = draw_section_header(c, y_position, "Education")
    
    # Master's
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(DARK_GRAY)
    c.drawString(LEFT_MARGIN, y_position, "University of Milano-Bicocca")
    c.setFont("Helvetica", 10)
    c.setFillColor(LIGHT_GRAY)
    c.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, y_position, "Milan")
    
    y_position -= 15
    c.setFont("Helvetica", 10)
    c.setFillColor(DARK_GRAY)
    c.drawString(LEFT_MARGIN, y_position, "MASTER'S DEGREE IN STATISTICAL SCIENCES 103/110")
    c.setFillColor(LIGHT_GRAY)
    c.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, y_position, "Oct 2017 -> Mar 2020")
    
    # Bachelor's
    y_position -= 25
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(DARK_GRAY)
    c.drawString(LEFT_MARGIN, y_position, "University of Milano-Bicocca")
    c.setFont("Helvetica", 10)
    c.setFillColor(LIGHT_GRAY)
    c.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, y_position, "Milan")
    
    y_position -= 15
    c.setFont("Helvetica", 10)
    c.setFillColor(DARK_GRAY)
    c.drawString(LEFT_MARGIN, y_position, "BACHELOR'S DEGREE IN STATISTICAL SCIENCES 85/110")
    c.setFillColor(LIGHT_GRAY)
    c.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, y_position, "Oct 2011 -> Mar 2017")
    
    return y_position - 25

def draw_skills(c, y_position):
    """Draw skills section"""
    y_position = draw_section_header(c, y_position, "Skills")
    
    skills_data = [
        ("Programming Languages", "PYTHON, R, SQL, BASH"),
        ("Visualization Tools", "MICROSTRATEGY"),
        ("Version Control", "GIT"),
        ("Text Editors", "RSTUDIO, VISUAL STUDIO CODE"),
        ("Operating System", "LINUX, WINDOWS"),
        ("Cloud Provider", "AWS"),
        ("DevOps", "DOCKER")
    ]
    
    for i in range(len(skills_data)):
        skill_title, skill_value = skills_data[i]
        if((i+1)%2==0):
            c.setFont("Helvetica-Bold", 10)
            c.setFillColor(DARK_GRAY)
            c.drawRightString(PAGE_WIDTH-RIGHT_MARGIN, y_position, skill_title)

            y_position -= 14
            c.setFont("Helvetica", 9)
            c.setFillColor(LIGHT_GRAY)
            c.drawRightString(PAGE_WIDTH-RIGHT_MARGIN, y_position, skill_value)
            y_position -= 18
        else:
            c.setFont("Helvetica-Bold", 10)
            c.setFillColor(DARK_GRAY)
            c.drawString(LEFT_MARGIN, y_position, skill_title)

            # y_position -= 14
            c.setFont("Helvetica", 9)
            c.setFillColor(LIGHT_GRAY)
            c.drawString(LEFT_MARGIN, y_position-14, skill_value)
            # y_position -= 18
    
    return y_position - 5

def draw_certifications(c, y_position):
    """Draw certifications section"""
    y_position = draw_section_header(c, y_position, "Certifications")
    
    # HackerRank
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(DARK_GRAY)
    c.drawString(LEFT_MARGIN, y_position, "Hacker Rank")
    
    y_position -= 15
    c.setFont("Helvetica", 10)
    c.drawString(LEFT_MARGIN, y_position, "SQL (BASIC) SQL (INTERMEDIATE)")
    c.setFillColor(LIGHT_GRAY)
    c.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, y_position, "2024")
    
    y_position -= 14
    c.setFont("Helvetica", 8)
    c.setFillColor(HexColor("#0066CC"))
    c.drawString(LEFT_MARGIN + 10, y_position, "• https://www.hackerrank.com/certificates/8e0767711de3")
    y_position -= 12
    c.drawString(LEFT_MARGIN + 10, y_position, "• https://www.hackerrank.com/certificates/9cedf64a161a")
    
    # SAS
    y_position -= 20
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(DARK_GRAY)
    c.drawString(LEFT_MARGIN, y_position, "SAS")
    
    y_position -= 15
    c.setFont("Helvetica", 10)
    c.drawString(LEFT_MARGIN, y_position, "SAS CERTIFIED SPECIALIST: BASE PROGRAMMING USING SAS 9.4")
    c.setFillColor(LIGHT_GRAY)
    c.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, y_position, "2020")
    
    y_position -= 14
    c.setFont("Helvetica", 8)
    c.setFillColor(HexColor("#0066CC"))
    c.drawString(LEFT_MARGIN + 10, y_position, "• https://www.credly.com/badges/c94d7c74-2a21-41bb-8df6-fe2e605eea87/public_url")
    
    return y_position - 20

def draw_languages(c, y_position):
    """Draw languages section"""
    y_position = draw_section_header(c, y_position, "Languages")
    
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(DARK_GRAY)
    c.drawString(LEFT_MARGIN, y_position, "Italiano")
    y_position -= 14
    c.setFont("Helvetica", 9)
    c.setFillColor(LIGHT_GRAY)
    c.drawString(LEFT_MARGIN, y_position, "MOTHER TONGUE")
    
    y_position -= 20
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(DARK_GRAY)
    c.drawString(LEFT_MARGIN, y_position, "English")
    y_position -= 14
    c.setFont("Helvetica", 9)
    c.setFillColor(LIGHT_GRAY)
    c.drawString(LEFT_MARGIN, y_position, "B2")
    y_position -= 12
    c.setFont("Helvetica", 8)
    c.setFillColor(HexColor("#0066CC"))
    c.drawString(LEFT_MARGIN + 10, y_position, "• https://bestr.it/award/show/DMl8BEZ3QCeI0KKNu9YVxg")
    
    return y_position - 20

def draw_footer(c, y_position, page_number=1):
    """Draw footer with privacy notice"""
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(LIGHT_GRAY)
    privacy_text = "I authorize the processing of my personal data contained in my curriculum vitae in accordance with Legislative"
    c.drawString(LEFT_MARGIN, y_position, privacy_text)
    y_position -= 12
    c.drawString(LEFT_MARGIN, y_position, "Decree 196/2003 and EU Regulation 2016/679.")

    # Page number
    y_position -= 30
    c.setFont("Helvetica", 9)
    c.setFillColor(DARK_GRAY)
    c.drawCentredString(PAGE_WIDTH / 2, y_position, f"FRANCESCO COLICINO · CURRICULUM VITAE · {page_number}")

def create_cv(output_path):
    """Main function to create the CV"""
    c = canvas.Canvas(output_path, pagesize=A4)

    # Page 1 - Main content
    y_position = PAGE_HEIGHT - TOP_MARGIN

    # Draw sections for page 1
    y_position = draw_header(c, y_position)
    y_position = draw_employment(c, y_position)
    y_position = draw_education(c, y_position)
    y_position = draw_skills(c, y_position)

    # Draw footer for page 1
    draw_footer(c, 2 * cm, page_number=1)

    # Start new page for Certifications and Languages
    c.showPage()

    # Page 2 - Certifications and Languages
    y_position = PAGE_HEIGHT - TOP_MARGIN

    y_position = draw_certifications(c, y_position)
    y_position = draw_languages(c, y_position)

    # Draw footer for page 2
    draw_footer(c, 2 * cm, page_number=2)

    # Save PDF
    c.save()
    print(f"CV created successfully: {output_path}")

if __name__ == "__main__":
    output_file = "Francesco_Colicino.pdf"
    create_cv(output_file)
