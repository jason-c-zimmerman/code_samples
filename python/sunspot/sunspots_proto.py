from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from data import data

drawing = Drawing(200,150)

pred = [row[5] for row in data]
high = [row[6] for row in data]
low = [row[7] for row in data]
times = [200 * ((row[0] + row[1] / 12.0) - 2018)-110 for row in data]


drawing.add(PolyLine(zip(times, pred), strokeColor=colors.blue))
drawing.add(PolyLine(zip(times, high), strokeColor=colors.red))
drawing.add(PolyLine(zip(times, low), strokeColor=colors.green))
drawing.add(String(65,115,'Sunspots', fontSize = 18, fillColor=colors.red))

renderPDF.drawToFile(drawing, 'report1.pdf', 'Sunspots')