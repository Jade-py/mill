from django.shortcuts import render, HttpResponse
from fpdf import FPDF
from fpdf.enums import XPos, YPos
import datetime


class InvoicePDF(FPDF):
    def header(self):
        pass

    def footer(self):
        pass

def create_bill(request):
    return render(request, 'bills/create-bill.html')


# Create your views here.
def print_bill(request):
    try:
        transportation_mode = request.POST.get('transportation_mode', '')
        vehicle_no = request.POST.get('vehicle_no', '')
        supply_datetime = request.POST.get('supply_datetime', '')
        supply_place = request.POST.get('supply_place', '')
        invoice_number = request.POST.get('invoice_number', '')
        date = request.POST.get('date', '')
        receiver_name = request.POST.get('receiver_name', '')
        receiver_address = request.POST.get('receiver_address', '')
        receiver_state = request.POST.get('receiver_state', '')
        receiver_state_code = request.POST.get('receiver_state_code', '')
        receiver_gstin = request.POST.get('receiver_gstin', '')
        consignee_name = request.POST.get('consignee_name', '')
        consignee_address = request.POST.get('consignee_address', '')
        consignee_state = request.POST.get('consignee_state', '')
        consignee_state_code = request.POST.get('consignee_state_code', '')
        consignee_gstin = request.POST.get('consignee_gstin', '')
        total_x = request.POST.get('total_x', '')
        total_amount_words = request.POST.get('total_amount_words', '')
        total_before_tax = request.POST.get('total_before_tax', '')
        cgst = request.POST.get('cgst', '')
        sgst = request.POST.get('sgst', '')
        igst = request.POST.get('igst', '')
        transportation = request.POST.get('transportation', '')
        total_y = request.POST.get('total_y', '')

        pdf = InvoicePDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=False)
        pdf.add_font("Algerian", "B", "Algerian.ttf")

        # Company Header
        pdf.set_font('Algerian', 'B', 16)
        pdf.multi_cell(72, 8, 'ST. SEBASTIAN TIMBERS', border='LTR', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        pdf.set_font('helvetica', '', 10)
        pdf.multi_cell(72, 5, 'ATHIRAMPUZHA P.O., KOTTAYAM', border='LR', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        pdf.multi_cell(72, 5, 'KERALA - 686 562', border='LR', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        pdf.multi_cell(72, 5, 'Phone: 9947880862, 8157006045', border='LR', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        pdf.multi_cell(72, 5, 'GST IN: 32AAGFS5444L1Z0', border='LBR', new_x=XPos.END, new_y=YPos.TMARGIN, align='C')

        pdf.set_x(pdf.get_x() + 20)

        # Invoice details line
        pdf.set_font('helvetica', 'B', 10)
        pdf.multi_cell(60, 7, f'Transportation Mode: {transportation_mode}', border='LTR', new_x=XPos.LEFT, new_y=YPos.NEXT, padding=[0, 2])
        pdf.multi_cell(60, 7, f'Veh. No: {vehicle_no}', border='LR', new_x=XPos.LEFT, new_y=YPos.NEXT, padding=[0, 2])
        pdf.multi_cell(60, 7, f'Date & Time of Supply: {supply_datetime}', border='LR', new_x=XPos.LEFT, new_y=YPos.NEXT, padding=[0, 2])
        pdf.multi_cell(60, 7, f'Place of Supply: {supply_place}', border='LBR', new_x=XPos.START, new_y=YPos.TMARGIN, padding=[0, 2])

        pdf.set_x(pdf.get_x() + 59)

        pdf.set_font('helvetica', 'B', 10)
        pdf.multi_cell(50, 7, f'Invoice No. {invoice_number}', border='TR', new_x=XPos.LEFT, new_y=YPos.NEXT, padding=[0, 2])
        pdf.multi_cell(50, 7, '', border='R', new_x=XPos.LEFT, new_y=YPos.NEXT)
        pdf.multi_cell(50, 7, '', border='R', new_x=XPos.LEFT, new_y=YPos.NEXT)
        pdf.multi_cell(50, 7, f'Date: {datetime.date.today().strftime('%d-%m-%Y')}', border='BR', new_x=XPos.LEFT,
                       new_y=YPos.NEXT, padding=[0, 2])

        # Receiver and Consignee details
        pdf.set_font('helvetica', 'B', 10)
        y_start = 40
        # Receiver (Left side)
        pdf.set_xy(10, y_start)
        pdf.multi_cell(95, 6, 'Details of Receiver (Billed to):', border='', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        pdf.set_font('helvetica', '', 9)
        pdf.set_x(10)
        pdf.multi_cell(95, 5, f'Name: {receiver_name}', border='LTR', new_x=XPos.LMARGIN, new_y=YPos.NEXT, padding=[0, 2])
        pdf.set_x(10)
        pdf.multi_cell(95, 5, f'Address: {receiver_address}', border='LR', new_x=XPos.LMARGIN, new_y=YPos.NEXT, padding=[0, 2])
        pdf.set_x(10)
        pdf.multi_cell(95, 5, f'State: {receiver_state}', border='LR', new_x=XPos.LMARGIN, new_y=YPos.NEXT, padding=[0, 2])
        pdf.set_x(10)
        pdf.multi_cell(95, 5, f'State Code: {receiver_state_code}', border='LR', new_x=XPos.LMARGIN, new_y=YPos.NEXT, padding=[0, 2])
        pdf.set_x(10)
        pdf.multi_cell(95, 5, f'GSTIN Number: {receiver_gstin}', border='LRB', new_x=XPos.LMARGIN, new_y=YPos.NEXT, padding=[0, 2])

        # Consignee (Right side)
        pdf.set_font('helvetica', 'B', 10)
        pdf.set_xy(105, y_start)
        pdf.multi_cell(95, 6, 'Details of Consignee (Shipped to):', border='', new_x=XPos.LMARGIN, new_y=YPos.NEXT,
                       align='C')
        pdf.set_font('helvetica', '', 9)
        pdf.set_xy(105, y_start + 6)
        pdf.multi_cell(95, 5, f'Name: {consignee_name}', border='LTR', new_x=XPos.LMARGIN, new_y=YPos.NEXT, padding=[0, 2])
        pdf.set_xy(105, y_start + 11)
        pdf.multi_cell(95, 5, f'Address: {consignee_address}', border='LR', new_x=XPos.LMARGIN, new_y=YPos.NEXT, padding=[0, 2])
        pdf.set_xy(105, y_start + 16)
        pdf.multi_cell(95, 5, f'State: {consignee_state}', border='LR', new_x=XPos.LMARGIN, new_y=YPos.NEXT, padding=[0, 2])
        pdf.set_xy(105, y_start + 21)
        pdf.multi_cell(95, 5, f'State Code: {consignee_state_code}', border='LR', new_x=XPos.LMARGIN, new_y=YPos.NEXT, padding=[0, 2])
        pdf.set_xy(105, y_start + 26)
        pdf.multi_cell(95, 5, f'GSTIN Number: {consignee_gstin}', border='LRB', new_x=XPos.LMARGIN, new_y=YPos.NEXT, padding=[0, 2])

        pdf.set_y(y_start + 34)

        # Items table header
        pdf.set_font('helvetica', 'B', 9)
        pdf.set_x(10)
        pdf.multi_cell(10, 6, 'S.No', max_line_height=pdf.font_size, border=1, align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.multi_cell(39, 6, 'Description of Goods', max_line_height=pdf.font_size, border=1, align='C', new_x=XPos.RIGHT,
                       new_y=YPos.TOP)
        pdf.multi_cell(25, 6, 'HSN ACS/UOM', max_line_height=pdf.font_size, border=1, align='C', new_x=XPos.RIGHT,
                       new_y=YPos.TOP)
        pdf.multi_cell(15, 6, 'Qty', max_line_height=pdf.font_size, border=1, align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.multi_cell(25, 6, 'Rate', max_line_height=pdf.font_size, border=1, align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.multi_cell(20, 6, 'Amount', max_line_height=pdf.font_size, border=1, align='C', new_x=XPos.RIGHT,
                       new_y=YPos.TOP)
        pdf.multi_cell(16, 6, 'Discount', max_line_height=pdf.font_size, border=1, align='C', new_x=XPos.RIGHT,
                       new_y=YPos.TOP)
        pdf.multi_cell(20, 6, 'Taxable Value', max_line_height=pdf.font_size, border=1, align='C', new_x=XPos.RIGHT,
                       new_y=YPos.TOP)
        pdf.multi_cell(20, 6, 'Total', max_line_height=pdf.font_size, border=1, align='C', new_x=XPos.LMARGIN,
                       new_y=YPos.NEXT)

        # Item 1
        pdf.set_font('helvetica', '', 9)
        pdf.set_x(10)
        pdf.multi_cell(10, 10, '1', max_line_height=pdf.font_size, border='LR', align='C', new_x=XPos.RIGHT, new_y=YPos.TOP,
                       padding=[2, 0])
        pdf.multi_cell(39, 10, 'Rubber load packing case materials', max_line_height=pdf.font_size, border='LR', align='C',
                       new_x=XPos.RIGHT, new_y=YPos.TOP, padding=[2, 0])
        pdf.multi_cell(25, 10, '44044010', max_line_height=pdf.font_size, border='LR', align='C', new_x=XPos.RIGHT,
                       new_y=YPos.TOP, padding=[2, 0])
        pdf.multi_cell(15, 10, 'CFT 62X15X155', max_line_height=pdf.font_size, border='LR', align='C', new_x=XPos.RIGHT,
                       new_y=YPos.TOP, padding=[2, 0])
        pdf.multi_cell(25, 10, '2A6.15X220', max_line_height=pdf.font_size, border='LR', align='C', new_x=XPos.RIGHT,
                       new_y=YPos.TOP, padding=[2, 0])
        pdf.multi_cell(20, 10, '', max_line_height=pdf.font_size, border='LR', align='C', new_x=XPos.RIGHT, new_y=YPos.TOP,
                       padding=[2, 0])
        pdf.multi_cell(16, 10, '', border='LR', align='C', new_x=XPos.RIGHT, new_y=YPos.TOP, padding=[2, 0])
        pdf.multi_cell(20, 10, '', border='LR', align='C', new_x=XPos.RIGHT, new_y=YPos.TOP, padding=[2, 0])
        pdf.multi_cell(20, 10, '161160.00', max_line_height=pdf.font_size, border='LR', align='C', new_x=XPos.LMARGIN,
                       new_y=YPos.NEXT, padding=[2, 0])

        pdf.multi_cell(10, 10, '1', max_line_height=pdf.font_size, border='LR', align='C', new_x=XPos.RIGHT, new_y=YPos.TOP,
                       padding=[2, 0])
        pdf.multi_cell(39, 10, 'Rubber load packing case materials', max_line_height=pdf.font_size, border='LR', align='C',
                       new_x=XPos.RIGHT, new_y=YPos.TOP, padding=[2, 0], )
        pdf.multi_cell(25, 10, '44044010', max_line_height=pdf.font_size, border='LR', align='C', new_x=XPos.RIGHT,
                       new_y=YPos.TOP, padding=[2, 0])
        pdf.multi_cell(15, 10, 'CFT 62X15X155', max_line_height=pdf.font_size, border='LR', align='C', new_x=XPos.RIGHT,
                       new_y=YPos.TOP, padding=[2, 0])
        pdf.multi_cell(25, 10, '2A6.15X220', max_line_height=pdf.font_size, border='LR', align='C', new_x=XPos.RIGHT,
                       new_y=YPos.TOP, padding=[2, 0])
        pdf.multi_cell(20, 10, '', max_line_height=pdf.font_size, border='LR', align='C', new_x=XPos.RIGHT, new_y=YPos.TOP,
                       padding=[2, 0])
        pdf.multi_cell(16, 10, '', border='LR', align='C', new_x=XPos.RIGHT, new_y=YPos.TOP, padding=[2, 0])
        pdf.multi_cell(20, 10, '', border='LR', align='C', new_x=XPos.RIGHT, new_y=YPos.TOP, padding=[2, 0])
        pdf.multi_cell(20, 10, '161160.00', max_line_height=pdf.font_size, border='LR', align='C', new_x=XPos.LMARGIN,
                       new_y=YPos.NEXT, padding=[2, 0])

        pdf.multi_cell(10, 90, '', max_line_height=pdf.font_size, border='LR', align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.multi_cell(39, 90, '', max_line_height=pdf.font_size, border='LR', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.multi_cell(25, 90, '', max_line_height=pdf.font_size, border='LR', align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.multi_cell(15, 90, '', max_line_height=pdf.font_size, border='LR', align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.multi_cell(25, 90, '', max_line_height=pdf.font_size, border='LR', align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.multi_cell(20, 90, '', max_line_height=pdf.font_size, border='LR', align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.multi_cell(16, 90, '', max_line_height=pdf.font_size, border='LR', align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.multi_cell(20, 90, '', max_line_height=pdf.font_size, border='LR', align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.multi_cell(20, 90, '', max_line_height=pdf.font_size, border='LR', align='C', new_x=XPos.LMARGIN,
                       new_y=YPos.NEXT)

        pdf.multi_cell(10, 10, '', max_line_height=pdf.font_size, border=1, align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.multi_cell(64, 10, 'TOTAL', max_line_height=pdf.font_size, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP,
                       align='C')
        pdf.multi_cell(15, 10, f'{total_x}', max_line_height=pdf.font_size, border=1, align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.multi_cell(25, 10, '', max_line_height=pdf.font_size, border=1, align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.multi_cell(20, 10, '', max_line_height=pdf.font_size, border=1, align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.multi_cell(16, 10, '', max_line_height=pdf.font_size, border=1, align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.multi_cell(20, 10, '', max_line_height=pdf.font_size, border=1, align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.multi_cell(20, 10, '', max_line_height=pdf.font_size, border=1, align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Amount in words
        pdf.set_font('helvetica', '', 10)
        pdf.set_x(10)

        pdf.rect(10, 208, 190, 50)

        pdf.multi_cell(114, 6,
                       f'**Total Amount (in Words):** {total_amount_words} rupees only',
                       new_x=XPos.LEFT, new_y=YPos.NEXT, markdown=True, padding=[4, 0])

        pdf.set_xy(14, pdf.get_y() + 10)
        pdf.multi_cell(100, 6, 'Bank Account Number           2491261005117', max_line_height=6, new_x=XPos.LEFT, border=1,
                       new_y=YPos.NEXT, markdown=True)
        pdf.multi_cell(100, 6, 'Bank Branch IFSC                 CNRB0002491', max_line_height=6, new_x=XPos.LMARGIN,
                       border=1, new_y=YPos.NEXT, markdown=True)

        pdf.line(60, 238, 60, 250)

        pdf.set_xy(124, 208)

        pdf.set_x(124)  # Reset to left edge
        pdf.multi_cell(56, 6, 'Total Amount Before Tax', border='LBR', new_x=XPos.RIGHT,
                       new_y=YPos.TOP)  # Label - moves RIGHT
        pdf.multi_cell(20, 6, f'{total_before_tax}', border='BR', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        pdf.set_x(124)  # Reset to left edge
        pdf.multi_cell(56, 6, 'CGST', border='LBR', new_x=XPos.RIGHT, new_y=YPos.TOP)  # Label - moves RIGHT
        pdf.multi_cell(20, 6, f'{cgst}', border='BR', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        pdf.set_x(124)  # Reset to left edge
        pdf.multi_cell(56, 6, 'SGST', border='LBR', new_x=XPos.RIGHT, new_y=YPos.TOP)  # Label - moves RIGHT
        pdf.multi_cell(20, 6, f'{sgst}', border='BR', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        pdf.set_x(124)  # Reset to left edge
        pdf.multi_cell(56, 6, 'IGST', border='LBR', new_x=XPos.RIGHT, new_y=YPos.TOP)  # Label - moves RIGHT
        pdf.multi_cell(20, 6, f'{igst}', border='BR', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        pdf.set_x(124)  # Reset to left edge
        pdf.multi_cell(56, 6, 'Transportation', border='LBR', new_x=XPos.RIGHT, new_y=YPos.TOP)  # Label - moves RIGHT
        pdf.multi_cell(20, 6, f'{transportation}', border='BR', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        pdf.set_x(124)  # Reset to left edge
        pdf.multi_cell(56, 6, 'TOTAL', border='LBR', new_x=XPos.RIGHT, new_y=YPos.TOP)  # Label - moves RIGHT
        pdf.multi_cell(20, 6, f'{total_y}', border='BR', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        pdf.set_x(124)  # Reset to left edge
        pdf.multi_cell(76, 7, 'Certified that the particulars given above are true and correct', border='LR',
                       new_x=XPos.RIGHT, new_y=YPos.TOP)  # Label - moves RIGHT

        pdf.set_font('helvetica', 'B', 10)
        pdf.set_xy(10, 275)
        pdf.multi_cell(190, 2, 'For ST. SEBASTIAN TIMBERS', max_line_height=pdf.font_size, align='R', new_x=XPos.LEFT,
                       new_y=YPos.NEXT, padding=[2, 0])
        pdf.set_font('helvetica', '', 10)
        pdf.multi_cell(180, 2, 'Managing Partner', max_line_height=pdf.font_size, align='R', new_x=XPos.LEFT,
                       new_y=YPos.NEXT, padding=[2, 0])

        pdf_output = pdf.output()
        response = HttpResponse(bytes(pdf_output), content_type='application/pdf')
        return response
    except Exception as e:
        # Return error as plain text to see what went wrong
        return HttpResponse(f"Error generating PDF: {str(e)}", content_type='text/plain')
